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

def test_db_operations(db_connection):
    cursor = db_connection.cursor()

    cursor.execute("INSERT INTO test_table (name) VALUES ('Test Name')")
    db_connection.commit()

    cursor.execute("SELECT name FROM test_table WHERE id = 1")
    result = cursor.fetchone()
    assert result[0] == 'Test Name'
