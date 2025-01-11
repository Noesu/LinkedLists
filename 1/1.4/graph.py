class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data: list):
        self.data = data

    def draw(self):
        for value in self.data:
            if self.LIMIT_Y[0] <= value <= self.LIMIT_Y[1]:
                print(value, end=' ')


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()
