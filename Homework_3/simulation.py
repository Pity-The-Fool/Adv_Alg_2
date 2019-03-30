#!/usr/bin/python3

import sys

from Candidate import Candidate
#from Catx import scripts, encodeCatx
from CompliantNode import CompliantNode
from MaliciousNode import MaliciousNode
import random
from Transaction import Transaction


def main(args):
##      // There are four required command line arguments: p_graph (.1, .2, .3),
##      // p_malicious (.15, .30, .45), p_txDistribution (.01, .05, .10),
##      // and numRounds (10, 20). You should try to test your CompliantNode
##      // code for all 3x3x3x2 = 54 combinations.
##
    numNodes = 100
    p_graph = args[0] # // parameter for random graph: prob. that an edge will exist
    p_malicious = args[1] # // prob. that a node will be set to be malicious
    p_txDistribution = args[2]  #// probability of assigning an initial transaction to each node
    numRounds = args[3]  #// number of simulation rounds your nodes will run for

 #     // pick which nodes are malicious and which are compliant
    nodes = [None for i in range(numNodes)]
    for i in range(numNodes):
         if random.random() < p_malicious:
            nodes[i] = MaliciousNode(p_graph, p_malicious, p_txDistribution, numRounds)
         else:
            nodes[i] = CompliantNode(p_graph, p_malicious, p_txDistribution, numRounds)

    followees = [[1 if random.random() < p_graph and i!= j else 0 for i in range(numNodes)] for j in range(numNodes)]
    for i in range(numNodes):
         nodes[i].setFollowees(followees[i]);

##      // initialize a set of 500 valid Transactions with random ids
    numTx = 500
    validTxIds = set()
    for i in range(numTx):
         validTxIds.add(random.randint(1000,50000))


##      // distribute the 500 Transactions throughout the nodes, to initialize
##      // the starting state of Transactions each node has heard. The distribution
##      // is random with probability p_txDistribution for each Transaction-Node pair.

    pendingTransactions = set()
    for i in range(numNodes):
        for txid in validTxIds:
          if (random.random() < p_txDistribution): #// p_txDistribution is .01, .05, or .10.
                     pendingTransactions.add(Transaction(txid))

        nodes[i].setPendingTransaction(pendingTransactions)


    for round in range(numRounds):
##         // gather all the proposals into a map. The key is the index of the node receiving
##         // proposals. The value is an List containing pairs. The first
##         // element is the id of the transaction being proposed and the second
##         // element is the index # of the node proposing the transaction.
         allProposals = {}

         for i in range(numNodes):
            proposals = nodes[i].sendToFollowers()
            for tx in proposals:
               if (tx not in validTxIds):
                  break  #// ensure that each tx is actually valid

               for j in range(numNodes):
                   if (not followees[j][i]):
                       break #continue; // tx only matters if j follows i

                   if (j not in allProposals):
                       candidates = set()
                       allProposals[j] = candidates
                   candidate = Candidate(tx, i)
                   allProposals[j].add(candidate) # I guess brackets here is what we should do?

##         // Distribute the Proposals to their intended recipients as Candidates
         for i in range(numNodes):
            if (i in allProposals):
               nodes[i].receiveFromFollowees(allProposals.get(i));



 #     // print results
    for i in range(numNodes):
         transactions = nodes[i].sendToFollowers()
         print("Transaction ids that Node " + str(i) + " believes consensus on:")
         for tx in transactions:
             print(tx.id)

# All of the arrays below are directly from the homework assignment
# (except I added |30| to the final array, for fun)

for g in [0.1, 0.2, 0.3]:
    for m in [0.15, 0.3, 0.45]:
        for t in [0.01, 0.05, 0.1]:
            for r in [10, 20, 30]:
                main([g, m, t, r])
