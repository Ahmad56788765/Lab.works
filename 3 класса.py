# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class VideoGames:
    def __init__(self, name: str, weight: int, price: int):
        """
        создание объекта "видео игра"
        :name: Наименование игры
        :weight: Её вес занимаемой на устройстве
        :price:Цена игры в рублях
        Пример:
        >>> vige = VideoGames("Raid", 6.37, 2)
        """
        if not isinstance(name, str):
            raise TypeError("Имя не тип str")
        if weight <= 0:
            raise ValueError("игра не можеть иметь вес равной или ниже 0")
        if price < 0:
            raise ValueError("игра не можеть иметь цену ниже 0")
        self.name = name
        self.weight = weight
        self.price = price
    def weigt_of_the_updated_game(self, new_weight: int)->None:
        """
        в случае обновление игры вес её меняется этот методэто фиксирует в гигабайтах
        :new_waigt: Вес который прибовляется
        :ValueError: ПОсле обновление игра не может весить 0 или меньше
        Пример:
        >>> vige = VideoGames("Raid", 5.6, 0)
        >>> vige.weigt_of_the_updated_game(1)
        """
        if not isinstance(new_weight, (int, float)):
            raise TypeError("не тот тип")
        if self.weight <= -new_weight:
            raise ValueError("недопустимое значение веса")
        ...
    def new_price(self, price2):
        """
        часто цена игры меняется например во время скидки
        :price2: новая цена
        :ValueError: новая цена не может быть ниже 0
        Пример:
        >>> v_g = VideoGames("Terraria", 0.61, 1100)
        >>> v_g.new_price(0)
        """
        if price2<0:
            raise ValueError("видео игра не можеть быть иметь отрицательную цену")
        ...
class Point:
    def __init__(self, name: str, x: int, y: int):
        """
        создание объекта "точка"
        :name: Наименование Точки
        :x: координата по x
        :y: координата по y
        Пример:
        >>> T = Point("A", 0, 7)
        """
        if not isinstance(name, str):
            raise TypeError("Имя не тип str")
        if not isinstance(x, int):
            raise TypeError("y не тип int")
        if not isinstance(y, int):
            raise TypeError("y не тип int")
        self.name = name
        self.x = x
        self.y = y
    def koordinate_x(self, new_x: int)->None:
        """
        если нужно перемистить точку по оси x
        :new_x: Новая координата
        :TypeError: НЕ тот тип
        >>> T = Point("A", 7, 5)
        >>> T.koordinate_x(4)
        """
        if not isinstance(new_x, (int, float)):
            raise TypeError("не тот тип")
        ...
    def dlina_ot_new_T1(self, x2: int, y2: int ):
        """
        можно задать координату иной точки и измерить длину
        :x2, y2: новые координаты
        :ValueError: координаты не должны соовпадать
        Пример:
        >>> T1 = Point("A", 0, 0)
        >>> T1.dlina_ot_new_T1(1, 1)
        """
        if self.x == x2 and self.y == y2:
            raise ValueError("координаты соовпадают")
        ...
class Children:
    def __init__(self, name: str, born_year: int):
        """
        создание объекта "ребонок"
        :name: Имя ребенка
        :born_year: год рождение
        Пример:
        >>> children1 = Children("Maкс", 2005)
        """
        if not isinstance(name, str):
            raise TypeError("Имя не тип str")
        if not isinstance(born_year, int):
            raise TypeError("y не тип int")
        self.name = name
        self.born_year = born_year
    def Oldest(self)->int:
        """
        если нужно узнать возрост ребенка
        >>> ch1 = Children("Marc", 2007)
        >>> ch1.Oldest()
        """
        ...
    def Children_True(self)-> bool:
        """по году рождение узнает реально ли он ребенок
        Пример:
        >>> ch = Children("Вася", 2007)
        >>> ch.Children_True()
        """
        ...






if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
