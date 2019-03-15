#!/usr/bin/python3

from Node import Node

# CompliantNode refers to a node that follows the rules (not malicious)
class CompliantNode(Node):

    def __init__(self, p_graph, p_malicious, p_txDistribution, numRounds):
        Node.__init__(self, p_graph, p_malicious, p_txDistribution, numRounds)

        self.followees = []               # followees is a list in simulation.py
        self.pendingTransactions = set()  # pendingTransactions is a set in simulation.py


    def setFollowees(self, followees):
        self.followees = followees


    def setPendingTransaction(self, pendingTransactions):
        self.pendingTransactions = pendingTransactions

    # Consensus: After final round, for each node, sendToFollowers() should return
    # the Catxs upon which consensus has been reached.
    def sendToFollowers(self):
        return self.pendingTransactions


    def receiveFromFollowees(self, candidates):
        # TODO: implementation
        pass
