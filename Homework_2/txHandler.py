# You will be responsible for creating a module that contains an API called
# txHandler that validates transactions using UTXOpool and updates the pool
# based on processing a set of non-conflicting tranactions contained in the
# pool.

import hashlib
import UTXOPool
from Transaction import Transaction
from keys import verify, n, g, p

class TxHandler():

    def __init__(self, utxoPool):
        self.utxoPool = utxoPool

    def isValidTx(self, tx):
        output_size = tx.getOutputSize()
        input_size = tx.getInputSize()
        associated_utxos = []

        # (1) All outputs claimed by |tx| are in the current UTXO pool,
        # I believe to "claim an output" is to have some output as your
        # own input, so we have to look at all of the inputs in |tx|, and
        # ensure that they exist as outputs in the given UTXOPool.
        for input_idx in range(input_size):
          transaction_input = tx.getInput(input_idx)
          found_input_in_utxo_pool = False

          # Now we have to see if we can find |transaction_input| in the UTXOPool.
          for utxo in self.utxoPool.getAllUTXO():
            if transaction_input.prevTxHash is utxo.getTxHash() and transaction_input.outputIndex is utxo.getIndex():
              found_input_in_utxo_pool = True
              associated_utxos.append(utxo)
              break # I believe this is safe.

          if found_input_in_utxo_pool is False:
            return False

        # (2) the signatures on each input of tx are valid,
        # need to verify() (from keys.py) each signature it seems.
        # This contains the signatures for each input
        public_keys = [self.utxoPool.getTxOutput(utxo).address for utxo in associated_utxos]
        signatures = [transaction_input.signature for transaction_input in tx.inputs]
        hms = [tx.getRawDataToSign(i) for i in range(input_size)]
        for i in range(len(hms)):
          m = hashlib.sha256()
          m.update(str.encode(hms[i]))
          hms[i] = int(m.hexdigest(), 16)

        for combo in zip(public_keys, signatures, hms):
          # |combo| has the form (pk, sig, hm), for each transaction, letting
          # us easily call |verify| with the necessary arguments.
          if verify(combo[0], combo[1], combo[2], p, g) is False:
            print("A signature in the transaction could not be verified")
            return False

        # (3) no UTXO is claimed multiple times by tx,
        # We already have a list of UTXOs associated with each of |tx|'s inputs,
        # so what we can do is simply check to see if any of the UTXOs are duplicates.
        if len(associated_utxos) > len(set(associated_utxos)):
          print("There were '", len(associated_utxos) - len(set(associated_utxos)), "' duplicate UTXOs for this Transaction's inputs")
          return False

        # (4) all of |tx|'s output values are non-negative, and
        for i in range(output_size):
            if tx.getOutput(i).value < 0:
                print("The transaction's output was below zero:", tx.getOutput(i).value)
                return False

        # (5) the sum of tx's input values is greater than or
        # equal to the sum of its output values; and false otherwise.
        # This obviously can only be completed if this check happens after check (4),
        # because negative output values can screw this up.
        input_sum = 0
        output_sum = 0

        # Collect input sums.
        for utxo in associated_utxos:
          input_sum += self.utxoPool.getTxOutput(utxo).value

        # Collect output sums.
        for i in range(output_size):
          output_sum += tx.getOutput(i).value

        if (output_sum > input_sum):
          print("The total output sum of the |tx| exceeds its input sum")
          return False

        # Remove the UTXOs claimed by |tx| from the given UTXOPool.
        # for utxo in associated_utxos:
        # self.utxoPool.remove(utxo)

        return True




    def handleTxs(possibleTxs): # Transaction[] --> Transaction[]
        input_size = possibleTxs.getInputSize()
        output_size = possibleTxs.getOutputSize()
        is_valid = false
        valid_txs = []

        # get all utxos associated with possibleTxs
        for ind in range(input_size):
          transaction_input = possibleTxs.getInput(ind)
          for utxo in self.utxoPool.getAllUTXO():
            if transaction_input.prevTxHash is utxo.getTxHash() and transaction_input.outputIndex is utxo.getIndex():
              associated_utxos.append(utxo)

        # get sum of inputs
        for utxo in associated_utxos:
            input_sum += self.utxoPool.getTxOutput(utxo).value

        # check each transaction for correctness
        for ind in range(0, output_size)
            if isValidTx(possibleTxs[ind]):

                # insert valid transaction into our return list
                # while input sum is greater than current valid_tx sum
                if input_sum > valid_tx_sum:
                    valid_tx_sum += possibleTxs.getOutput(ind).value
                    valid_txs.append(possibleTxs[ind])

                    # update internal view of UTXOPool -- remove chosen tx
                    # self.utxoPool.remove(possibleTxs.getOutput(ind))
                    self.utxoPool.remove(associated_utxos[ind])
                else:
                    break # no more transactions can be added to valid_txs

        # return mutually valid array of accepted transactions
        return valid_txs
