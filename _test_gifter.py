# -*- coding:utf-8 -*-
import pytest

TEST_VALIDATOR = {
    ('send a thank you', True),
    ('create a report', False)
}

@pytest.mark.parametrize("fn, result", TEST_VALIDATOR)
def test_validator(fn, result):
    from gifter import validator
    assert validator(fn) == result


TEST_PRINT_EMAIL = {
    ("David, 100", "Dear David, \n Thank you so much for your donation of $100. You are one cool cat \n"),
    ("Alison, 200", "Dear Alison, \n Thank you so much for your donation of $200. You are one cool cat \n")
}

@pytest.mark.parametrize("fn, result", TEST_PRINT_EMAIL)
def test_print_email(fn, result):
    from gifter import validator
    assert print_email(fn) == result

TEST_CHECK_DICT = {
    ("David Flegal"),
    ("Alison Maclean"),
    ("Bob Hope")
}

@pytest.mark.parametrize("fn", TEST_CHECK_DICT)
def test_check_dict(fn):
    from gifter import validator
    from gifter import GIFTER_DICT
    check_dict(fn)
    assert fn in GIFTER_DICT

TEST_UPDATE_VALUES = {
    ("david", "100"),
    ("alison", "200"),
    ("barney", "250")
}

@pytest.mark.parametrize("name","ammt", TEST_UPDATE_VALUES)
def test_update_dict(name, ammt):
    from gifter import update_values
    from gifter import GIFTER_DICT
    update_values(name, ammt)
    assert name in GIFTER_DICT
