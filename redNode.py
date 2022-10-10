import random;
import collections;

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
    def broadcast(self,populationGrid,broadcastOption):
        broadcastOption -= 1
        option = self.messagesString[broadcastOption]
        print(option[0])
        if option[1] == 1:
            print("broadcasted\n")
            for gn in populationGrid:
                influence = random.randrange(1, 6)
                if influence < 4:
                    if (not gn.voting):
                        if(not gn.uncertainty == -1):
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
                else:
                    gn.flipVote()

    def redAIagent(self):
        return 10;

    def minimax(self, populationList , depth , aiturn):
        if depth <= 0 or abs(self.analyse(populationList)) > 10000:
            return self.analyse(populationList)

        if(aiturn):
            #go through each column
            currentMaxScore = -100000000
            for i in range(len(populationList)):
                newState = populationList.copy()
                if(len(populationList[i]) < 10):
                    currentMaxScore= max(currentMaxScore,self.minimax(newState,depth-1,False,"O"))
                else:
                    continue

            return currentMaxScore
        else:
            currentMinScore = 1000000000
            for i in range(len(populationList)):
                newState = populationList.copy()
                if (len(populationList[i]) < 6):
                    currentMinScore= min(currentMinScore,self.minimax(newState,depth-1,True,"O"))
                else:
                    continue
            return  currentMinScore