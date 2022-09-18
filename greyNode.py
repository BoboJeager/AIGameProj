import random;
import collections;

class GreyNode:

    def __init__(self,id, isAlly):
        self.id = id
        self.ally = isAlly
        self.voting = isAlly
        self.uncertain = -1
