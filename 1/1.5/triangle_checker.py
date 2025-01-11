class TriangleChecker:
    def __init__(self, a, b, c):
        self.sides = (self.a, self.b, self.c) = a, b, c


    def is_triangle(self):
        for side in self.sides:
            if type(side) in (int, float) or side <= 0:
                return 1
        return 2 if sum(self.sides) > 2 * max(self.sides) else 3

a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())