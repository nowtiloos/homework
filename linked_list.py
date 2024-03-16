class ObjList:
    def __init__(self, data):
        self.data = data
        self.__next = None
        self.__prev = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        self.__prev = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList) -> None:
        if not isinstance(obj, ObjList):
            raise ValueError("Неверный тип объекта")
        else:
            if not self.head:
                self.head = self.tail = obj
            else:
                self.tail.next, obj.prev = obj, self.tail
                self.tail = obj

    def remove_obj(self) -> None:
        if self.tail:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        else:
            print("Невозможно удалить элемент из пустого списка")

    def get_data(self) -> list:
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result
