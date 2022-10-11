import random;
import collections;
from greyNode import GreyNode;
from redNode import RedNode;


class BlueNode:

    def __init__(self):
        self.energy = 100
        self.messagesString = [("1. Vote Plox (broadcast power 1/Energy cost 5)",1),("2. Democracy good (broadcast power 1/Energy cost 5)",1),
                               ("3. just vote pls, do it (broadcast power 2/Energy cost 10)",2),("4. I beg you (broadcast power 2)/Energy cost 10)",2),
                               ("5. red no good (broadcast power 3)/Energy cost 15",3),("6. boo red fake news (broadcast power 3)/Energy cost 15)",3),
                               ("7. dont belif media pls (broadcast power 4/Energy cost 20)",4),("8. i swear we're better (broadcast power 4/Energy cost 20)",4),
                               ("9. free healthcare (broadcast power 5/Energy cost 30)",5),("10. for the ppl by the ppl (broadcast power 5/Energy cost 30)",5)]
        self.greyAgentsAvailable = 1
        self.redAi = RedNode()

    def setenergy(self, value):
        self.energy -= value

    def broadcastMessage(self,populationGrid,broadcastOption):
        broadcastOption -= 1
        option = self.messagesString[broadcastOption]
        print(option[0])
        if(option[1] == 1):
            print("broadcasted")
            self.setenergy(5)
            for gn in populationGrid:
                influence = random.randrange(1,6)
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

        elif(option[1] == 2):
            print("broadcasted")
            self.setenergy(10)
            print("broadcasted")
            self.setenergy(5)
            for gn in populationGrid:
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
        elif (option[1] == 3):
            print("broadcasted")
            self.setenergy(15)
            for gn in populationGrid:
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
        elif (option[1] == 4):
            print("broadcasted")
            self.setenergy(20)
            for gn in populationGrid:
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
            print("broadcasted")
            self.setenergy(30)
            for gn in populationGrid:
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




    def deployGreyAgent(self,poplist, grid):
        if (self.greyAgentsAvailable > 0):
            self.greyAgentsAvailable -= 1
            print("agent deployed")
            rnum = random.randrange(1,6)
            ally = True
            if(rnum  == 2):
                ally = False
            gAgent = GreyNode(len(poplist), ally)
            poplist.append(gAgent)
            grid[gAgent.id] = 0
        else:
            print("No more agents you used all")

    def deploySimulatedGreyAgent(self,poplist):
            print("agent deployed")
            rnum = random.randrange(1,6)
            ally = True
            if(rnum  == 2):
                ally = False
            gAgent = GreyNode(len(poplist), ally)
            poplist.append(gAgent)


    def blueAIagent(self, populationList, grid):
        moveScores = []
        for i in range(11):
            boardcopy = populationList.copy()
            if (i < 9):
                self.broadcastMessage(boardcopy, i)
                score = self.minimax(boardcopy,4,False)
                moveScores.append(score)
            else:
                self.deploySimulatedGreyAgent(boardcopy)
                score = self.minimax(boardcopy, 4, False)
                moveScores.append(score)
        bestNumber = max(moveScores)
        bestMove = moveScores.index(bestNumber)
        if(bestMove < 10):
            self.broadcastMessage(populationList,bestMove)
        else:
            self.deployGreyAgent(populationList,grid)




    def minimax(self, populationList , depth , aiturn):
        if depth <= 0 or abs(self.heuristic(populationList)) > 10000:
            return self.heuristic(populationList)

        if(aiturn):
            #go through each column
            currentMaxScore = -100000000
            newState = populationList.copy()
            for i in range(11):
                if(i < 9):
                    self.broadcastMessage(newState,i)
                else:
                    self.deploySimulatedGreyAgent(newState)
                currentMaxScore= max(currentMaxScore,self.minimax(newState,depth-1,False))

            return currentMaxScore
        else:
            currentMinScore = 1000000000
            newState = populationList.copy()
            for i in range(10):
                self.redAi.broadcast(newState,i)
                currentMinScore= min(currentMinScore,self.minimax(newState,depth-1,True))
            return  currentMinScore
