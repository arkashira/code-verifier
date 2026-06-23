import pytest
from code_verifier import verify_code, generate_report

def test_verify_code():
    code = "print('Hello World')"
    report = verify_code(code)
    assert report.accuracy < 1.0
    assert report.reliability < 1.0
    assert "Avoid using print statements" in report.error_messages
    assert "Use logging instead" in report.suggestions

def test_generate_report():
    code = "import os"
    report = generate_report(code)
    assert "Avoid using import statements" in report
    assert "Use relative imports instead" in report

def test_empty_code():
    code = ""
    report = verify_code(code)
    assert report.accuracy == 1.0
    assert report.reliability == 1.0
    assert not report.error_messages
    assert not report.suggestions
