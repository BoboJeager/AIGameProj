import random
import collections
from blueNode import BlueNode


class RedNode:

    def __init__(self):
        self.messagesString = [("1. Vote Plox (broadcast power 1/Energy cost 5)", 1),
                               ("2. Democracy good (broadcast power 1/Energy cost 5)", 1),
                               ("3. just vote pls, do it (broadcast power 2/Energy cost 10)", 2),
                               ("4. I beg you (broadcast power 2)/Energy cost 10)", 2),
                               ("5. red no good (broadcast power 3)/Energy cost 15", 3),
                               ("6. boo red fake news (broadcast power 3)/Energy cost 15)", 3),
                               ("7. dont belif media pls (broadcast power 4/Energy cost 20)", 4),
                               ("8. i swear we're better (broadcast power 4/Energy cost 20)", 4),
                               ("9. free healthcare (broadcast power 5/Energy cost 30)", 5),
                               ("10. for the ppl by the ppl (broadcast power 5/Energy cost 30)", 5)]
        self.blueAi = BlueNode()

    def broadcast(self, populationGrid, broadcastOption):
        broadcastOption -= 1
        option = self.messagesString[broadcastOption]
        print(option[0])
        if option[1] == 1:
            print("broadcasted\n")
            for gn in populationGrid:
                influence = random.randrange(1, 6)
                if influence < 4:
                    if (not gn.voting):
                        if (not gn.uncertainty == -1):
                            gn.setUncertainty(-0.2)
                            if (gn.uncertainty < -1):
                                gn.uncertainty = -1
                    else:
                        gn.setUncertainty(0.2)
                        if (gn.uncertainty > 1):
                            gn.flipVote()
                            x = 1 - gn.uncertainty
                            gn.uncertainty = 1 - x

        elif option[1] == 2:
            print("broadcasted\n")
            for gn in populationGrid:
                influence = random.randrange(1, 6)
                if influence < 4:
                    if (not gn.voting):
                        if (not gn.uncertainty == -1):
                            gn.setUncertainty(-0.3)
                            if (gn.uncertainty < -1):
                                gn.uncertainty = -1
                    else:
                        gn.setUncertainty(0.3)
                        if (gn.uncertainty > 1):
                            gn.flipVote()
                            x = 1 - gn.uncertainty
                            gn.uncertainty = 1 - x
        elif option[1] == 3:
            print("broadcasted\n")
            for gn in populationGrid:
                influence = random.randrange(1, 6)
                if influence < 4:
                    if (not gn.voting):
                        if (not gn.uncertainty == -1):
                            gn.setUncertainty(-0.5)
                            if (gn.uncertainty < -1):
                                gn.uncertainty = -1
                    else:
                        gn.setUncertainty(0.5)
                        if (gn.uncertainty > 1):
                            gn.flipVote()
                            x = 1 - gn.uncertainty
                            gn.uncertainty = 1 - x
        elif option[1] == 4:
            print("broadcasted\n")
            for gn in populationGrid:
                influence = random.randrange(1, 6)
                if influence < 4:
                    if (not gn.voting):
                        if (not gn.uncertainty == -1):
                            gn.setUncertainty(-0.6)
                            if (gn.uncertainty < -1):
                                gn.uncertainty = -1
                    else:
                        gn.setUncertainty(0.6)
                        if (gn.uncertainty > 1):
                            gn.flipVote()
                            x = 1 - gn.uncertainty
                            gn.uncertainty = 1 - x
        else:
            print("broadcasted\n")
            for gn in populationGrid:
                influence = random.randrange(1, 6)
                if influence < 4:
                    if (not gn.voting):
                        if (not gn.uncertainty == -1):
                            gn.setUncertainty(-0.8)
                            if (gn.uncertainty < -1):
                                gn.uncertainty = -1
                    else:
                        gn.setUncertainty(0.8)
                        if (gn.uncertainty > 1):
                            gn.flipVote()
                            x = 1 - gn.uncertainty
                            gn.uncertainty = 1 - x
                else:
                    gn.flipVote()

    def redAIagent(self, populationList):
        moveScores = []
        for i in range(10):
            boardcopy = populationList.copy()
            self.broadcast(boardcopy, i+1)
            score = self.minimax(boardcopy, 3, False)
            moveScores.append(score)
        bestNumber = max(moveScores)
        bestMove = moveScores.index(bestNumber)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", moveScores)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", bestMove)
        self.broadcast(populationList, bestMove + 1)

    def minimax(self, populationList, depth, aiturn):
        if depth <= 0 or abs(self.redHeuristic(populationList)) > 10000:
            return self.redHeuristic(populationList)

        if (aiturn):
            # go through each column
            currentMaxScore = -100000000
            newState = populationList.copy()
            for i in range(10):
                self.broadcast(newState, i + 1)
                currentMaxScore = max(
                    currentMaxScore,
                    self.minimax(newState, depth - 1, False))
            return currentMaxScore
        else:
            currentMinScore = 1000000000
            newState = populationList.copy()
            for i in range(11):
                if (i < 9):
                    self.blueAi.broadcastMessage(newState, i + 1)
                else:
                    self.blueAi.deploySimulatedGreyAgent(newState)
                currentMinScore = min(
                    currentMinScore,
                    self.minimax(newState, depth - 1, True))
            return currentMinScore

    def redHeuristic(self, populationlist):
        # Score to be returned
        score = 0
        scoreBlue = 0
        scoreRed = 0
        # Associated weight to be added to the score
        weight = {1: 1, 2: 5, 3: 10, 4: 30, 5: 80,
                  6: 200, 7: 500, 8: 1000, 9: 20000, 10: 100000}
        # Calculations for voting uncertainties and averages
        votingcount = 0
        notvotingcount = 0
        uncertaintyavgVoting = 0
        uncertaintyavgNotVoting = 0
        for agent in populationlist:
            if (agent.voting):
                votingcount += 1
                uncertaintyavgVoting += agent.uncertainty
            else:
                notvotingcount += 1
                uncertaintyavgNotVoting += agent.uncertainty

        currentNotVotingPercentage = (notvotingcount/len(populationlist))
        if notvotingcount == 0:
            score -= 10000000
        else:
            uncertaintyavgNotVoting /= notvotingcount
        if votingcount == 0:
            score += 10000000

        if uncertaintyavgNotVoting < 0:
            if ((uncertaintyavgNotVoting < -0.9) and (uncertaintyavgNotVoting >= -1)):
                score += weight[10]
            elif ((uncertaintyavgNotVoting < -0.8) and (uncertaintyavgNotVoting >= -0.9)):
                score += weight[9]
            elif ((uncertaintyavgNotVoting < -0.7) and (uncertaintyavgNotVoting >= -0.8)):
                score += weight[8]
            elif ((uncertaintyavgNotVoting < -0.6) and (uncertaintyavgNotVoting >= -0.7)):
                score += weight[7]
            elif ((uncertaintyavgNotVoting < -0.5) and (uncertaintyavgNotVoting >= -0.6)):
                score += weight[6]
            elif ((uncertaintyavgNotVoting < -0.4) and (uncertaintyavgNotVoting >= -0.5)):
                score += weight[5]
            elif ((uncertaintyavgNotVoting < -0.3) and (uncertaintyavgNotVoting >= -0.4)):
                score += weight[4]
            elif ((uncertaintyavgNotVoting < -0.2) and (uncertaintyavgNotVoting >= -0.3)):
                score += weight[3]
            elif ((uncertaintyavgNotVoting < -0.1) and (uncertaintyavgNotVoting >= -0.2)):
                score += weight[2]
            elif ((uncertaintyavgNotVoting < 0) and (uncertaintyavgNotVoting >= -0.1)):
                score += weight[1]
        elif uncertaintyavgNotVoting > 0:
            if ((uncertaintyavgNotVoting > 0) and (uncertaintyavgNotVoting <= 0.1)):
                score -= weight[1]
            elif ((uncertaintyavgNotVoting > 0.1) and (uncertaintyavgNotVoting <= 0.2)):
                score -= weight[2]
            elif ((uncertaintyavgNotVoting > 0.2) and (uncertaintyavgNotVoting <= 0.3)):
                score -= weight[3]
            elif ((uncertaintyavgNotVoting > 0.3) and (uncertaintyavgNotVoting <= 0.4)):
                score -= weight[4]
            elif ((uncertaintyavgNotVoting > 0.4) and (uncertaintyavgNotVoting <= 0.5)):
                score -= weight[5]
            elif ((uncertaintyavgNotVoting > 0.5) and (uncertaintyavgNotVoting <= 0.6)):
                score -= weight[6]
            elif ((uncertaintyavgNotVoting > 0.6) and (uncertaintyavgNotVoting <= 0.7)):
                score -= weight[7]
            elif ((uncertaintyavgNotVoting > 0.7) and (uncertaintyavgNotVoting <= 0.8)):
                score -= weight[8]
            elif ((uncertaintyavgNotVoting > 0.8) and (uncertaintyavgNotVoting <= 0.9)):
                score -= weight[9]
            elif ((uncertaintyavgNotVoting > 0.9) and (uncertaintyavgNotVoting <= 1)):
                score -= weight[10]

        score *= currentNotVotingPercentage

        print("Current Not voting percentage ", currentNotVotingPercentage)
        print("UncertaintyAvgVoting ", uncertaintyavgVoting)
        print("UncertaintyAvgNotVoting ", uncertaintyavgNotVoting)
        print(int(score))
        return int(score)
