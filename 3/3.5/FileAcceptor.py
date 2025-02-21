class FileAcceptor:
    def __init__(self, *extensions: str) -> None:
        self.ext = extensions

    def __call__(self, filename: str):
        return any(filename.endswith(f".{ext}") for ext in self.ext)

    def __add__(self, other: "FileAcceptor") -> "FileAcceptor":
        return FileAcceptor(*self.ext, *other.ext)

########################################################################################################################


filenames_list = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png",
                  "eq_2.xls", "eq_3,png", "text1.sxls", "doc", "doc.docx", "doc."]

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames_list))

assert filenames == ['boat.jpg', 'ans.web.png', 'text.txt', 'www.python.doc', 'my.ava.jpg', 'forest.jpeg', 'eq_1.png',
                     'eq_2.xls']
