import pytest
from code_verifier import verify_snippet, verify_manifest
import json

def test_verify_snippet_pass():
    snippet = verify_snippet('test.py')
    assert snippet.status == 'PASS'

def test_verify_snippet_fail():
    snippet = verify_snippet('test.txt')
    assert snippet.status == 'FAIL'

def test_verify_manifest_pass():
    manifest = ['test.py', 'test2.py']
    snippets = verify_manifest(manifest)
    assert all(snippet.status == 'PASS' for snippet in snippets)

def test_verify_manifest_fail():
    manifest = ['test.py', 'test.txt']
    snippets = verify_manifest(manifest)
    assert any(snippet.status == 'FAIL' for snippet in snippets)

def test_main_pass(capsys):
    with open('manifest.json', 'w') as f:
        json.dump(['test.py', 'test2.py'], f)
    import sys
    sys.argv = ['code-verifier-cli', '--manifest', 'manifest.json']
    from code_verifier import main
    main()
    captured = capsys.readouterr()
    assert captured.out == "test.py: PASS\ntest2.py: PASS\n"

def test_main_fail(capsys):
    with open('manifest.json', 'w') as f:
        json.dump(['test.py', 'test.txt'], f)
    import sys
    sys.argv = ['code-verifier-cli', '--manifest', 'manifest.json']
    from code_verifier import main
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 1
