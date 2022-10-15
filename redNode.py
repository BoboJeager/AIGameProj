import random
import collections


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

    # For player
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
                            gn.setUncertainty(-0.3)
                            if (gn.uncertainty < -1):
                                gn.uncertainty = -1
                    else:
                        gn.setUncertainty(0.3)
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
                            gn.setUncertainty(-0.4)
                            if (gn.uncertainty < -1):
                                gn.uncertainty = -1
                    else:
                        gn.setUncertainty(0.4)
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

    # Used For Ai
    def simulatedbroadcast(self, populationGrid, broadcastOption):
        broadcastOption -= 1
        option = self.messagesString[broadcastOption]
        if option[1] == 1:
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

        elif option[1] == 2:
            for gn in populationGrid:
                influence = random.randrange(1, 6)
                if influence < 4:
                    if (not gn.voting):
                        if (not gn.uncertainty == -1):
                            gn.setUncertainty(-0.4)
                            if (gn.uncertainty < -1):
                                gn.uncertainty = -1
                    else:
                        gn.setUncertainty(0.4)
                        if (gn.uncertainty > 1):
                            gn.flipVote()
                            x = 1 - gn.uncertainty
                            gn.uncertainty = 1 - x
        elif option[1] == 3:
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
            for gn in populationGrid:
                influence = random.randrange(1, 6)
                if influence < 4:
                    if (not gn.voting):
                        if (not gn.uncertainty == -1):
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
