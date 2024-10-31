def get_string_length(s: str) -> int:
    return len(s)

def test_get_string_length():
    assert get_string_length("") == 0

    assert get_string_length("Hello\nWorld") == 11

    assert get_string_length("    ") == 4