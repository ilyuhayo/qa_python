import pytest
from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        assert "Book1" in collector.get_books_genre()

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        collector.set_book_genre("Book1", "Фантастика")
        assert collector.get_book_genre("Book1") == "Фантастика"

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        collector.set_book_genre("Book1", "Ужасы")
        assert collector.get_book_genre("Book1") == "Ужасы"

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        collector.set_book_genre("Book1", "Фантастика")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Book1"]

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        collector.set_book_genre("Book1", "Мультфильмы")
        assert collector.get_books_for_children() == ["Book1"]

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Book1")
        collector.add_book_in_favorites("Book1")
        assert "Book1" in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize("book_name", ["Book1", "Book2"])
    def test_delete_book_from_favorites(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()
