#!/usr/bin/python3

from Node import Node

class MaliciousNode(Node):

    def __init__(self, p_graph, p_malicious, p_txDistribution, numRounds):
        Node.__init__(self, p_graph, p_malicious, p_txDistribution, numRounds)
