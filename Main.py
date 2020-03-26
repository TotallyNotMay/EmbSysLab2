from RandomSignal import RandomSignal
from time import perf_counter
from FourierTransform import FourierTransform
import matplotlib.pyplot as plt


def Rxx(arr, t):
    list = [x[1] for x in arr]
    N = len(arr) / 2
    M = sum(list) / len(list)

    if t > N:
        print('t exceeds range')
        return 0
    else:
        Rxx = 0
        for j in range(int(N)):
            Rxx += (list[j] - M) * (list[j + t] - M) / (N - 1)

        return Rxx


def Rxy(arr1, arr2, t):
    list1 = [x[1] for x in arr1]
    list2 = [x[1] for x in arr2]

    N = len(arr1) / 2
    M1 = sum(list1) / len(list1)
    M2 = sum(list2) / len(list2)

    if t > N:
        print('t exceeds range')
        return 0
    else:
        Rxy = 0
        for j in range(int(N)):
            Rxy += (list1[j] - M1) * (list2[j + t] - M2) / (N - 1)

        return Rxy


class Main:
    n = 10
    w = 1500
    N = 256

    obj1 = RandomSignal(n, w, N)
    points1 = obj1.generete_signal()
    RxxList = []
    for tau in range(int(N / 2)):
        RxxList.append(Rxx(points1, tau))

    obj2 = RandomSignal(n, w, N)
    points2 = obj2.generete_signal()
    RxyList = []
    for tau in range(int(N / 2)):
        RxyList.append(Rxy(points1, points2, tau))

    signalValues = []
    for i in range(len(points1)):
        signalValues.append(points1[i][1])
    fourier = FourierTransform(signalValues)

    DFTList = fourier.DFT()
    print(DFTList)
    FFTList = fourier.FFT()
    print(FFTList)

    plt.plot([x for x in range(N)], DFTList, color='b')
    plt.plot([x for x in range(N)], FFTList, color='r')
    plt.show()
