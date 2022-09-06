import random;
import collections;


class greenNode:
    def __init__(self, voting,uncertainty):
        self.voting = voting
        self.uncertainty = uncertainty

    def flipVote(self):
        self.voting = not self.voting

    def setUncertainty(self,value):
        self.uncertainty += value
