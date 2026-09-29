from xml.etree import ElementTree

from aksum_messagebench.engine import compare
from aksum_messagebench.reports import render


def test_html_escape(source, contract):
    report = compare(source, source, contract)
    report["limitations"].append('<script>alert("secret")</script>')
    rendered = render(report, "html")
    assert b"<script>" not in rendered
    assert b"&lt;script&gt;" in rendered
    assert b"default-src 'none'" in rendered


def test_junit_required_unknown_is_error(source, change_contract):
    contract = change_contract(lambda d: d["assertions"][0].update(field="unknown.field"))
    report = compare(source, source, contract)
    tree = ElementTree.fromstring(render(report, "junit"))
    assert tree.get("errors") == "1"
    assert tree.find(".//error") is not None


def test_junit_failure(source, contract, root):
    report = compare(source, root / "corpus/negative/reference-truncated.target.xml", contract)
    tree = ElementTree.fromstring(render(report, "junit"))
    assert tree.get("failures") == "1"
    assert tree.find(".//failure") is not None
