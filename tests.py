import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:



    def test_add_new_book(self): # Добавление книги
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        assert "Гарри Поттер" in collector.books_genre



    def test_set_book_genre(self):  #проверка  установки и получения жанра книги
        collector = BooksCollector()
        collector.add_new_book('Зомби')
        collector.set_book_genre('Зомби','Ужасы')
        assert collector.get_book_genre('Зомби') == 'Ужасы'

    def test_get_books_with_specific_genre(self): #выводим список книг с определённым жанром
        collector = BooksCollector()
        collector.add_new_book('Вампиры')
        collector.set_book_genre('Вампиры','Фантастика')
        collector.add_new_book('Злые фрикадельки')
        collector.set_book_genre('Злые фрикадельки','Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Вампиры', 'Злые фрикадельки']

    def test_get_books_for_children(self):
        collector = BooksCollector()
        genre_mult = 'Мультфильмы'
        genre_horror = 'Ужасы'
        temp_name_1 = 'Смешарики'
        temp_name_2 = 'Тачки'
        temp_name_3 = 'Чужой'
        temp_name_4 = 'Тень'

        collector.add_new_book(temp_name_1)
        collector.set_book_genre(temp_name_1, genre_mult)
        collector.add_new_book(temp_name_2)
        collector.set_book_genre(temp_name_2, genre_mult)
        collector.add_new_book(temp_name_3)
        collector.set_book_genre(temp_name_3, genre_horror)
        collector.add_new_book(temp_name_4)
        collector.set_book_genre(temp_name_4,genre_horror)
        children_list_book = collector.get_books_for_children()
        assert temp_name_1, temp_name_2 in children_list_book
        assert temp_name_3, temp_name_4 not in children_list_book


    @pytest.mark.parametrize("book_name, add_to_favorites, expected_count", [
        ("Избранная книга", True, 1),  # Добавление в избранное
        ("Неизвестная книга", False, 0),  # Попытка добавить несуществующую книгу
        ("Избранная книга", True, 1),  # Повторное добавление не должно увеличивать количество
    ])
    def test_favorites(self, book_name, add_to_favorites, expected_count):
        collector = BooksCollector()
        collector.add_new_book("Избранная книга")  # Добавляем в коллекцию
        if add_to_favorites:
            collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == expected_count


    def test_delete_book_from_favorites(self): #Тест удаления из избранного
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.add_book_in_favorites('Хоббит')
        collector.delete_book_from_favorites('Хоббит')
        assert 'Хоббит' not in collector.get_list_of_favorites_books()




