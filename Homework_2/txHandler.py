# You will be responsible for creating a module that contains an API called txHandler that validates transactions using UTXOpool and updates the pool based on processing a set of non-conflicting tranactions contained in the pool.

from UTXO import UTXOPool
from transaction import transaction
from digital_signature import digital_signature

class TxHandler():

    def __init__(self, public, utxoPool):
        self.public = public
        self.utxoPool = utxoPool

    def isValidTx(Transaction tx):
        outputSize = tx.getOutputSize()
        inputSize = tx.getInputSize()

        # (1) all outputs claimed by tx are in the current UTXO pool,
        for i in range(0, outputSize):
            coinOut = tx.getOutput(i).value
            if not utxoPool.contains(CoinOut):
                return false


        # TODO: (2) the signatures on each input of tx are valid,



        # TODO: (3) no UTXO is claimed multiple times by tx,


        # (4) all of tx’s output values are non-negative, and
        for i in range(0, ouputSize):
            if tx.getOutput(i).value < 0
                return false

        # (5) the sum of tx’s input values is greater than or
        # equal to the sum of its output values; and false otherwise.
        for i in range(0, inputSize):
            coinIn = previousTx.value # TODO: get coin in from previous transaction output?
            if coinIn < coinOut:
                return false

        return true


    def handleTxs(possibleTxs): # Transaction[] --> Transaction[]
        is_valid = false

        for tx in possibleTxs:
            if isValidTx(tx):  # how do we know if the list is full?
                validTxList.append(tx) # add valid tx to list
                # utxoPool.remove(tx)
                # update UTXOPool ?            else:
                # do something with invalid tx??

        return validTxList



    # Extra Credit: Improve the handleTxs() method so that it finds a set of transactions with maximum total transaction fees -- i.e. maximize the sum over all transactions in the set of (sum of input values - sum of output values)).
