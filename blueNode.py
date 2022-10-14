import random
import collections
from unittest import case
from greyNode import GreyNode
from redNode import RedNode
from greenNode import greenNode


class BlueNode:

    def __init__(self):
        self.energy = 100
        self.messagesString = [("1. Vote Plox (broadcast power 1/Energy cost 5)", 1), ("2. Democracy good (broadcast power 1/Energy cost 5)", 1),
                               ("3. just vote pls, do it (broadcast power 2/Energy cost 10)",
                                2), ("4. I beg you (broadcast power 2)/Energy cost 10)", 2),
                               ("5. red no good (broadcast power 3)/Energy cost 15",
                                3), ("6. boo red fake news (broadcast power 3)/Energy cost 15)", 3),
                               ("7. dont belif media pls (broadcast power 4/Energy cost 20)",
                                4), ("8. i swear we're better (broadcast power 4/Energy cost 20)", 4),
                               ("9. free healthcare (broadcast power 5/Energy cost 30)", 5), ("10. for the ppl by the ppl (broadcast power 5/Energy cost 30)", 5)]
        self.greyAgentsAvailable = 0
        self.redAi = RedNode()

    def setenergy(self, value):
        self.energy -= value

    def broadcastMessage(self, populationGrid, broadcastOption):
        broadcastOption -= 1
        option = self.messagesString[broadcastOption]
        print(option[0])
        if(option[1] == 1):
            print("broadcasted")
            self.setenergy(5)
            for gn in populationGrid:
                if isinstance(gn, greenNode):
                    influence = random.randrange(1, 6)
                    if influence < 4:
                        if(gn.voting):
                            gn.setUncertainty(-0.1)
                            if(gn.uncertainty < -1):
                                gn.uncertainty = -1
                        else:
                            gn.setUncertainty(0.1)
                            if(gn.uncertainty > 1):
                                gn.flipVote()
                                x = 1 - gn.uncertainty
                                gn.uncertainty = 1 - x
                else:
                    continue

        elif(option[1] == 2):
            print("broadcasted")
            self.setenergy(5)
            for gn in populationGrid:
                if isinstance(gn, greenNode):
                    influence = random.randrange(1, 6)
                    if influence < 4:
                        if (gn.voting):
                            gn.setUncertainty(-0.2)
                            if (gn.uncertainty < -1):
                                gn.uncertainty = -1
                        else:
                            gn.setUncertainty(0.2)
                            if (gn.uncertainty > 1):
                                gn.flipVote()
                                x = 1 - gn.uncertainty
                                gn.uncertainty = 1 - x
                else:
                    continue

        elif (option[1] == 3):
            print("broadcasted")
            self.setenergy(15)
            for gn in populationGrid:
                if isinstance(gn, greenNode):
                    influence = random.randrange(1, 6)
                    if influence < 4:
                        if (gn.voting):
                            gn.setUncertainty(-0.4)
                            if (gn.uncertainty < -1):
                                gn.uncertainty = -1
                        else:
                            gn.setUncertainty(0.4)
                            if (gn.uncertainty > 1):
                                gn.flipVote()
                                x = 1 - gn.uncertainty
                                gn.uncertainty = 1 - x
                else:
                    continue
        elif (option[1] == 4):
            print("broadcasted")
            self.setenergy(20)
            for gn in populationGrid:
                if isinstance(gn, greenNode):
                    influence = random.randrange(1, 6)
                    if influence < 4:
                        if (gn.voting):
                            gn.setUncertainty(-0.5)
                            if (gn.uncertainty < -1):
                                gn.uncertainty = -1
                        else:
                            gn.setUncertainty(0.5)
                            if (gn.uncertainty > 1):
                                gn.flipVote()
                                x = 1 - gn.uncertainty
                                gn.uncertainty = 1 - x
                else:
                    continue
        else:
            print("broadcasted")
            self.setenergy(30)
            for gn in populationGrid:
                if isinstance(gn, greenNode):
                    influence = random.randrange(1, 6)
                    if influence < 4:
                        if (gn.voting):
                            gn.setUncertainty(-0.7)
                            if (gn.uncertainty < -1):
                                gn.uncertainty = -1
                        else:
                            gn.setUncertainty(0.7)
                            if (gn.uncertainty > 1):
                                gn.flipVote()
                                x = 1 - gn.uncertainty
                                gn.uncertainty = 1 - x
                else:
                    continue

    def deployGreyAgent(self, poplist, grid):
        if (self.greyAgentsAvailable > 0):
            self.greyAgentsAvailable -= 1
            print("agent deployed")
            rnum = random.randrange(1, 6)
            ally = True
            if (rnum == 2):
                ally = False
            gAgent = GreyNode(len(poplist), ally)
            poplist.append(gAgent)
            grid[gAgent.id] = 0
        else:
            print("No more agents you used all")

    def deploySimulatedGreyAgent(self, poplist):
        rnum = random.randrange(1, 6)
        ally = True
        if (rnum == 2):
            ally = False
        gAgent = GreyNode(len(poplist), ally)
        poplist.append(gAgent)

    def simulatebroadcastMessage(self, populationGrid, broadcastOption):
        broadcastOption -= 1
        option = self.messagesString[broadcastOption]
        if(option[1] == 1):
            for gn in populationGrid:
                if isinstance(gn, greenNode):
                    influence = random.randrange(1, 6)
                    if influence < 4:
                        if(gn.voting):
                            gn.setUncertainty(-0.1)
                            if(gn.uncertainty < -1):
                                gn.uncertainty = -1
                        else:
                            gn.setUncertainty(0.1)
                            if(gn.uncertainty > 1):
                                gn.flipVote()
                                x = 1 - gn.uncertainty
                                gn.uncertainty = 1 - x
                else:
                    continue

        elif(option[1] == 2):
            for gn in populationGrid:
                if isinstance(gn, greenNode):
                    influence = random.randrange(1, 6)
                    if influence < 4:
                        if (gn.voting):
                            gn.setUncertainty(-0.2)
                            if (gn.uncertainty < -1):
                                gn.uncertainty = -1
                        else:
                            gn.setUncertainty(0.2)
                            if (gn.uncertainty > 1):
                                gn.flipVote()
                                x = 1 - gn.uncertainty
                                gn.uncertainty = 1 - x
                else:
                    continue

        elif (option[1] == 3):
            for gn in populationGrid:
                if isinstance(gn, greenNode):
                    influence = random.randrange(1, 6)
                    if influence < 4:
                        if (gn.voting):
                            gn.setUncertainty(-0.4)
                            if (gn.uncertainty < -1):
                                gn.uncertainty = -1
                        else:
                            gn.setUncertainty(0.4)
                            if (gn.uncertainty > 1):
                                gn.flipVote()
                                x = 1 - gn.uncertainty
                                gn.uncertainty = 1 - x
                else:
                    continue
        elif (option[1] == 4):
            for gn in populationGrid:
                if isinstance(gn, greenNode):
                    influence = random.randrange(1, 6)
                    if influence < 4:
                        if (gn.voting):
                            gn.setUncertainty(-0.5)
                            if (gn.uncertainty < -1):
                                gn.uncertainty = -1
                        else:
                            gn.setUncertainty(0.5)
                            if (gn.uncertainty > 1):
                                gn.flipVote()
                                x = 1 - gn.uncertainty
                                gn.uncertainty = 1 - x
                else:
                    continue
        else:
            for gn in populationGrid:
                if isinstance(gn, greenNode):
                    influence = random.randrange(1, 6)
                    if influence < 4:
                        if (gn.voting):
                            gn.setUncertainty(-0.7)
                            if (gn.uncertainty < -1):
                                gn.uncertainty = -1
                        else:
                            gn.setUncertainty(0.7)
                            if (gn.uncertainty > 1):
                                gn.flipVote()
                                x = 1 - gn.uncertainty
                                gn.uncertainty = 1 - x
                else:
                    continue
