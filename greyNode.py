import random;
import collections;

class GreyNode:

    def __init__(self, isAlly):
        self.ally = isAlly
        self.voting = isAlly
        self.uncertain = -1
