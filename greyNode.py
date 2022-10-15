import random;
import collections;

class GreyNode:

    def __init__(self,id, isAlly):
        self.id = id
        self.ally = isAlly
        self.voting = isAlly
        self.uncertainty = -1

    def setUncertainty(self, number):
        self.uncertainty = -1

    def flipVote(self):
        self.voting = self.ally

    def interact(self,neighbour):
        if (self.id != neighbour.id):
            print(self.id, ' is interacting with ', neighbour.id)
            influenceUncertainty = float(
                "{:.1f}".format(random.uniform(0.1, 0.4)))
            influenced = random.randrange(1, 3)
            if (influenced < 2):
                if (neighbour.voting != self.voting):
                    neighbour.setUncertainty(influenceUncertainty)
                    if (neighbour.uncertainty > 1):
                        neighbour.flipVote()
                        x = 1 - neighbour.uncertainty
                        neighbour.uncertainty = 1 - x
                else:
                    neighbour.setUncertainty(-influenceUncertainty)
                    if (neighbour.uncertainty < -1):
                        neighbour.uncertainty = -1
            else:
                print('no one is convinced\n')
