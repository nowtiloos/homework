class Data:
    def __init__(self, data, target_ip):
        self.data = data
        self.target_ip = target_ip

    def __repr__(self):
        return self.data


class Server:
    __ip_count = 1

    def __init__(self):
        self.router = None
        self.buffer = []
        self.ip = Server.__ip_count
        Server.__ip_count += 1

    def get_ip(self):
        return self.ip

    def send_data(self, data: Data):
        self.router.buffer.append(data)

    def get_data(self):
        result = self.buffer[:]
        self.buffer.clear()
        return result


class Router:
    def __init__(self):
        self.net = {}
        self.buffer = []

    def link(self, server: Server):
        self.net.setdefault(server.ip, server.buffer)
        server.router = self

    def unlink(self, server: Server):
        server.router = None
        self.net.pop(server.ip)

    def send_data(self):
        for data in self.buffer:
            self.net[data.target_ip].append(data)

        self.buffer.clear()


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)

sv_from.send_data(Data("hello", sv_to.get_ip()))
sv_from2.send_data(Data("hello", sv_to.get_ip()))
sv_to.send_data(Data("hi", sv_from.get_ip()))

router.send_data()
msg_list_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
print(msg_lst_to, msg_list_from)