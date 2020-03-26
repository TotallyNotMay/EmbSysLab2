from Function import Function
from random import random

class RandomSignal(Function):

    def __init__(self, n, w, pointsCount = 256):
        self.pointsList = []
        self.w = w
        self.n = n
        self.pointsCount = pointsCount
        
    def generete_signal(self):
        A = random()
        f = random()
        W = self.w / self.n
        resultNew = []
        
        for i in range(self.n):
            wNew = self.w - W * i
            result = Function(A, f, wNew, self.pointsCount)
            result = result.func_sin()
            for j in range(len(result)):
                if len(resultNew) == j:
                    resultNew.append(result[j])
                else :
                    resultNew[j][1] += result[j][1]

        self.pointsList = resultNew
        return resultNew




