import random
import numpy as np
from greenNode import greenNode
from blueNode import BlueNode
from redNode import RedNode
from Ai import ai
from greyNode import GreyNode
import matplotlib.pyplot as plt
import matplotlib as mpl
import networkx as nx
import plotly.graph_objects as go
import copy


class Gameplay:

    def __init__(self, size, maxUncertainty, minUncertainty, blueRealPlayer, redRealPlayer):
        self.size = size
        self.grid = {}
        self.poplist = []
        self.maxUncertainty = maxUncertainty
        self.minUncertainty = minUncertainty
        self.bluePlayer = BlueNode()
        self.redPlayer = RedNode()
        self.blueRealPlayer = blueRealPlayer
        self.redRealPlayer = redRealPlayer
        self.aiplayers = ai()

    def setup(self):
        # Press Ctrl+F8 to toggle the breakpoint.
        dataDist = np.random.pareto(1, self.size) + 1
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

                uncertainty = float("{:.1f}".format(
                    random.uniform(-self.minUncertainty, self.maxUncertainty)))
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

                uncertainty = float("{:.1f}".format(
                    random.uniform(-self.minUncertainty, self.maxUncertainty - 0.1)))
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

                uncertainty = float("{:.1f}".format(
                    random.uniform(-self.minUncertainty, self.maxUncertainty - 0.2)))
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

                uncertainty = float("{:.1f}".format(
                    random.uniform(-self.minUncertainty, self.maxUncertainty - 0.3)))
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

                uncertainty = float("{:.1f}".format(
                    random.uniform(-self.minUncertainty, 0)))
                g = greenNode(voting, uncertainty, count)
                self.grid[g.id] = 0
                self.poplist.append(g)
                count += 1

            else:
                probcurve.append(6)
                voting = True
                uncertainty = -self.minUncertainty
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
            if (agent.voting):
                votingcount += 1
                uncertaintyavgVoting += agent.uncertainty
            else:
                notvotingcount += 1
                uncertaintyavgNotVoting += agent.uncertainty

        currvotingpercentage = (votingcount/len(self.poplist)) * 100
        uncertaintyavgVoting /= votingcount
        uncertaintyavgNotVoting /= notvotingcount
        print('people voting =', "{:.1f}".format(currvotingpercentage))
        print('the uncertainty average of people voting =',
              "{:.1f}".format(uncertaintyavgVoting))
        print('the uncertainty average of people NOT voting =',
              "{:.1f}".format(uncertaintyavgNotVoting))
        return_list = []
        return_list.append(currvotingpercentage)
        return_list.append(uncertaintyavgVoting)
        return_list.append(uncertaintyavgNotVoting)
        return return_list

    def blueTeamTurn(self):
        if (self.blueRealPlayer):
            print("current energy = ", self.bluePlayer.energy)
            print("Grey Agents at your disposal = ",
                  self.bluePlayer.greyAgentsAvailable)
            print("press 1 to broadcast message")
            print("press 2 to deploy a grey agent\n")
            choice = input()
            try:
                choice = int(choice)
                if (choice == 1):
                    for t in self.bluePlayer.messagesString:
                        print(t[0])
                    option = input("\nwhich message to broadcast?\n")
                    option = int(option)
                    self.bluePlayer.broadcastMessage(self.poplist, option)
                    print(self.bluePlayer.energy)
                else:
                    if (self.bluePlayer.greyAgentsAvailable > 0):
                        self.bluePlayer.deployGreyAgent(
                            self.poplist, self.grid)
                    else:
                        print("No agents available choose a message to broadcast")
                        for t in self.bluePlayer.messagesString:
                            print(t[0])
                        option = input("\nwhich message to broadcast?\n")
                        option = int(option)
                        self.bluePlayer.broadcastMessage(self.poplist, option)
                        print(self.bluePlayer.energy)

            except ValueError:
                print('number must be an int')
        else:
            self.aiplayers.blueAIagent(
                self.poplist, self.grid)

    def redTeamTurn(self):
        if self.redRealPlayer:
            for t in self.redPlayer.messagesString:
                print(t[0])
            option = input("\nwhich message to broadcast?\n")
            option = int(option)
            self.redPlayer.broadcast(self.poplist, option)
        else:
            self.aiplayers.redAIagent(self.poplist)

    def result(self):
        print('You are all winners')

   # Displays network with colors representing voting
    def displayWindows(self):
        Graph = nx.Graph()
        color_map = []
        # Add in edges
        for key in self.grid.keys():
            iagent = random.randrange(0, len(self.poplist))
            # print(self.poplist[key].uncertainty,self.poplist[key].id)
            self.grid[key] = self.poplist[iagent]
            Graph.add_edges_from([(self.poplist[key].id, self.grid[key].id)])
            # Make color of node blue if voting or red otherwise
            if self.poplist[key].voting:
                color_map.append('blue')
            else:
                color_map.append('red')
        nx.draw(Graph, node_color=color_map, with_labels=True)
        BlueFavour = 100 * (self.aiplayers.votingPercentage(self.poplist))
        RedFavour = 100 - BlueFavour
        fig1, ax1 = plt.subplots()
        chartLabels = 'Voting', 'Not Voting'
        sizes = [BlueFavour, RedFavour]
        chartColors = ["blue", "red"]
        ax1.pie(sizes, labels=chartLabels,  autopct='%1.1f%%',
                shadow=True, colors=chartColors)
        # plt.pie(votingArray, labels=chartLabels, colors=chartColors)
        ax1.axis('equal')
        fig = plt.gcf()
        fig.set_size_inches(6, 6)
        plt.show()

    def getVoting(self):
        percentage = 100 * (self.aiplayers.votingPercentage(self.poplist))
        return percentage
