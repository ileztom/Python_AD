import json
import pytest

def load_superheroes(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def is_older_than_30(superheroes):
    return [member for member in superheroes['members'] if member['age'] > 30]

def test_is_older_than_30():
    data = load_superheroes('superhero_new.json')
    older_members = is_older_than_30(data)

    for member in older_members:
        assert member['age'] > 30

if __name__ == "__main__":
    pytest.main()
