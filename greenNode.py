import random
import collections
import time


class greenNode:
    def __init__(self, voting, uncertainty, id):
        self.id = id
        self.voting = voting
        self.uncertainty = uncertainty

    def __hash__(self):
        return hash((self.voting, self.uncertainty, self.id))

    def __eq__(self, other):
        return (self.voting, self.uncertainty, self.id) == (other.voting, other.uncertainty, other.id)

    def flipVote(self):
        self.voting = not self.voting

    def setUncertainty(self, value):
        self.uncertainty += value

    def interact(self, neighbour):
        if(self.id != neighbour.id):
            influenceUncertainty = float(
                "{:.1f}".format(random.uniform(0.1, 0.4)))
            influenced = random.randrange(1, 3)
            if (influenced == 1):
                if(neighbour.uncertainty > self.uncertainty):
                    if(neighbour.voting != self.voting):
                        self.setUncertainty(influenceUncertainty)
                        self.flipVote()
                        x = 1 - self.uncertainty
                        self.uncertainty = 1 - x
                    else:
                        self.setUncertainty(-influenceUncertainty)
                        if(self.uncertainty < -1):
                            self.uncertainty = -1
                elif(neighbour.uncertainty < self.uncertainty):
                    if (neighbour.voting != self.voting):
                        neighbour.setUncertainty(influenceUncertainty)
                        if (neighbour.uncertainty > 1):
                            self.flipVote()
                            x = 1 - self.uncertainty
                            self.uncertainty = 1 - x
                    else:
                        neighbour.setUncertainty(-influenceUncertainty)
                        if (neighbour.uncertainty < -1):
                            neighbour.uncertainty = -1
