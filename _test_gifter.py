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