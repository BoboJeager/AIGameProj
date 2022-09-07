import random;
import collections;


class greenNode:
    def __init__(self, voting,uncertainty,id):
        self.id = id
        self.voting = voting
        self.uncertainty = uncertainty

    def __hash__(self):
        return hash((self.voting, self.uncertainty,self.id))

    def __eq__(self, other):
        return (self.voting, self.uncertainty,self.id) == (other.voting, other.uncertainty,other.id)

    def flipVote(self):
        self.voting = not self.voting

    def setUncertainty(self,value):
        self.uncertainty += value

    def interact(self, neighbour):
        print('interacting')
