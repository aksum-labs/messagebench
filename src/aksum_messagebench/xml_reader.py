"""A bounded, non-resolving XML parser. Limits apply while constructing the tree."""

from dataclasses import dataclass

from lxml import etree

from .errors import BenchError
from .input_guard import MAX_BYTES


@dataclass(frozen=True)
class Limits:
    size: int = MAX_BYTES
    depth: int = 64
    elements: int = 100_000
    text: int = 1024 * 1024


class DenyResolver(etree.Resolver):
    def resolve(self, url, public_id, context):
        raise BenchError("EXTERNAL_RESOURCE_FORBIDDEN", 4)


class BoundedTree:
    def __init__(self, limits: Limits):
        self.limits = limits
        self.builder = etree.TreeBuilder()
        self.depth = 0
        self.count = 0
        self.text_count = 0
        self.error: BenchError | None = None

    def reject(self, code):
        self.error = BenchError(code, 4)
        raise self.error

    def start(self, tag, attributes):
        self.depth += 1
        self.count += 1
        self.text_count = 0
        if len(tag) > 512 or len(attributes) > 128 or any(len(k) > 512 for k in attributes):
            self.reject("XML_NAME_OR_ATTRIBUTE_LIMIT")
        if self.depth > self.limits.depth:
            self.reject("XML_DEPTH_LIMIT")
        if self.count > self.limits.elements:
            self.reject("XML_ELEMENT_LIMIT")
        if tag.startswith("{http://www.w3.org/2001/XInclude}"):
            self.reject("XINCLUDE_FORBIDDEN")
        if any(len(v.encode("utf-8")) > self.limits.text for v in attributes.values()):
            self.reject("XML_TEXT_LIMIT")
        if any(
            k in attributes
            for k in (
                "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation",
                "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation",
            )
        ):
            self.reject("SCHEMA_HINT_FORBIDDEN")
        return self.builder.start(tag, attributes)

    def end(self, tag):
        self.depth -= 1
        self.text_count = 0
        return self.builder.end(tag)

    def data(self, data):
        self.text_count += len(data.encode("utf-8"))
        if self.text_count > self.limits.text:
            self.reject("XML_TEXT_LIMIT")
        self.builder.data(data)

    def comment(self, text):
        # Comments are neither financial facts nor coverage units.
        if len(text.encode("utf-8")) > self.limits.text:
            self.reject("XML_TEXT_LIMIT")

    def pi(self, target, text):
        self.reject("XML_PI_FORBIDDEN")

    def doctype(self, name, public_id, system_id):
        self.reject("DTD_FORBIDDEN")

    def close(self):
        if self.error is not None:
            raise self.error
        return self.builder.close()


DEFAULT_LIMITS = Limits()


def parse_xml(data: bytes, limits: Limits = DEFAULT_LIMITS):
    if len(data) > limits.size:
        raise BenchError("INPUT_SIZE_LIMIT", 4)
    parser = etree.XMLParser(
        target=BoundedTree(limits),
        resolve_entities=False,
        load_dtd=False,
        no_network=True,
        dtd_validation=False,
        attribute_defaults=False,
        huge_tree=False,
        recover=False,
        collect_ids=False,
    )
    parser.resolvers.add(DenyResolver())
    try:
        return etree.fromstring(data, parser)
    except etree.XMLSyntaxError:
        raise BenchError("XML_SYNTAX_INVALID", 1) from None
