# Задача №1
# Реализуйте класс Temperature, описывающий температуру в градусах Цельсия.
# У класса должен быть:
# конструктор, принимающий температуру Temperature(celsius: int) .
# метод доступа к значению температуры get_value() .
# метод to_fahrenheit() , переводящий температуру в градусы Фаренгейта по формуле F = C * 9/5 + 32.
# метод to_kelvin() , переводящий температуру в кельвины по формуле K = C + 273 .
# метод is_positive() , проверяющий, положительная ли температура.
# статический метод compare(t1, t2) , сравнивающий две температуры и возвращающий -1,
# если первая температура больше второй, 0 если они равны, и 1 если вторая температура больше первой.

class Temperature:

    __celsius: int

    def __init__(self, celsius: int):

        if not isinstance(celsius, int): raise TypeError("Должен быть тип int")
        if celsius < -273.14: raise ValueError("Не забывай про абсолютный ноль")

        self.__celsius = celsius

    def to_fahrenheit(self):

        F = self.__celsius * (9 / 5) + 32
        return F

    def to_kelvin(self):

        K = self.__celsius + 273.14
        return K

    def is_positive(self):

        if self.__celsius > 0 and self.to_fahrenheit() > 0 and self.to_kelvin() > 0:
            return True

        return False

    def get_value(self):
        return (f"По Цельсию: {self.__celsius} C\n"
                f"По Фаренгейту: {self.to_fahrenheit()} F\n"
                f"По Кельвину: {self.to_kelvin()} K")

    @staticmethod
    def compare(t1, t2):

        if t1.__celsius > t2.__celsius: return -1
        elif t1.__celsius < t2.__celsius: return 1
        elif t1.__celsius == t2.__celsius: return 0

# temp_1 = Temperature(0)
# temp_2 = Temperature(-273)
# print("-" * 20)
# print(temp_1.to_fahrenheit())
# print(temp_1.to_kelvin())
# print(temp_1.get_value())
# print((temp_1.is_positive()))
# print("-" * 20)
# print(temp_2.to_fahrenheit())
# print(temp_2.to_kelvin())
# print(temp_2.get_value())
# print((temp_2.is_positive()))
# print("-" * 20)
# print(temp_1.compare(temp_1, temp_2))
# print(temp_2.compare(temp_1, temp_2))


# Задача №2
# Создайте класс LibraryBook, описывающий книгу в библиотеке.
# У класса должен быть:
# конструктор, принимающий название, автора и год издания Library(title: str,
# author: str, publish_year: int).
# Методы доступа к названию, автору и году.
# Метод rename(new_title), меняющий название книги.
# Метод info(), возвращающий строку с краткой информацией о книге.
# Методы ниже в качестве параметра принимают текущий год!
# Метод is_old(current_year), проверяющий, является ли книга старше 50 лет.
# Метод age(current_year), возвращающий возраст книги.

class LibraryBook:

    __title: str
    __autor: str
    __year_publication: int

    def __init__(self, title: str, autor: str, year_publication: int):
        if not isinstance(title, str) or not isinstance(autor, str):
            raise TypeError("type: str")

        if not isinstance(year_publication, int):
            raise TypeError("type: int")

        self.__title = title
        self.__autor = autor
        self.__year_publication = year_publication

    def get_title(self):
        return self.__title

    def get_autor(self):
        return self.__autor

    def get_year_publication(self):
        return self.__year_publication

    def rename_title(self, new_title: str):

        if not isinstance(new_title, str):
            raise TypeError("type: str")

        if new_title != self.__title:
            self.__title = new_title

    def info(self):
        return f"Книга: {self.__title}. Автор: {self.__autor}. Год издания: {self.__year_publication} г."

    def is_old(self, current_year: int):

        if not isinstance(current_year, int):
            raise TypeError("type: int")

        if current_year - self.__year_publication > 50:
            return True

        return False

    def age(self, current_year: int):

        if not isinstance(current_year, int):
            raise TypeError("type: int")
        return current_year - self.__year_publication

# book = LibraryBook("Аэлита", "А.Н. Толстой", 1923)
# print(book.info())
# book.rename_title("Гиперболоид инженера Гарина")
# print(book.info())
# print(book.is_old(2026))
# print(book.age(2026))
