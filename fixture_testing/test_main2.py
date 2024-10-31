from main2 import save_string_to_file
import pytest

def test_save_string_to_file(tmp_path):
    file_path = tmp_path / "test_file.txt"

    save_string_to_file("Hello, World!", file_path)

    assert file_path.exists()
    with open(file_path, 'r') as file:
        assert file.read() == "Hello, World!"