if __name__ == "__main__":
    # Write your solution here
    pass
class Child:
    def __init__(self, name: str, age: int, gender: str):
        """
        создание объекта ребенок
        :param name: имя ребенка
        :param age: возрост ребенка
        :param gender: пол ребенка
        атрибуты такого рода не могут свободно менятся
        нельзя просто менять возрост и имя ребенка
        про пол нечего и говорить
        Примеры
        >>>Child1 = Child("max", 12, "men")
        """
        self._name = name
        self._age = age
        self._gender = gender
    @property
    def name(self) -> str:
        return self._name
    @property
    def age(self) -> int:
        return self._age
    @property
    def age(self, new_age: int):
        if not isinstance(new_age, int):
            raise TypeError("не тот тип значение")
        if new_age < 0 or new_age > 17:
            raise ValueError("ребенок не может иметь такой возрост")
        self._age = new_age

    @property
    def gender(self) -> str:
        return self._gender
    def My_Name(self) -> str:
        """
        Функция которая не будет перегруженна ибо атрибуд имя есть как у ребенка так и взрослого
        """
        return f'Мое имя {self.name}'
    def Occupation(self, action: str) -> str:
        """
        Род занятий ребенка могут быть разным менятся много раз """
        return f'Я сейчас {action}'

    def __str__(self) -> str:
        return f"Ребёнок '{self.name}' возроста '{self.age}' пола '{self.gender}'"
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r}, {self.age!r}, {self.gender!r})'

class Adult(Child):
    def __init__(self, name: str, age: int, gender: str, profession: str):
        """
        создание объекта взрослый
        Помимо унаследованных атрибутов добавляется новый профессия
        :param profession: проффесия взрослого
        >>>Adult1 = Adult("Max", 23, "men", "Учитель")
        """
        super().__init__(name, age, gender)
        self.profession = profession
    def __str__(self) -> str:
        """
        Перегрузка ибо добавлен новый атрибут который тоже нужно было отобразить в атрибуте __str___
        хотя чисто технически можно было без отображение всех атрибутов, метод бы работал
        """
        return f"Взрослый '{self.name}' возроста '{self.age}' пола '{self.gender}' работает '{self.profession}'"
    def __repr__(self) -> str:
        """
        Перегрузка в данном случае необходимо иначе метод не работал
        была бы ошибка
        """
        return f'{self.__class__.__name__}({self.name!r}, {self.age!r}, {self.gender!r}, {self.profession!r})'
    def Occupation(self) -> str:
        """
        Род занятий Взрослого это его работа
        """
        return f'Я сейчас работаю {self.profession}'
