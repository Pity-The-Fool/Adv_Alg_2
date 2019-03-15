#!/usr/bin/python3


# CompliantNode refers to a node that follows the rules (not malicious)
class CompliantNode(Node):

    def __init__(self, p_graph, p_malicious, p_txDistribution, numRounds):
#       // IMPLEMENT THIS
        # TODO: not sure any of this is necessary
        self.p_graph = p_graph
        self.p_malicious = p_malicious
        self.p_txDistribution = p_txDistribution
        self.numRounds = numRounds

        # why not do this??
        self.followees = []
        self.pendingTransactions = set()


    def setFollowees(self, followees):
        self.followees = followees


    def setPendingTransaction(self, pendingTransactions):
        self.pendingTransactions = pendingTransactions

    # Consensus: After final round, for each node, sendToFollowers() should return
    # the Catxs upon which consensus has been reached.
    def sendToFollowers(self):
#        // IMPLEMENT THIS
        return self.pendingTransactions

    def receiveFromFollowees(self,candidates):
#        // IMPLEMENT THIS
        pass
