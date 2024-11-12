import pytest

#1
def is_even(number):
    return number % 2 == 0

@pytest.mark.parametrize("number, expected", [(2, True)])

def test_is_even(number, expected):
    assert is_even(number) == expected

#2
def calculate_area(length, width):
    return length * width

@pytest.mark.parametrize("length, width, expected", [(2, 3, 6)])

def test_calculate_area(length, width, expected):
    assert calculate_area(length, width) == expected

#3
def classify_triangle(a, b, c):
    if a == b == c:
        return "равносторонний"
    elif a == b or b == c or a == c:
        return "равнобедренный"
    else:
        return "разносторонний"

@pytest.mark.parametrize("a, b, c, expected", [(3, 3, 3, "равносторонний")])

def test_classify_triangle(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected