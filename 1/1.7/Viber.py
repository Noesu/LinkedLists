class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False


class Viber:
    chat = []

    @classmethod
    def add_message(cls, msg: Message):
        cls.chat.append(msg)

    @classmethod
    def remove_message(cls, msg: Message):
        cls.chat.remove(msg)

    @staticmethod
    def set_like(msg: Message):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, count):
        print(msg.text for msg in cls.chat[count])

    @classmethod
    def total_messages(cls):
        return len(cls.chat)


####################

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)