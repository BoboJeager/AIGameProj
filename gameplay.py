import random
import numpy as np
from greenNode import greenNode
from blueNode import BlueNode
from greyNode import GreyNode
import matplotlib.pyplot as plt
import matplotlib as mpl

class Gameplay:
    def __init__(self,size):
        self.size = size
        self.grid = {}
        self.poplist = []
        self.greylist= []
        self.bluePlayer = BlueNode()

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

                uncertainty = float("{:.1f}".format(random.uniform(-0.7, 0.7)))
                g = greenNode(voting, uncertainty, count)
                self.poplist.append(g)
                self.grid[g.id] = 0
                count += 1


            elif (i < 5):
                probcurve.append(2)
                prob = random.randrange(1, 6)
                if (prob <= 3):
                    voting = True
                else:
                    voting = False

                uncertainty = float("{:.1f}".format(random.uniform(-0.8, 0.6)))
                g = greenNode(voting, uncertainty, count)
                self.grid[g.id] = 0
                self.poplist.append(g)
                count += 1
            elif (i < 7):
                probcurve.append(3)
                prob = random.randrange(1, 11)
                if (prob <= 7):
                    voting = True
                else:
                    voting = False

                uncertainty = float("{:.1f}".format(random.uniform(-0.9, 0.4)))
                g = greenNode(voting, uncertainty, count)
                self.grid[g.id] = 0
                self.poplist.append(g)
                count += 1
            elif (i < 9):
                probcurve.append(4)
                prob = random.randrange(1, 11)
                if (prob <= 8):
                    voting = True
                else:
                    voting = False

                uncertainty = float("{:.1f}".format(random.uniform(-1, 0.2)))
                g = greenNode(voting, uncertainty, count)
                self.grid[g.id] = 0
                self.poplist.append(g)
                count += 1
            elif (i < 30):
                probcurve.append(5)
                prob = random.randrange(1, 11)
                if (prob <= 9):
                    voting = True
                else:
                    voting = False

                uncertainty = float("{:.1f}".format(random.uniform(-1, 0)))
                g = greenNode(voting, uncertainty, count)
                self.grid[g.id] = 0
                self.poplist.append(g)
                count += 1

            else:
                probcurve.append(6)
                voting = True
                uncertainty = -1.0
                g = greenNode(voting, uncertainty, count)
                self.poplist.append(g)
                self.grid[g.id] = 0
                count += 1

    def interactionPhase(self):
        print('Everyone is talking...')
        for key in self.grid.keys():
            iagent = random.randrange(0, len(self.poplist))
            # print(self.poplist[key].uncertainty,self.poplist[key].id)
            self.grid[key] = self.poplist[iagent]
            self.poplist[key].interact(self.grid[key])
            # print(self.poplist[key].uncertainty, self.poplist[key].id)

        # for key, value in self.grid.items():
        #     key.interact(value)

        print('Interaction is over...')

    def currentBias(self):
        votingcount = 0
        notvotingcount = 0
        uncertaintyavgVoting = 0
        uncertaintyavgNotVoting = 0
        for agent in self.poplist:
            if(agent.voting):
                votingcount += 1
                uncertaintyavgVoting += agent.uncertainty
            else:
                notvotingcount += 1
                uncertaintyavgNotVoting += agent.uncertainty

        currvotingpercentage = (votingcount/len(self.poplist)) * 100
        uncertaintyavgVoting /= votingcount
        uncertaintyavgNotVoting /= notvotingcount
        print('people voting =',"{:.1f}".format(currvotingpercentage))
        print('the uncertainty average of people voting =', "{:.1f}".format(uncertaintyavgVoting))
        print('the uncertainty average of people NOT voting =', "{:.1f}".format(uncertaintyavgNotVoting))


    def blueTeamTurn(self):
        print("current energy = ", self.bluePlayer.energy)
        print("press 1 to broadcast message")
        print("press 2 to deploy a grey agent\n")
        choice = input()
        try:
            choice = int(choice)
            if(choice == 1):
                for t in self.bluePlayer.messagesString:
                    print(t[0])
            option = input("\nwhich message to broadcast?\n")
            option = int(option)
            self.bluePlayer.broadcastMessage(self.poplist,option)
            print(self.bluePlayer.energy)
        except ValueError:
            print('number must be an int')




    def result(self):
        print('You are all winners')