from code_verifier import CodeVerifier, CodeError

def test_validate_valid_code():
    code = 'x = 5\ny = 10'
    verifier = CodeVerifier(code)
    errors = verifier.validate()
    assert not errors

def test_validate_invalid_assignment():
    code = 'x =\ny = 10'
    verifier = CodeVerifier(code)
    errors = verifier.validate()
    assert len(errors) == 1
    assert errors[0].line == 1
    assert errors[0].column == 2
    assert errors[0].message == 'Invalid assignment'

def test_validate_missing_except_block():
    code = 'try:\n    x = 5\ny = 10'
    verifier = CodeVerifier(code)
    errors = verifier.validate()
    assert len(errors) == 1
    assert errors[0].line == 1
    assert errors[0].column == 0
    assert errors[0].message == 'Missing except block'

def test_format_errors():
    errors = [CodeError(1, 2, 'Invalid assignment'), CodeError(3, 4, 'Missing except block')]
    verifier = CodeVerifier('')
    formatted_errors = verifier.format_errors(errors)
    assert formatted_errors == 'Line 1, Column 2: Invalid assignment\nLine 3, Column 4: Missing except block'

def test_validate_and_format_valid_code():
    code = 'x = 5\ny = 10'
    verifier = CodeVerifier(code)
    result = verifier.validate_and_format()
    assert result == 'No errors found'

def test_validate_and_format_invalid_code():
    code = 'x =\ntry:\n    y = 10'
    verifier = CodeVerifier(code)
    result = verifier.validate_and_format()
    assert 'Line 1, Column 2: Invalid assignment' in result
    assert 'Line 2, Column 0: Missing except block' in result
