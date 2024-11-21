from gc import collect

import pytest
from main import BooksCollector

            # класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
                # обязательно указывать префикс Test
class TestBooksCollector:


    def test_add_new_book(self): # Проверка добавление новой  книги
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        assert "Гарри Поттер" in collector.books_genre
        assert len(collector.books_genre) == 1

    def test_set_book_genre(self):  #Проверка  установки  жанра книги
        collector = BooksCollector()
        collector.add_new_book('Зомби')
        collector.set_book_genre('Зомби','Ужасы')
        assert collector.get_book_genre('Зомби') == 'Ужасы'

    def test_get_book_genre(self):  #Проверка  получения   жанра книги
        collector = BooksCollector()
        collector.add_new_book('Зомби')
        collector.set_book_genre('Зомби','Ужасы')
        assert collector.get_book_genre('Зомби') == 'Ужасы'

    def test_get_books_with_specific_genre(self): #Вывод списка книг с определённым жанром
        collector = BooksCollector()
        collector.add_new_book('Вампиры')
        collector.set_book_genre('Вампиры','Фантастика')
        collector.add_new_book('Злые фрикадельки')
        collector.set_book_genre('Злые фрикадельки','Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Вампиры', 'Злые фрикадельки']

    def test_get_books_for_children(self): #Проверка книг подходящих детям
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

    def test_get_books_genre(self):# Проверка получения словаря
        collector = BooksCollector()
        collector.add_new_book('Черви')
        collector.set_book_genre('Черви', 'Фантастика')
        assert collector.get_books_genre() == {"Тестовая книга": "Фантастика"}

    @pytest.mark.parametrize("book_name, add_to_favorites, expected_count", [
             ("Избранная книга", True, 1),
             ("Неизвестная книга", False, 0),
            ("Избранная книга", True, 1),
    ])
    def test_favorites(self, book_name, add_to_favorites, expected_count): #Добавление книг в избранное
        collector = BooksCollector()
        collector.add_new_book("Избранная книга")
        if add_to_favorites:
         collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == expected_count

    def test_delete_book_from_favorites(self): #Проверка удаления из избранного
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.add_book_in_favorites('Хоббит')
        collector.delete_book_from_favorites('Хоббит')
        assert 'Хоббит' not in collector.get_list_of_favorites_books()

    def test_set_book_genre(self): #Проверка установка жанра книги
        collector = BooksCollector()
        collector.add_new_book('Интерстеллар')
        collector.set_book_genre('Интерстеллар', 'Фантастика')
        assert collector.get_book_genre('Интерстеллар') ==  'Фантастика'

    def test_get_books_genre(self):# Проверка получения жанра книги
        collector = BooksCollector()
        collector.add_new_book('Интерстеллар')
        collector.set_book_genre('Интерстеллар', "Фантастика")
        assert collector.get_books_genre() == {'Интерстеллар': 'Фантастика'}








