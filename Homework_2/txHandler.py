# You will be responsible for creating a module that contains an API called
# txHandler that validates transactions using UTXOpool and updates the pool
# based on processing a set of non-conflicting tranactions contained in the
# pool.

import UTXOPool
from Transaction import Transaction
# Do we need the digital signature's fns?

class TxHandler():

    def __init__(self, utxoPool):
        #self.public = public
        self.utxoPool = utxoPool

    def isValidTx(self, tx):
        outputSize = tx.getOutputSize()
        input_size = tx.getInputSize()

        # (1) All outputs claimed by |tx| are in the current UTXO pool,
        # I believe to "claim an output" is to have some output as your
        # own input, so we have to look at all of the inputs in |tx|, and
        # ensure that they exist as outputs in the given UTXOPool.
        for input_idx in range(input_size):
          transaction_input = tx.getInput(input_idx)
          found_input_in_utxo_pool = False

          # Now we have to see if we can find |transaction_input| in the UTXOPool.
          for utxo in self.utxoPool.getAllUTXO():
            # TODO(domfarolino): Also do an index check!
            if transaction_input.prevTxHash is utxo.getTxHash() and transaction_input.outputIndex is utxo.getIndex():
              found_input_in_utxo_pool = True

          if found_input_in_utxo_pool is False:
            return False

        # ...

        # TODO: (2) the signatures on each input of tx are valid,
        # need to verify() (from keys.py) each signature it seems.



        # TODO: (3) no UTXO is claimed multiple times by tx,


        return True
        # (4) all of tx’s output values are non-negative, and
        for i in range(0, ouputSize):
            if tx.getOutput(i).value < 0:
                return false

        # (5) the sum of tx’s input values is greater than or
        # equal to the sum of its output values; and false otherwise.
        for i in range(0, inputSize):
            input_value = previousTx.value # TODO: get coin in from previous transaction output?
            if coinIn < coinOut:
                return false

        return True


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
