Для последовательной обработки файлов из некоторого списка, например:

`
filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png", "my.html", "data.shtml"]
`

Необходимо объявить класс **ImageFileAcceptor**, который бы выделял только файлы с указанными расширениями.

Для этого предполагается создавать объекты класса командой:

`acceptor = ImageFileAcceptor(extensions)`

где _extensions_ - кортеж с допустимыми расширениями файлов, например: _extensions = ('jpg', 'bmp', 'jpeg')._

А, затем, использовать объект _acceptor_ в стандартной функции _filter_ языка Python следующим образом:

_image_filenames = filter(acceptor, filenames)_

Пример использования класса (эти строчки в программе писать не нужно):

```
filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]
```

P.S. Ваша задача только объявить класс **ImageFileAcceptor**. На экран ничего выводить не нужно. 