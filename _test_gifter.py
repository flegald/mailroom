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
    assert validator(fn) == result