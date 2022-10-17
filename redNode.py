import random
import collections


class RedNode:

    def __init__(self):
        self.messagesString = [("1. Voting won't change anything (broadcast power 1)", 1),
                               ("2. We've got big plans for you (broadcast power 1)", 1),
                               ("3. We reduced unemployment rates last year (broadcast power 2)", 2),
                               ("4. Economy went up by 30% (broadcast power 2))", 2),
                               ("5. Blue has false advertising (broadcast power 3)", 3),
                               ("6. Blue is trying to remove your free choice by forcing you to vote (broadcast power 3)", 3),
                               ("7. We are the real truth (broadcast power 4)", 4),
                               ("8. Life just gets better with us (broadcast power 4)", 4),
                               ("9. Why change what already works (broadcast power 5)", 5),
                               ("10. Order and structure has kept us safe and prosperous (broadcast power 5)", 5)]

    # For player
    def broadcast(self, populationGrid, broadcastOption):
        broadcastOption -= 1
        option = self.messagesString[broadcastOption]
        print(option[0])
        if option[1] == 1:
            print("Message Broadcasted")
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
            print("Message Broadcasted")
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
            print("Message Broadcasted")
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
            print("Message Broadcasted")
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
            print("Message Broadcasted")
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
