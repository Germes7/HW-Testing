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

    celsius: int

    def __init__(self, celsius: int):
        self.__celsius = celsius

        if not isinstance(celsius, int): raise ValueError("Должен быть тип int")

    def to_fahrenheit(self):

        F = self.__celsius * (9 / 5) + 32
        return F

    def to_kelvin(self):

        K = self.__celsius + 273.14
        return K

    def is_positive(self):

        if self.__celsius > 0 and self.to_fahrenheit() > 0 and self.to_kelvin() > 0:
            return "Температуры все градусных систем, положительны"

        return "Какая либо (или все) из температурных систем, отрицательная (либо = 0)"

    def get_value(self):
        return (f"По Цельсию: {self.__celsius} C\n"
                f"По Фаренгейту: {self.to_fahrenheit()} F\n"
                f"По Кельвину: {self.to_kelvin()} K")

    @staticmethod
    def compare(t1, t2):

        if t1.__celsius > t2.__celsius: return -1
        elif t1.__celsius < t2.__celsius: return 1
        else: return 0


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
