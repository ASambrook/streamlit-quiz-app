
def test_pytest():
    """
    Smoketest to validate the functioning of the pytest framework 
    """
    assert 2+2 ==4


from welcome_screen import NameValidator

def test_length_check_valid_names():
    """
    Tests valid name lengths between 3 and 30 characters
    """
    validator = NameValidator()
    assert validator.length_check("Alex") == True
    assert validator.length_check("Freya Hit") == True
    assert validator.length_check("A" * 30) == True


def test_pattern_check_valid_characters():
    validator = NameValidator()
    """
    Tests valid characters within names
    """
    assert validator.pattern_check("Anne-Marie") == True
    assert validator.pattern_check("O'shea") == True
    assert validator.pattern_check("Alex") == True





