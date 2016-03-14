#  _*_ coding:utf-8 _*_
"""Test mail room."""
import pytest

TEST_VALIDATOR = {
    ("send a thank you", True),
    ("create a report", False),
    ("typo", "error")
}


@pytest.mark.parametrize("fn, result", TEST_VALIDATOR)
def test_validator(fn, result):
    """Test validator function."""
    from mail_room import validator
    assert validator(fn) == result

test_dict = {'david': {"name": "david", "total": 100}, "Cris": {"name": "cris", "ammt": 400}}

TEST_IN_DICT = {
    ("david", True),
    ("Cris", True),
    ("Alison", False)
}


@pytest.mark.parametrize("fn, result", TEST_IN_DICT)
def test_check_dict(fn, result):
    """Test check_dict function."""
    from mail_room import check_dict
    assert check_dict(fn, test_dict) == result


email_text = "Dear {},\nThank you so much for you donation of ${}. You are a good person.\n"


def test_send_email():
    """Test send_email function."""
    from mail_room import send_email
    assert send_email("David", 100) == "Dear David,\nThank you so much for you donation of $100. You are a good person.\n"


def test_create_list():
    """Test create_list function."""
    from mail_room import create_list
    test_list = create_list(test_dict)
    assert "david" in test_list
