import json

def load_superheroes(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def save_superheroes(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def add_superheroes(data, new_members):
    data['members'].extend(new_members)

def sort_superheroes_by_age(data):
    data['members'].sort(key=lambda x: x['age'])

def main():
    # Загрузка существующих супергероев
    data = load_superheroes('superhero.json')

    # Новые супергерои
    new_members = [
        {
            "name": "Captain Code",
            "age": 32,
            "secretIdentity": "Code Master",
            "powers": ["Coding", "Debugging", "Problem Solving"]
        },
        {
            "name": "The Enforcer",
            "age": 45,
            "secretIdentity": "John Doe",
            "powers": ["Strength", "Combat Skills", "Tactical Genius"]
        }
    ]

    # Добавление новых супергероев
    add_superheroes(data, new_members)

    # Сортировка по возрасту
    sort_superheroes_by_age(data)

    # Сохранение в новый JSON файл
    save_superheroes('superhero_new.json', data)

if __name__ == "__main__":
    main()
