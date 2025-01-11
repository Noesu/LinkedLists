class Graph:
    def __init__(self, data : list):
        self.data = data
        self.is_show = True

    def set_data(self, data):
        self.data = data

    def show_table(self):
        self.display_data()

    def show_graph(self):
        self.display_data('Графическое отображение данных:')

    def show_bar(self):
        self.display_data('Столбчатая диаграмма:')

    def set_show(self, fl_show):
        self.is_show = fl_show

    def display_data(self, text = None):
        if self.is_show:
            if text:
                print(text, end=" ")
            print(*self.data)
        else:
            print("Отображение данных закрыто")

data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()