import pytest

from aksum_messagebench.errors import BenchError
from aksum_messagebench.xml_reader import Limits, parse_xml


@pytest.mark.parametrize(
    "payload,code",
    [
        (b'<!DOCTYPE x [<!ENTITY a "secret">]><x>&a;</x>', "DTD_FORBIDDEN"),
        (b'<!DOCTYPE x SYSTEM "https://example.invalid/secret"><x/>', "DTD_FORBIDDEN"),
        (b'<!DOCTYPE x [<!ENTITY a SYSTEM "file:///etc/passwd">]><x>&a;</x>', "DTD_FORBIDDEN"),
        (
            (
                '<?xml version="1.0" encoding="UTF-16"?>'
                '<!DOCTYPE x [<!ENTITY a "secret">]><x>&a;</x>'
            ).encode("utf-16"),
            "DTD_FORBIDDEN",
        ),
        (
            b'<x xmlns:i="http://www.w3.org/2001/XInclude">'
            b'<i:include href="file:///etc/passwd"/></x>',
            "XINCLUDE_FORBIDDEN",
        ),
        (
            b'<x xmlns:s="http://www.w3.org/2001/XMLSchema-instance" s:schemaLocation="a https://example.invalid/a"/>',
            "SCHEMA_HINT_FORBIDDEN",
        ),
        (b'<?stylesheet href="https://example.invalid"?><x/>', "XML_PI_FORBIDDEN"),
        (b"<x>" * 65 + b"</x>" * 65, "XML_DEPTH_LIMIT"),
        (b"<x>" + b"a" * (1024 * 1024 + 1) + b"</x>", "XML_TEXT_LIMIT"),
        (b"<x/>junk", "XML_SYNTAX_INVALID"),
    ],
    ids=lambda value: value if isinstance(value, str) else "xml",
)
def test_rejections(payload, code):
    with pytest.raises(BenchError) as err:
        parse_xml(payload)
    assert err.value.code == code


def test_small_quotas():
    for data, limits, code in [
        (b"<x/>", Limits(size=3), "INPUT_SIZE_LIMIT"),
        (b"<x><a/><b/></x>", Limits(elements=2), "XML_ELEMENT_LIMIT"),
        (b'<x a="12345"/>', Limits(text=4), "XML_TEXT_LIMIT"),
        (b"<x><!--12345--></x>", Limits(text=4), "XML_TEXT_LIMIT"),
    ]:
        with pytest.raises(BenchError) as err:
            parse_xml(data, limits)
        assert err.value.code == code


def test_comment_cannot_split_text_quota():
    with pytest.raises(BenchError) as err:
        parse_xml(b"<x>1234<!--abc-->56</x>", Limits(text=5))
    assert err.value.code == "XML_TEXT_LIMIT"


def test_positive_bounds():
    assert parse_xml(b"<x><a/>1234<!--abc-->5</x>", Limits(text=5)).tag == "x"


def test_name_and_attribute_quotas():
    for data in [
        b'<x xmlns="' + b"a" * 513 + b'"/>',
        b"<x " + b" ".join(f'a{i}="v"'.encode() for i in range(129)) + b"/>",
    ]:
        with pytest.raises(BenchError) as err:
            parse_xml(data)
        assert err.value.code == "XML_NAME_OR_ATTRIBUTE_LIMIT"


@pytest.mark.parametrize(
    "component,version", [("LIBXML_VERSION", (2, 14, 6)), ("LIBXSLT_VERSION", (1, 1, 43))]
)
def test_older_native_profile_fails_closed(monkeypatch, component, version):
    from lxml import etree

    monkeypatch.setattr(etree, component, version)
    with pytest.raises(BenchError) as failure:
        parse_xml(b"<a/>")
    assert failure.value.code == "NATIVE_XML_PROFILE_UNSUPPORTED"
    assert failure.value.exit_code == 3
