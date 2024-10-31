import sqlite3
import pytest

@pytest.fixture
def db_connection():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)''')
    conn.commit()

    yield conn

    cursor.execute('''DROP TABLE test_table''')
    conn.commit()
    conn.close()
