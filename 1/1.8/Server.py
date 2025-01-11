class Data:
    def __init__(self, data, destination):
        self.data = data
        self.destination = destination


class Server:
    count = 0

    def __init__(self):
        Server.count += 1
        self.ip = Server.count
        self.buffer = []

    def send_data(self, data: Data):
        Router.buffer.append(data)

    def get_data(self):
        data = list(self.buffer)
        self.buffer.clear()
        return data

    def get_ip(self):
        return self.ip



class Router:
    linked_servers = []
    buffer = []

    @classmethod
    def link(cls, server: Server):
        if server not in cls.linked_servers:
            cls.linked_servers.append(server)

    @classmethod
    def unlink(cls, server: Server):
        if server in cls.linked_servers:
            cls.linked_servers.remove(server)

    @classmethod
    def send_data(cls):
        cls.buffer = [
            packet for packet in cls.buffer
            if not any(
                packet.destination == server.ip and not server.buffer.append(packet)
                for server in cls.linked_servers
            )
        ]

########################

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello2", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

print(msg_lst_to)
print(msg_lst_from)