#!/usr/bin/python3
import unittest
import hashlib
import random
from Transaction import Transaction
from UTXOPool import UTXOPool
from UTXO import UTXO
from txHandler import TxHandler
from keys import genkeys, sign, verify, n, g, p

class TestMethods(unittest.TestCase):

    def test_strings(self):
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_keysigs(self):
        m = hashlib.sha256()
        m.update(b"Nobody respects")
        m.update(b" the spammish repetition")
        skx, pkx = genkeys(n,p,g)
        hm=int(m.hexdigest(),16)
        sig= sign(skx,hm,p,g)
        self.assertTrue(verify(pkx,sig,hm,p,g))
        self.assertFalse(verify(pkx,sig,hm+1,p,g))

    def test_1(self):
        possibleTxs = []
        print("Test 1: test isValidTx() with valid transactions")
        nPeople = 10
        people = [] #new List DigSigKeyPair
        # Create |nPeople| pairs of {secret, public} keys.
        for i in range(nPeople):
           sk,pk = genkeys(n,p,g)
           people.append((sk,pk))

        # Create a pool and an index into key pairs
        utxoPool = UTXOPool()
        utxoToKeyPair = {} # {UTXO: (sk, pk)}

        # |keyPairAtIndex| maps {idx: (sk, pk)}, so we
        # can know a person's keys for a given
        # Transaction.Output in a Transaction.
        keyPairAtIndex = {}
        nUTXOTx=10
        maxUTXOTxOutput = 5
        maxInput = 3
        maxValue = 100

        # For num Transaction()s:
        for i in range(nUTXOTx):
           num = random.randint(1,maxUTXOTxOutput)
           tx = Transaction()
           # Add num random outputs to tx.
           for j in range(num):
              # Pick a random public address and transaction value.
              rIndex = random.randint(0,len(people)-1)
              #print("Index",rIndex); print(people[rIndex])
              addr = people[rIndex][1]  #(sk,pk)
              value = random.random() * maxValue
              tx.addOutput(value, addr)
              keyPairAtIndex[j] = people[rIndex]
           tx.finalize()

           # Add all of the Transaction's outputs to UTXOPool.
           for j in range(num):
              ut = UTXO(tx.getHash(), j)
              utxoPool.addUTXO(ut, tx.getOutput(j))
              utxoToKeyPair[ut] = keyPairAtIndex[j]

        # At this point we have a UTXOPool with all of the generated UTXOs
        # in the form of:
        #   {UTXO(TransactionHash, TransactionIndex): Transaction.Output},
        # as well as a map {UTXO: (sk, pk)}, so we can book-keep the
        # identities of the UTXO "authors" for testing.

        print("Len of utxoSet", len(utxoPool.getAllUTXO()))
        maxValidInput = min(maxInput, len(utxoPool.getAllUTXO()))

        nTxPerTest= 11
        maxValidInput = 2
        maxOutput = 3
        passes = True
        txHandler = TxHandler(utxoPool)

        for i in range(nTxPerTest):
           tx = Transaction() # Create a new Transaction.
           utxoAtIndex = {}
           nInput = random.randint(1, maxValidInput + 1)
           inputValue = 0.0

           # We're using this as our sample space to pull UTXOs from for
           # a Transaction's input. This is helpful because it ensures that
           # we never introduce a duplicate UTXO for an input of a valid Transaction.
           utxoSet = set(utxoPool.getAllUTXO())

           # Add a bunch of inputs to |tx|.
           for j in range(nInput):
              # Choose a random UTXO to fund the input.
              # There is a non-zero chance that this could actually
              # pick duplicate UTXOs for a Transaction's input, thus
              # breaking the test.
              utxo = random.sample(utxoSet, 1)[0]
              tx.addInput(utxo.getTxHash(), utxo.getIndex())
              utxoSet.remove(utxo) # Ensure we do not pick this UTXO as another input.
              inputValue += utxoPool.getTxOutput(utxo).value
              utxoAtIndex[j] = utxo

           nOutput = random.randint(1,maxOutput)
           outputValue = 0.0

           # Add a bunch of outputs to |tx|, as long as the sum of
           # all of the outputs <= the sum of the inputs.
           for j in range(nOutput):
               value = random.random()*(maxValue)
               if (outputValue + value > inputValue): # Keep the transaction valid.
                  break

               # Pick a random person to send the $ to.
               rIndex = random.randint(0,len(people)-1)
               addr = people[rIndex][1] # Random person's public key address.
               tx.addOutput(value, addr)
               outputValue += value

           # Sign each input of the transaction.
           for j in range(nInput):
             m=hashlib.sha256()
             m.update(str.encode(tx.getRawDataToSign(j)))
             hm = int(m.hexdigest(),16)
             signature = sign(utxoToKeyPair[utxoAtIndex[j]][0], hm,p,g)
             tx.addSignature(signature, j)

           # Compute overall transaction hash.
           tx.finalize()

           possibleTxs.append(tx)

           if (not txHandler.isValidTx(tx)):
             passes = False
        self.assertTrue(passes)

        valid_txs = txHandler.handleTxs(possibleTxs)

        for tx in valid_txs:
           if txHandler.isValidTx(tx):
               is_valid = true
           else:
               is_valid = false
               break

        print("handleTxs: ")
        self.assertTrue(is_valid)


if __name__ == '__main__':
    unittest.main()
