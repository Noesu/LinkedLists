import sys

class MailItem:
    def __init__(self, mail_from: str, title: str, content: str) -> None:
        self.is_read = False
        self.mail_from = mail_from
        self.title = title
        self.content = content

    def __bool__(self) -> bool:
        return self.is_read

    def set_read(self, fl_read: bool) -> None:
        self.is_read = fl_read


class MailBox:
    def __init__(self):
        self.inbox_list = []

    def receive(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        self.inbox_list = [MailItem(*line.split('; ')) for line in lst_in]


mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)
inbox_list_filtered = list(filter(bool, mail.inbox_list))

