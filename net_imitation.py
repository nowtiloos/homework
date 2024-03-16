class Data:
    def __init__(self, data, target_ip) -> None:
        self.data = data
        self.target_ip = target_ip

    def __repr__(self) -> str:
        return f"Data({self.data}, {self.target_ip})"


class Server:
    __get_ip = 1

    def __init__(self) -> None:
        self.router = None
        self.buffer = []
        self.ip = Server.__get_ip
        Server.__get_ip += 1

    def get_ip(self) -> int:
        return self.ip

    def send_data(self, data: Data) -> None:
        self.router.buffer.append(data)

    def get_data(self) -> list:
        result = self.buffer[:]
        self.buffer.clear()
        return result


class Router:
    def __init__(self) -> None:
        self.net = {}
        self.buffer = []

    def link(self, server: Server) -> None:
        self.net.setdefault(server.ip, server.buffer)
        server.router = self

    def unlink(self, server: Server) -> None:
        server.router = None
        self.net.pop(server.ip)

    def send_data(self) -> None:
        for data in self.buffer:
            self.net[data.target_ip].append(data)

        self.buffer.clear()
