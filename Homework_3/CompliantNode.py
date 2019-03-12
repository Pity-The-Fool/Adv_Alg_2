#!/usr/bin/python3


# CompliantNode refers to a node that follows the rules (not malicious)
class CompliantNode(Node):

    def __init__(self, p_graph, p_malicious, p_txDistribution, numRounds):
#       // IMPLEMENT THIS
        pass


    def setFollowees(self, followees):
#        // IMPLEMENT THIS
        pass

    def setPendingTransaction(self, pendingTransactions):
#        // IMPLEMENT THIS
      pass

    # Consensus: After final ​round​, ​for​ each node, sendToFollowers() should ​return
 ​   # the Catxs upon which consensus has been reached.
    def sendToFollowers(self):
#        // IMPLEMENT THIS
       pass

    def receiveFromFollowees(self,candidates):
#        // IMPLEMENT THIS
        pass
