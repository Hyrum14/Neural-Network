import random
import subprocess
import collections
import math

class Network:
    """
    Neural network
    """
    def __init__(self, layers=[]):
        self.points = [[[0, 0, [0 for n in range(layers[(icount + 1) % len(layers)])]] for j in range(i)] for (icount, i) in enumerate(layers)]

    def show(self, full=False):
        for i in self.points:
            for j in i:
                print(j[0], end=' '*(6 - len(str(j[0]))))
                if full:
                    print(str(j[1]), '- ', end='')
                    for n in j[2]:
                        print(n, end = ' '*(5 - len(str(n))))
                    print('')
            print('')

    def scramble(self):
        for i in self.points:
            for j in i:
                j[0] = round(random.uniform(0, 1), 2)
                j[1] = round(random.uniform(0, 1), 2)
                j[2] = [round(random.uniform(0, 1), 2) for _ in range(len(j[2]))]
        return self.points
    
    def calcButBetter(self):
        return [[[round(1 / (1 + math.e ** (-2 * math.e * sum(list(map(lambda a: a[1] * list(map(lambda a: round(a / sum(map(lambda b: b[2][jcount], self.points[icount - 1])), 2), 
        map(lambda c: c[2][jcount], self.points[icount - 1])))[a[0]], list(enumerate(list(map(lambda b: b[2][jcount], self.points[icount - 1]))))))) + math.e) + j[1]), 2) ,j[1] , j
        [2]] for (jcount, j) in list(enumerate(i))] for (icount, i) in list(enumerate(self.points))[1:]]

    def calc(self):
        for (icount, i) in list(enumerate(self.points))[1:]:
            for (jcount, j) in list(enumerate(i)):
                percentages = list(
                        map(
                            lambda a: round(a / sum(map(lambda b: b[2][jcount], self.points[icount - 1])), 2), 
                            map(
                                lambda c: c[2][jcount], 
                                self.points[icount - 1])))
                last = list(map(lambda b: b[2][jcount], self.points[icount - 1]))
                j[0] = round(1 / (1 + math.e ** (-2 * math.e * sum(list(map(lambda a: a[1] * percentages[a[0]], list(enumerate(last))))) + math.e) + j[1]), 2)
        return self.points

    def cost(self, correct=[]):
        ans = map(lambda a: a[0], self.calc(False)[-1])
        return self.points
    
    def save(self, name):
        saved = open('./NeuralNetwork/saved.txt', 'a')
        saved.write(name.lower())
        saved.write('|')
        saved.write(str(self.points))
        saved.write('\n')
    
    def load(self):
        saved = open('./NeuralNetwork/saved.txt', 'r')
        networks = saved.read().split('\n')
        names = list(map(lambda a: a[:a.index('|')], networks[:-1]))
        print(names)
        selected = names.index(input('Choose a list: ').lower())
        new = networks[selected][len(names[selected]) + 1:]
        exec('self.points = ' + new)


if __name__ == '__main__':
    a = Network([5, 2, 2, 4])
    a.save('joe')
    a.load()
    a.show()