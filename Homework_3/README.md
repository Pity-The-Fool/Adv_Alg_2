CS7082 Assignment 3: Due March 14
==================================================================================
Part 1: Designing a Blockchain
----------------------------------------------------------------------------------

We determine the Blockchain by deciding how? and what? is encoded for each block of the chain. Assume that only outputs from legal transactions called Catx (pronounced 'cats') will be allowed. Each output will be determined by an approved script and appropriate set of parameters.

We will start with a small set of approved Catx outputs, but you are free to add new ones. All allowable Catx have a specified encoding and an associated validation rule for each.

Allowable Scripts
--------------------

    ## Catx Interface API

    scripts ​=​ { ​P2PKH​ :​"OP_DUP OP_HASH160 <Public-Key-Hash> OP_EQUALVERIFY OP_CHECKSIG"​, ​P2PT​: ​"Pay to Post UC Tribute <shortened -url>"​,
        P2UCS​: ​"Pay to UC Scholar <Public-Key-Hash>"​,
        P2HS​ : ​"Pay to Hashed Script <Hashed-Address>"​,
        OTHER​: ​"Another Script"​ }

    def​ ​encodeCatx​(script, ​*​args, ​**​kwargs): ​return​ code


Allowable Addresses - Encodings
-----------------------------------

Scripts might have one or more addresses specified as parameters. Like in BitCoin, allowable addresses are hashed to 20-bytes encoded/formatted in Base58. For example, we can create such an address starting with the public key PK, then compute the SHA256 hash and then compute the RIPEMD160 hash of the result, producing a 160-bit (20-byte) string/number: Address = RIPEMD160(SHA256(PK)). Finally to encode the this address for the Blockchain we will use Base58 encoding using fixed alphabet of 58 symbols.

    alphabet ​=​ ​'123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
    base_count ​=​ ​len​(alphabet)

    def​ ​encode​(num):
        """ Returns num (int) in a base58-encoded string """ encode ​=​ ​''
        assert​(​type​(num) ​==​ ​int​)

        if​ (num ​<​ ​0​):
            return​ ​''

        while​ (num ​>=​ base_count):
            mod ​=​ num ​%​ base_count
            assert​(​type​(mod) ​==​ ​int​ ​and​ mod ​<​ ​58​)
            encode ​=​ alphabet[mod] ​+​ encode
            num ​=​ num ​//​ base_count

        if​ (num):
            encode ​=​ alphabet[num] ​+​ encode

        return​ encode


    def​ ​decode​(s):
        """ Decodes the base58-encoded string s into an integer """
        decoded ​=​ ​0
        multi ​=​ ​1
        s ​=​ s[::​-​1​]

        for​ char ​in​ s:
            decoded ​+=​ multi ​*​ alphabet.index(char)
            multi = multi ​*​ base_count

        return​ decoded




Part 2: Programming Distributed Consensus from Trust
==================================================================

For this assignment, you will design and implement a distributed consensus algorithm which will determine a file of consensus carrying the encoding of a set-list of legal Catx. We assume there is given a graph of “trust” relationships between nodes. This is an alternative method for achieving consensus that does not require proof-of-work or the time and energy associated with proof-of-work.

Nodes in the network are either compliant or malicious. You will write a CompliantNode class (which implements a provided Node interface) that defines the behavior of each of the compliant nodes. The network is a directed random graph, where each edge represents a trust relationship. For example, if there is an A → B edge, it means that Node B listens to broadcast Catx by node A, and by inference trusts that broadcast.


    # Node Interface API

    def​ ​setFollowees​ (followees):
    def​ ​setPendingCatx​ (pendingCatxs): def​ ​sendToFollowers​(candidates):
    def​ ​receiveFromFollowees​ (candidates):

    Consensus: After final ​round​, ​for​ each node, sendToFollowers() should ​return​ the Catxs upon which consensus has been reached.



Each node should succeed in achieving consensus with a network in which its peers are other nodes running the same code. Your algorithm should be designed such that a network of nodes receiving different sets of Catx can agree on a set to be accepted. We will be providing a Simulation class that generates a random trust graph. There will be a set number of rounds where during each round, your nodes will broadcast their proposal to their followers and at the end of the round, should have reached a consensus on what Catxs should be agreed upon.

Each node will be given its list of followees via a boolean array whose indices correspond to nodes in the graph. A ‘true’ at index i indicates that node i is a followee, ‘false’ otherwise. That node will also be given a list of Catx (its proposal list) that it can broadcast to its followers. Generating the initial Catx/proposal list will not be your responsibility. For this part you can assume that all Catx are valid.

In testing, the nodes running your code may encounter a number (up to 45%) of malicious nodes that do not cooperate with your consensus algorithm. Nodes of your design should be able to withstand as many malicious nodes as possible and still achieve consensus. Malicious nodes may have arbitrary behavior. For instance, among other things, a malicious node might:

   * be functionally dead and never actually broadcast any Catx.
   * constantly broadcasts its own set of Catx and never accept Catx given to it.
   * change behavior between rounds to avoid detection.


You will be provided the following files:

   * CompliantNode.py A class skeleton for your CompliantNode class. You should develop your code based off of the template this file provides.
   * Candidate.py a simple class to describe candidate Catx your node recieves
   * MaliciousNode.py a very simple example of a malicious node
   * Simulation.py a basic graph generator that you may use to run your own simulations with varying graph parameters (described below) and test your CompliantNode class
   * Catx.py the Catx class, a transaction from Part I above.


The graph of nodes will have the following parameters:

   * the pairwise connectivity probability of the random graph: e.g. {.1, .2, .3}
   * the probability that a node will be set to be malicious: e.g {.15, .30, .45}
   * the probability that each of the initial valid transactions will be communicated:
       e.g. {.01, .05, .10}
   * the max number of rounds needed to reach consensus e.g. {10, 20}

Your focus will be on developing a robust CompliantNode class that will work in all combinations of the graph parameters. At the end of each round, your node will write a file of Catx using its id as file name. The set written will be determined by the list of transactions that were broadcast to it during previous rounds. Your node will not know the network topology and should do its best to work in the general case. That said, be aware of how different topology might impact what to include in your picture of consensus. Here is a suggested use of python multiprocessing to run the Node code.


    from​ multiprocessing ​import​ Pool, ​TimeoutError
    import​ time
    import​ os
    import​ Node

    def​ ​run​(node, round):
        f ​=​ ​open​(​str​(node.name​+​'round'​)​+​str​(​round​),​'w'​)
        f.write(​'all Catx from this Node'​ ​+​ ​str​(node.name))
        f.write(​'round:'​+​str​(​round)​ )
        f.close()

    #   return "done:" + str(node.name)

    if​ ​__name__​ ​==​ ​'__main__'​:
        numNodes ​=​ ​10
        pool ​=​ Pool(​processes​=n​ umNodes)
        nowNodes ​=​ [Node(​name​='​ node'​+​str​(i)) ​for​ i ​in​ ​range​(numNodes)]
        multiple_results ​=​ [pool.apply(run, ​args​ ​=​ (nowNodes[i],​0)​ )

        for​ i ​in range​(numNodes)]
            print​([res ​for​ res ​in​ multiple_results])


Finishing by Signing the Consensus Block for the BlockChain
--------------------------------------------------------------------

Write a function that reads the file of consensus appends the hash of the previous block and then and appends the final hash for the block to the file.
