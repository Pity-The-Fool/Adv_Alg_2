# You will be responsible for creating a module that contains an API called txHandler that validates transactions using UTXOpool and updates the pool based on processing a set of non-conflicting tranactions contained in the pool.

from UTXO import UTXOPool
from transaction import transaction
from digital_signature import digital_signature

class TxHandler():

    def __init__(self, public, utxoPool):
        self.public = public
        self.utxoPool = utxoPool

    def isValidTx(Transaction tx):
        result = false

        # Returns true if:

        # (1) all outputs claimed by tx are in the current UTXO pool,
        outputSize = tx.getOutputSize()
        for i in range(0, outputSize):
            if !utxoPool.contains(tx.getOutput(i).value):
                return false


        # (2) the signatures on each input of tx are valid,
        i = 0
        while data = tx.getRawDataToSign(i) != None:
            ds = digital_signature.DigitalSignature(data)
            ds.sign(data)
            if ds.verify():
                result = true
            else:
                return false
            ++i


        # TODO: (3) no UTXO is claimed multiple times by tx,


        # (4) all of tx’s output values are non-negative, and
        for i in range(0, ouputSize):
            if tx.getOutput(i).value < 0
                return false

        # TODO: (5) the sum of tx’s input values is greater than or
        # equal to the sum of its output values; and false otherwise.


        return result


    def handleTxs(possibleTxs): # Transaction[] --> Transaction[]
        UTXOPool = UTXOPool.UTXOPool()
        is_valid = false

        for tx in possibleTxs:
            if isValidTx(tx):
                # while still room in validTxSet
                # place tx in array of acceptable transactions

                # Based on the transactions it has chosen to accept, handleTxs should also update
                # its internal view of UTXOPool to reflect the current set of unspent transaction
                # outputs, so that future calls to handleTxs() and isValidTx() are able to correctly
                # process/validate transactions that claimn outputs from transactions that were
                # accepted in a previous call to handleTxs().
        return validTxSet



    # Extra Credit: Improve the handleTxs() method so that it finds a set of transactions with maximum total transaction fees -- i.e. maximize the sum over all transactions in the set of (sum of input values - sum of output values)).
