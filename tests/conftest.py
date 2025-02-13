# tests/conftest.py
import pytest
from api.db.schemas import InMemoryDB, Book, Genre

# This fixture will create a fresh InMemoryDB instance before each test
@pytest.fixture
def setup_db():
    db = InMemoryDB()
    # Initialize the books in memory for testing
    db.books = {
        1: Book(id=1, title="The Hobbit", author="J.R.R. Tolkien", publication_year=1937, genre=Genre.SCI_FI),
        2: Book(id=2, title="The Lord of the Rings", author="J.R.R. Tolkien", publication_year=1954, genre=Genre.FANTASY),
        3: Book(id=3, title="The Return of the King", author="J.R.R. Tolkien", publication_year=1955, genre=Genre.FANTASY),
    }
    return db  # Return the instance of the InMemoryDB
