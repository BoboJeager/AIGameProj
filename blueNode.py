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
        self.greyAgentsAvailable = 1
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
            self.setenergy(10)
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
            if(rnum == 2):
                ally = False
            gAgent = GreyNode(len(poplist), ally)
            poplist.append(gAgent)
            grid[gAgent.id] = 0
        else:
            print("No more agents you used all")

    def deploySimulatedGreyAgent(self, poplist):
        print("agent deployed")
        rnum = random.randrange(1, 6)
        ally = True
        if(rnum == 2):
            ally = False
        gAgent = GreyNode(len(poplist), ally)
        poplist.append(gAgent)

    def blueAIagent(self, populationList, grid, startingMaxUncertainty):
        moveScores = []
        for i in range(11):
            boardcopy = populationList.copy()
            if (i < 9):
                self.broadcastMessage(boardcopy, i)
                score = self.minimax(boardcopy, 3, False,
                                     startingMaxUncertainty)
                moveScores.append(score)
            else:
                self.deploySimulatedGreyAgent(boardcopy)
                score = self.minimax(boardcopy, 3, False,
                                     startingMaxUncertainty)
                moveScores.append(score)
        bestNumber = max(moveScores)
        bestMove = moveScores.index(bestNumber)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", moveScores)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", bestMove)
        if(bestMove < 10):
            self.broadcastMessage(populationList, bestMove)
        else:
            self.deployGreyAgent(populationList, grid)

    def minimax(self, populationList, depth, aiturn, startingUncertainty):
        if depth <= 0 or abs(self.blueHeuristic(populationList, startingUncertainty)) > 10000:
            return self.blueHeuristic(populationList, startingUncertainty)

        if(aiturn):
            # go through each column
            currentMaxScore = -100000000
            newState = populationList.copy()
            for i in range(11):
                if(i < 9):
                    self.broadcastMessage(newState, i)
                else:
                    self.deploySimulatedGreyAgent(newState)
                currentMaxScore = max(
                    currentMaxScore, self.minimax(newState, depth-1, False, startingUncertainty))

            return currentMaxScore
        else:
            currentMinScore = 1000000000
            newState = populationList.copy()
            for i in range(10):
                self.redAi.broadcast(newState, i)
                currentMinScore = min(
                    currentMinScore, self.minimax(newState, depth-1, True, startingUncertainty))
            return currentMinScore

    def blueHeuristic(self, populationlist, startingMaxUncertainty):
        # Score to be returned
        score = 0
        # Associated weight to be added to the score
        weight = {1: 0, 2: 5, 3: 10, 4: 30, 5: 80,
                  6: 200, 7: 500, 8: 1000, 9: 20000, 10: 100000}
        # Calculations for voting uncertainties and averages
        votingcount = 0
        notvotingcount = 0
        uncertaintyavgVoting = 0
        uncertaintyavgNotVoting = 0
        for agent in populationlist:
            if(agent.voting):
                votingcount += 1
                uncertaintyavgVoting += agent.uncertainty
            else:
                notvotingcount += 1
                uncertaintyavgNotVoting += agent.uncertainty

        currvotingpercentage = (votingcount/len(populationlist)) * 100
        if votingcount == 0:
            score -= 1000000
        else:
            uncertaintyavgVoting /= votingcount
        if notvotingcount == 0:
            score += 1000000

        # Probably don't need these calculations, make sure to remove as parameters
        # CurrUncertaintyDiff = uncertaintyavgVoting - uncertaintyavgNotVoting
        # CurrUncertaintyDiff = abs(CurrUncertaintyDiff)
        # ChangedUncertaintyDiff = CurrUncertaintyDiff/UncertaintyDiff

        # Blue Bias so make higher for red and lower for blue
        if currvotingpercentage >= 75:
            # High voting percentage and very certain so add low score
            if uncertaintyavgVoting > (startingMaxUncertainty / 1.4):
                score -= weight[9]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 2):
                score -= weight[8]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 2.4):
                score -= weight[7]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 3):
                score -= weight[6]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 3.6):
                score += weight[4]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 4.3):
                score += weight[5]
            else:
                score += weight[1]

        elif currvotingpercentage >= 50 and currvotingpercentage < 75:

            # Still blue bias, so add medium-low score
            # High voting percentage and very certain so add low score
            if uncertaintyavgVoting > (startingMaxUncertainty / 1.4):
                score -= weight[7]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 2):
                score -= weight[6]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 2.4):
                score -= weight[3]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 3):
                score += weight[3]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 3.6):
                score += weight[4]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 4.3):
                score += weight[5]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 4.7):
                score += weight[6]
            else:
                score += weight[7]

        # Red bias so make higher for blue lower for red
        elif currvotingpercentage >= 25 and currvotingpercentage < 50:
            # Low voting percentage for blue, add higher scores
            if uncertaintyavgVoting > (startingMaxUncertainty / 1.4):
                score -= weight[4]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 2):
                score -= weight[3]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 2.4):
                score -= weight[2]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 3):
                score += weight[5]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 3.6):
                score += weight[6]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 4.3):
                score += weight[7]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 4.7):
                score += weight[8]
            else:
                score += weight[9]

        elif currvotingpercentage < 25 and currvotingpercentage > 10:
            # Very low voting percentage for blue, add very high scores
            if uncertaintyavgVoting > (startingMaxUncertainty / 1.4):
                score -= weight[3]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 2.4):
                score -= weight[2]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 3):
                score += weight[6]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 3.6):
                score += weight[7]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 4.3):
                score += weight[8]
            elif uncertaintyavgVoting > (startingMaxUncertainty / 4.7):
                score += weight[9]
            else:
                score += weight[10]

        elif currvotingpercentage <= 10:
            # Next to zero voting percentage in favour of blue, add the highest weight to score
            score += weight[10]

            # If no grey agents left, then make score very negative
        if self.greyAgentsAvailable == 0:
            score += -1000000
        print("Current voting percentage ", currvotingpercentage)
        print("UncertaintyAvgVoting ", uncertaintyavgVoting)

        return score
