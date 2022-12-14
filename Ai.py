import random
from redNode import RedNode
from blueNode import BlueNode


class ai:
    def __init__(self, noofgreyagents):
        self.redAI = RedNode()
        self.blueAI = BlueNode(noofgreyagents)
        self.redAILearningGraph = []
        self.turn = 0
        self.redFirstFiveMoves = []
        self.initialState = None

    def blueAIagent(self, populationList, grid):
        moveScores = []
        blueEnergy = {0: 5, 1: 5, 2: 10, 3: 10,
                      4: 15, 5: 15, 6: 20, 7: 20, 8: 30, 9: 30}
        for i in range(10):
            boardcopy = populationList.copy()
            if (i < 9):
                if self.blueAI.energy >= blueEnergy[i]:
                    self.blueAI.simulatebroadcastMessage(boardcopy, i + 1)
                    score = self.blueminimax(boardcopy, 3, False)
                    moveScores.append(score)
                else:
                    moveScores.append(-10000000000000)
            else:
                if self.blueAI.greyAgentsAvailable > 0:
                    self.blueAI.deploySimulatedGreyAgent(boardcopy)
                    score = self.blueminimax(boardcopy, 3, False)
                    moveScores.append(score)
                else:
                    moveScores.append(-10000000000000)
        bestNumber = max(moveScores)
        bestMove = moveScores.index(bestNumber)
        # print("Move scores = ", moveScores)
        # print("The best move is = ", bestMove)
        if (bestMove < 9):
            self.blueAI.broadcastMessage(populationList, bestMove + 1)
            # self.blueAI.setenergy(blueEnergy[bestMove])
        else:
            self.blueAI.deployGreyAgent(populationList, grid)

    def blueminimax(self, populationList, depth, aiturn):
        if depth <= 0 or abs(self.blueHeuristic(populationList)) > 10000:
            return self.blueHeuristic(populationList)

        if (aiturn):
            # go through each column
            currentMaxScore = -100000000
            newState = populationList.copy()
            for i in range(11):
                if (i < 9):
                    self.blueAI.simulatebroadcastMessage(newState, i + 1)
                else:
                    self.blueAI.deploySimulatedGreyAgent(newState)

                currentMaxScore = max(
                    currentMaxScore, self.blueminimax(newState, depth - 1, False))

            return currentMaxScore
        else:
            currentMinScore = 1000000000
            newState = populationList.copy()
            for i in range(10):
                self.redAI.simulatedbroadcast(newState, i + 1)
                currentMinScore = min(
                    currentMinScore, self.blueminimax(newState, depth - 1, True))
            return currentMinScore

    # Iteration number 4 now

    def blueHeuristic(self, populationlist):
        # Score to be returned
        score = 0
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
        # print("voting count = ",votingcount)
        # print("uncertaintyavgVoting = ",uncertaintyavgVoting)
        currvotingpercentage = (votingcount / len(populationlist))
        if votingcount == 0:
            score -= 10000000
        else:
            uncertaintyavgVoting /= votingcount
        if notvotingcount == 0:
            score += 10000000

        if uncertaintyavgVoting < 0:
            if ((uncertaintyavgVoting < -0.9) and (uncertaintyavgVoting >= -1)):
                score += weight[10]
            elif ((uncertaintyavgVoting < -0.8) and (uncertaintyavgVoting >= -0.9)):
                score += weight[9]
            elif ((uncertaintyavgVoting < -0.7) and (uncertaintyavgVoting >= -0.8)):
                score += weight[8]
            elif ((uncertaintyavgVoting < -0.6) and (uncertaintyavgVoting >= -0.7)):
                score += weight[7]
            elif ((uncertaintyavgVoting < -0.5) and (uncertaintyavgVoting >= -0.6)):
                score += weight[6]
            elif ((uncertaintyavgVoting < -0.4) and (uncertaintyavgVoting >= -0.5)):
                score += weight[5]
            elif ((uncertaintyavgVoting < -0.3) and (uncertaintyavgVoting >= -0.4)):
                score += weight[4]
            elif ((uncertaintyavgVoting < -0.2) and (uncertaintyavgVoting >= -0.3)):
                score += weight[3]
            elif ((uncertaintyavgVoting < -0.1) and (uncertaintyavgVoting >= -0.2)):
                score += weight[2]
            elif ((uncertaintyavgVoting < 0) and (uncertaintyavgVoting >= -0.1)):
                score += weight[1]
        elif uncertaintyavgVoting > 0:
            if ((uncertaintyavgVoting > 0) and (uncertaintyavgVoting <= 0.1)):
                score -= weight[1]
            elif ((uncertaintyavgVoting > 0.1) and (uncertaintyavgVoting <= 0.2)):
                score -= weight[2]
            elif ((uncertaintyavgVoting > 0.2) and (uncertaintyavgVoting <= 0.3)):
                score -= weight[3]
            elif ((uncertaintyavgVoting > 0.3) and (uncertaintyavgVoting <= 0.4)):
                score -= weight[4]
            elif ((uncertaintyavgVoting > 0.4) and (uncertaintyavgVoting <= 0.5)):
                score -= weight[5]
            elif ((uncertaintyavgVoting > 0.5) and (uncertaintyavgVoting <= 0.6)):
                score -= weight[6]
            elif ((uncertaintyavgVoting > 0.6) and (uncertaintyavgVoting <= 0.7)):
                score -= weight[7]
            elif ((uncertaintyavgVoting > 0.7) and (uncertaintyavgVoting <= 0.8)):
                score -= weight[8]
            elif ((uncertaintyavgVoting > 0.8) and (uncertaintyavgVoting <= 0.9)):
                score -= weight[9]
            elif ((uncertaintyavgVoting > 0.9) and (uncertaintyavgVoting <= 1)):
                score -= weight[10]

        score *= currvotingpercentage

        # print("Current voting percentage ", currvotingpercentage)
        # print("UncertaintyAvgVoting ", uncertaintyavgVoting)
        # print("UncertaintyAvgNotVoting ", uncertaintyavgNotVoting)
        # print(int(score))
        return int(score)

    # red AI functions

    def redAIagent(self, populationList):
        moveScores = []
        bestNextFiveMoves = []
        if (self.turn == 0):
            self.initialState = populationList.copy()
            bestNextFiveMoves = self.reccomendedMoveSet(populationList)
        if self.turn < 9:
            if not bestNextFiveMoves == None and len(bestNextFiveMoves) > 0:
                self.redAI.broadcast(
                    populationList, bestNextFiveMoves[self.turn] + 1)
            else:
                for i in range(10):
                    boardcopy = populationList.copy()
                    self.redAI.simulatedbroadcast(boardcopy, i + 1)
                    score = self.redminimax(boardcopy, 3, False)
                    moveScores.append(score)
                bestNumber = max(moveScores)
                bestMove = moveScores.index(bestNumber)
                # print("Move scores = ", moveScores)
                # print("The best move is = ", bestMove)
                self.redAI.broadcast(populationList, bestMove + 1)
                self.redFirstFiveMoves.append(bestMove)

        else:
            for i in range(10):
                boardcopy = populationList.copy()
                self.redAI.simulatedbroadcast(boardcopy, i + 1)
                score = self.redminimax(boardcopy, 3, False)
                moveScores.append(score)
            bestNumber = max(moveScores)
            bestMove = moveScores.index(bestNumber)
            # print("Move scores = ", moveScores)
            # print("The best move is = ", bestMove)
            self.redAI.broadcast(populationList, bestMove + 1)

    def redminimax(self, populationList, depth, aiturn):
        if depth <= 0 or abs(self.redHeuristic(populationList)) > 10000:
            return self.redHeuristic(populationList)

        if (aiturn):
            # go through each column
            currentMaxScore = -100000000
            newState = populationList.copy()
            for i in range(10):
                self.redAI.simulatedbroadcast(newState, i + 1)
                currentMaxScore = max(
                    currentMaxScore,
                    self.redminimax(newState, depth - 1, False))
            return currentMaxScore
        else:
            currentMinScore = 1000000000
            newState = populationList.copy()
            for i in range(11):
                if (i < 9):
                    self.blueAI.simulatebroadcastMessage(newState, i + 1)
                else:
                    self.blueAI.deploySimulatedGreyAgent(newState)
                currentMinScore = min(
                    currentMinScore,
                    self.redminimax(newState, depth - 1, True))
            return currentMinScore

    def redHeuristic(self, populationlist):
        # Score to be returned
        score = 0
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

        currentNotVotingPercentage = (notvotingcount / len(populationlist))
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

        # print("Current Not voting percentage ", currentNotVotingPercentage)
        # print("UncertaintyAvgVoting ", uncertaintyavgVoting)
        # print("UncertaintyAvgNotVoting ", uncertaintyavgNotVoting)
        # print(int(score))
        return int(score)

    def votingPercentage(self, populationlist):
        votingcount = 0
        for agent in populationlist:
            if (agent.voting):
                votingcount += 1
        currvotingpercentage = (votingcount / len(populationlist))
        return currvotingpercentage

    def calculateCurrentState(self, population):
        notvotingcount = 0
        uncertaintyavgNotVoting = 0
        for agent in population:
            if not (agent.voting):
                notvotingcount += 1
                uncertaintyavgNotVoting += agent.uncertainty
        votingPercentage = 100 - notvotingcount
        votingdifference = votingPercentage - notvotingcount
        if notvotingcount > 0:
            uncertaintyavgNotVoting /= notvotingcount
        else:
            uncertaintyavgNotVoting = -5
        return [votingdifference, uncertaintyavgNotVoting]

    def compareState(self, initalState, storedState):
        if (initalState[0] < storedState[0] + 2 or initalState[0] > storedState[0] - 2) and (
                initalState[1] + 0.2 or initalState[1] > storedState[1] - 0.2):
            return True
        else:
            return False

    def saveRedWinningState(self, initialpopulation, wonby, firstfivemove):
        initialstate = self.calculateCurrentState(initialpopulation)
        winState = [initialstate[0], initialstate[1], wonby, firstfivemove]
        self.redAILearningGraph.append(winState)

    def reccomendedMoveSet(self, population):
        winningpossibilities = []
        checkState = self.calculateCurrentState(population)
        if (len(self.redAILearningGraph) > 0):
            for i in self.redAILearningGraph:
                if self.compareState(checkState, i):
                    winningpossibilities.append(i)
            bestMoveSet = max(winningpossibilities,
                              key=lambda item: item[2])[3]
            # print("best Move set = ", bestMoveSet)
            return bestMoveSet
        else:
            return None
