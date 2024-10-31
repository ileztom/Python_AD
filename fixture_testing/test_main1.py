from main1 import get_string_length
import pytest

def test_get_string_length():
    assert get_string_length("") == 0

    assert get_string_length("Hello\nWorld") == 11

    assert get_string_length("    ") == 4