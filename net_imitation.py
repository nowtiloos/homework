from typing import Any


class Data:
    """
    Класс для представления пакета данных для передачи.
    """

    def __init__(self, data: Any, target_ip: int) -> None:
        """
        Инициализирует объект Data.

        :param data: Данные для передачи.
        :type data: Any
        :param target_ip: Целевой IP-адрес сервера.
        :type target_ip: int
        """
        self.data: Any = data
        self.target_ip: int = target_ip

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Data.

        :return: Строковое представление объекта Data.
        :rtype: str
        """
        return f"Data({self.data}, {self.target_ip})"


class Server:
    """
    Класс для представления сервера.
    """
    __get_ip: int = 1

    def __init__(self) -> None:
        """
        Инициализирует экземпляр класса Server.
        По умолчанию сервер не связан с маршрутизатором, а его буфер пуст.
        """
        self.router: Router | None = None
        self.buffer: list = []
        self.ip: int = Server.__get_ip
        Server.__get_ip += 1

    def get_ip(self) -> int:
        """
        Получает IP-адрес сервера.

        :return: IP-адрес сервера.
        :rtype: int
        """
        return self.ip

    def send_data(self, data: Data) -> None:
        """
        Отправляет данные подключенному маршрутизатору.

        :param data: Данные для отправки.
        :type data: Data
        """
        self.router.buffer.append(data)

    def get_data(self) -> list[Data]:
        """
        Получает данные из буфера сервера.

        :return: Список объектов Data из буфера сервера.
        :rtype: list
        """
        result: list[Data] = self.buffer[:]
        self.buffer.clear()
        return result


class Router:
    """
    Класс для представления маршрутизатора
    """
    def __init__(self) -> None:
        """
        Инициализирует экземпляр класса Router.
        """
        self.net: dict = {}
        self.buffer: list = []

    def link(self, server: Server) -> None:
        """
        Устанавливает соединение между сервером и маршрутизатором.

        :param server: Сервер для установки соединения.
        :type server: Server
        """
        self.net.setdefault(server.ip, server.buffer)
        server.router = self

    def unlink(self, server: Server) -> None:
        """
        Разрывает соединение между сервером и маршрутизатором.

        :param server: Сервер для разрыва соединения.
        :type server: Server
        """
        server.router = None
        self.net.pop(server.ip)

    def send_data(self) -> None:
        """
        Пересылает данные из буфера маршрутизатора на соответствующие серверы.
        """
        for data in self.buffer:
            self.net[data.target_ip].append(data)

        self.buffer.clear()
