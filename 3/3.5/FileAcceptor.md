Перед вами стоит задача выделения файлов с определенными расширениями из списка файлов, например:

`
filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
`

Для этого необходимо объявить класс **FileAcceptor**, объекты которого создаются командой:

`acceptor = FileAcceptor(ext1, ..., extN)`

где _ext1, ..., extN_ - строки с допустимыми расширениями файлов, например: _'jpg', 'bmp', 'jpeg'_.

После этого предполагается использовать объект _acceptor_ в стандартной функции _filter_ языка Python следующим образом:

`filenames = list(filter(acceptor, filenames))`

То есть, объект _acceptor_ должен вызываться как функция:

_acceptor(filename)_ 

и возвращать _True_, если файл с именем _filename_ содержит расширения, указанные при создании _acceptor_, и _False_ - в противном случае. Кроме того, с объектами класса **FileAcceptor** должен выполняться оператор:

`acceptor12 = acceptor1 + acceptor2`

Здесь формируется новый объект _acceptor12_ с уникальными расширениями первого и второго объектов. Например:
```python
acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")
```
Пример использования класса (эти строчки в программе писать не нужно):
```python
acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
```
P.S. На экран в программе ничего выводить не нужно.