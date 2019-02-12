# import hw#1 class

# A transaction consists of a list of inputs, a list of outputs, and a unique ID
# The class should contain methods to add and remove input items, add and remove output items,
# compute raw digests to be signed, add a signature to an input, and compute and
# store the hash-pointer of the entire transaction once all inputs/outputs/signatures have been added.
class Transaction:
    def __init__(self):


    # A transaction input consists of a hash-pointer to the transaction that contains the funding of the corresponding output,
    # the index of this funding output in that transaction, and a digital signature signed by the public key associated with the transaction input.
    class Transaction.Input:
        def __init__(self):


    # A transaction output consists of a coin value and a public key to which it is being paid.
    class Transaction.Output:
        def __init__(self):
