import pytest
from PyCode.LakeLevel_Temp2 import parse_text


def test_parse_text_happy_path():
    sample = """
Report Date
23 Sep 2025
Some other lines
Current Level
12.34
More text
Surface Temperature
75
"""

    result = parse_text(sample)

    assert result['report']['label'].startswith('Report')
    assert result['report']['value'].startswith('23')
    assert result['lake']['label'].startswith('Current')
    assert result['lake']['value'].startswith('12')
    assert result['temp']['label'].startswith('Surface')
    assert result['temp']['value'].startswith('75')


def test_parse_text_missing_values():
    sample = "No matching patterns here"
    result = parse_text(sample)
    assert result['report']['label'] is None
    assert result['report']['value'] is None
    assert result['lake']['label'] is None
    assert result['temp']['value'] is None


def test_extract_from_url_monkeypatch(monkeypatch):
    """Mock requests.get so extract_from_url can be tested without network access."""
    sample_html = """<html><body>
Report Date
23 Sep 2025
Current Level
12.34
Surface Temperature
75
</body></html>"""

    class DummyResp:
        def __init__(self, text):
            self.text = text

        def raise_for_status(self):
            return None

    import PyCode.LakeLevel_Temp2 as ll

    dummy = DummyResp(sample_html)
    # patch the requests.get used inside the module
    monkeypatch.setattr(ll.requests, 'get', lambda url: dummy)

    result = ll.extract_from_url('https://example.test')

    assert result['report']['label'] and result['report']['value']
    assert result['lake']['label'] and result['lake']['value']
    assert result['temp']['label'] and result['temp']['value']
