class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author
    @property
    def name(self) -> str:
        return self._name
    @property
    def author(self)-> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages
    @property
    def pages(self):
        return self._pages
    @property
    def pages(self, new_pages):
        if not isinstance(new_pages, int):
            raise TypeError('new_pages должен быть тип int')
        if new_pages < 0:
            raise ValueError('new_pages > 0!!!')
        self._pages = new_pages

    def __str__(self):
        return f"Книга бумажная {self.name}. Автор {self.author}. Странницы {self._pages}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self._pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration
    @property
    def duration(self):
        return self._duration
    @property
    def duration(self, new_duration):
        if not isinstance(new_duration, int):
            raise TypeError('new_duration должен быть тип int')
        if new_duration <= 0:
            raise ValueError('new_duration > 0!!!')
        self._duration = new_duration

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность {self._duration}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self._duration!r})"
\