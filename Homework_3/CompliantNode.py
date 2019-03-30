from Node import Node
#/* CompliantNode refers to a node that follows the rules (not malicious)*/
class CompliantNode(Node):

    def __init__(self, p_graph, p_malicious, p_txDistribution, numRounds):
         # Ignore p_malicious, p_graph, p_txDistribution, and num_rounds
         self.initial_tx = set()
         self.tx_set = set()
         self.followees = []


    def setFollowees(self, followees):
        self.followees = followees

    def setPendingTransaction(self, pendingTransactions):
        self.initial_tx = pendingTransactions
        self.tx_set = pendingTransactions


    def sendToFollowers(self):
        # should return the Catxs upon which consensus has been reached
        return self.tx_set

    def receiveFromFollowees(self,candidates):
        our_intersection = self.tx_set.intersection(candidates)
        return our_intersection.union(self.initial_tx)
