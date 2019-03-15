#!/usr/bin/python3

class Node(object):

    def __init__(self, p_graph, p_malicious, p_txDistribution, numRounds):
        # TODO: not sure any of this is necessary
        self.p_graph = p_graph
        self.p_malicious = p_malicious
        self.p_txDistribution = p_txDistribution
        self.numRounds = numRounds


    def setFollowees(self, followees):
        #        // IMPLEMENT THIS
        pass

    def setPendingTransaction(self, pendingTransactions):
        #        // IMPLEMENT THIS
      pass


    def sendToFollowers(self):
        #        // IMPLEMENT THIS
       pass

    def receiveFromFollowees(self,candidates):
        #        // IMPLEMENT THIS
        pass
