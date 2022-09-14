import random;
import collections;


class RedNode:

    def __init__(self):
        self.messagesString = [("Vote Plox",1),("Democracy good",1),("just vote pls, do it",2),("I beg you",2),("red no good",3),("boo red fake news",3),("dont belif media pls",4),("i swear we're better",4),("free healthcare",5),("for the ppl by the ppl",5)]

    def broadcast(self,populationGrid,broadcastOption):
        print("broadcasting")
