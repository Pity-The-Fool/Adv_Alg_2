# You will be responsible for creating a module that contains an API called txHandler that validates transactions using UTXOpool and updates the pool based on processing a set of non-conflicting tranactions contained in the pool.

import UTXOPool

def isValidTx(Transaction tx):
    # Returns true if
    # (1) all outputs claimed by tx are in the current UTXO pool,
    # (2) the signatures on each input of tx are valid,
    # (3) no UTXO is claimed multiple times by tx,
    # (4) all of tx’s output values are non-negative, and
    # (5) the sum of tx’s input values is greater than or
    #     equal to the sum of its output values; and false otherwise.
    return false;


def handleTxs(possibleTxs): # Transaction[] --> Transaction[]

# Handles each epoch by receiving a set of proposed
# transactions, checking each transaction for correctness using isValidTx(),
# returning a mutually valid array of accepted transactions.
# handleTxs() should return a mutually valid transaction set of maximal size ---
# one that can’t be enlarged simply by adding more transactions.


# Based on the transactions it has chosen to accept, handleTxs should also update its internal view of UTXOPool to reflect the current set of unspent transaction outputs, so that future calls to handleTxs() and isValidTx() are able to correctly process/validate transactions that claimn outputs from transactions that were accepted in a previous call to handleTxs().

# Extra Credit: Improve the handleTxs() method so that it finds a set of transactions with maximum total transaction fees -- i.e. maximize the sum over all transactions in the set of (sum of input values - sum of output values)).
