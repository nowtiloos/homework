from typing import Any, Optional


class ObjList:
    """
    Класс для представления объекта в связанном списке.
    """
    def __init__(self, data: Any) -> None:
        """
        Инициализирует объект списка.

        :param data: Данные объекта.
        :type data: Any
        """
        self.data: Any = data
        self.__next: Optional['ObjList'] = None
        self.__prev: Optional['ObjList'] = None

    @property
    def next(self) -> Optional['ObjList']:
        """
        Получает следующий объект в списке.

        :return: Следующий объект.
        :rtype: Optional['ObjList']
        """
        return self.__next

    @next.setter
    def next(self, obj: Optional['ObjList']) -> None:
        """
        Устанавливает следующий объект в списке.

        :param obj: Следующий объект.
        :rtype: Optional['ObjList']
        """
        self.__next: Optional['ObjList'] = obj

    @property
    def prev(self) -> Optional['ObjList']:
        """
        Получает предыдущий объект в списке.

        :return: Предыдущий объект.
        :rtype: Optional['ObjList']
        """
        return self.__prev

    @prev.setter
    def prev(self, obj: Optional['ObjList']) -> None:
        """
        Устанавливает предыдущий объект в списке.

        :param obj: Предыдущий объект.
        :rtype: Optional['ObjList']
        """
        self.__prev: Optional['ObjList'] = obj

    @property
    def data(self) -> Any:
        """
        Получает данные объекта.

        :return: Данные объекта.
        :rtype: Any
        """
        return self.__data

    @data.setter
    def data(self, data: Any) -> None:
        """
        Устанавливает данные объекта.

        :param data: Данные объекта.
        :type data: Any
        """
        self.__data: Any = data

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строковое представление объекта.
        :rtype: str
        """
        return f"ObjList({self.data})"


class LinkedList:
    """
    Класс для представления связанного списка объектов.
    """
    def __init__(self) -> None:
        """
        Инициализирует пустой связанный список.
        """
        self.head: Optional[ObjList] = None
        self.tail: Optional[ObjList] = None

    def add_obj(self, obj: ObjList) -> None:
        """
        Добавляет объект в конец связанного списка.

        :param obj: Добавляемый объект.
        :raises ValueError: Если переданный объект не является экземпляром ObjList.
        """
        if not isinstance(obj, ObjList):
            raise ValueError("Неверный тип объекта")
        else:
            if not self.head:
                self.head = self.tail = obj
            else:
                self.tail.next, obj.prev = obj, self.tail
                self.tail = obj

    def remove_obj(self) -> None:
        """
        Удаляет последний объект из связанного списка.
        """
        if self.tail:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        else:
            print("Невозможно удалить элемент из пустого списка")

    def get_data(self) -> list[Optional[ObjList]]:
        """
        Получает данные всех объектов в связанном списке.

        :return: Список данных объектов.
        :rtype: list[Optional[ObjList]]
        """
        current: Optional[ObjList] = self.head
        result: list[Optional[ObjList]] = []
        while current:
            result.append(current.data)
            current = current.next
        return result
