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
