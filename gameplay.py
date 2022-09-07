import random
import numpy as np
from greenNode import greenNode
from greyNode import GreyNode
import matplotlib.pyplot as plt
import matplotlib as mpl

class Gameplay:
    def __init__(self,size):
        self.size = size
        self.grid = {}
        self.greenlist = []
        self.greylist= []

    def setup(self):
        dataDist = np.random.pareto(1, self.size) + 1  # Press Ctrl+F8 to toggle the breakpoint.
        voting = True
        count = 0
        probcurve = []
        uncertainty = 0.0
        for i in dataDist:
            if (i < 3):
                probcurve.append(1)
                prob = random.randrange(1, 3)
                if (prob == 1):
                    voting = True
                else:
                    voting = False

                uncertainty = "{:.1f}".format(random.uniform(-1, 1))
                g = greenNode(voting, uncertainty, count)
                self.greenlist.append(g)
                self.grid[g] = 0
                count += 1


            elif (i < 5):
                probcurve.append(2)
                prob = random.randrange(1, 6)
                if (prob <= 3):
                    voting = True
                else:
                    voting = False

                uncertainty = "{:.1f}".format(random.uniform(-1, 0.7))
                g = greenNode(voting, uncertainty, count)
                self.grid[g] = 0
                self.greenlist.append(g)
                count += 1
            elif (i < 7):
                probcurve.append(3)
                prob = random.randrange(1, 11)
                if (prob <= 7):
                    voting = True
                else:
                    voting = False

                uncertainty = "{:.1f}".format(random.uniform(-1, 0.4))
                g = greenNode(voting, uncertainty, count)
                self.grid[g] = 0
                self.greenlist.append(g)
                count += 1
            elif (i < 9):
                probcurve.append(4)
                prob = random.randrange(1, 11)
                if (prob <= 8):
                    voting = True
                else:
                    voting = False

                uncertainty = "{:.1f}".format(random.uniform(-1, 0.2))
                g = greenNode(voting, uncertainty, count)
                self.grid[g] = 0
                self.greenlist.append(g)
                count += 1
            elif (i < 30):
                probcurve.append(5)
                prob = random.randrange(1, 11)
                if (prob <= 9):
                    voting = True
                else:
                    voting = False

                uncertainty = "{:.1f}".format(random.uniform(-1, 0))
                g = greenNode(voting, uncertainty, count)
                self.grid[g] = 0
                self.greenlist.append(g)
                count += 1

            else:
                probcurve.append(6)
                voting = True
                uncertainty = -1.0
                g = greenNode(voting, uncertainty, count)
                self.greenlist.append(g)
                self.grid[g] = 0
                count += 1

        for key, value in self.grid.items():
            print(key.voting, key.uncertainty, key.id)

    def interactionPhase(self):
        print('node interaction happening')

    def result(self):
        print('You are all winners')