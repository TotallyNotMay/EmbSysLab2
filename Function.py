from math import sin

class Function():

    def __init__(self, A, f, w, pointsCount = 64, accuracy = 0.1):
        self.A = A
        self.f = f
        self.w = w
        self.pointsCount = pointsCount
        self.accuracy = accuracy

    def func_sin(self):
        result = []
        for i in range(self.pointsCount):
            result.append([i * self.accuracy, self.A * sin(self.w * i * self.accuracy + self.f)])
        return result
