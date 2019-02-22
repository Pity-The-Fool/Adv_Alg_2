class Transaction():

    class Input():
        def __init__(self, prevHash, index):
            if (prevHash == None):
                self. prevTxHash = None
            else:
                self.prevTxHash = prevHash
            self.outputIndex = index

        def addSignature(self, sig):
            if (sig == None):
                self.signature = None
            else:
                self.signature = sig


    class Output():
        def __init__(self, v, pk):
            self.value = v;    # coin value
            self.address = pk  # public key


    def __init__(self, tx = None):
        self.inputs = []
        self.outputs = []
        if tx != None:
            self.hash = tx.hash


    # Input Methods:
    def addInput(self, prevTxHash, outputIndex):
        inp = self.Input(prevTxHash, outputIndex)
        self.inputs.append(inp)

    def addOutput(self, value, address):
        op = self.Output(value, address)
        self.outputs.append(op)

    def removeInput(self, index):
        self.inputs.remove(index)

    def removeInput(self, ut):
        for u in self.inputs:
            if (u.equals(ut)):
                self.inputs.remove(u)

    def getInput(self, index):
        if (index < len(self.inputs)):
            return self.inputs[index]
        return None

    def getInputSize():
        return len(self.inputs)

    def addSignature(self, signature, index):
        self.inputs[index].addSignature(signature)


    # Output Methods:
    def getOutput(self, index):
        if (index < len(self.outputs)):
            return self.outputs[index]
        return None

    def getOutputSize():
        return len(self.outputs)


    # Get Tx Data Methods:
    def getRawDataToSign(self,index):
        # produces data repr for  ith=index input and all outputs
        sigData = ""
        if (index > len(self.inputs)):
            return None
        inp = self.inputs[index]
        prevTxHash = inp.prevTxHash
        sigData += str(inp.outputIndex)
        sigData += str(prevTxHash)
        for op in self.outputs:
            sigData += str(op.value)
            sigData += str(op.address)
        return sigData

    def getRawTx(self):
        rawTx = ""
        for inp in self.inputs:
            rawTx += str(inp.prevTxHash)
            rawTx += str(inp.outputIndex)
            rawTx += str(inp.signature)

        for op in self.outputs:
            rawTx += str(op.value)
            rawTx += str(op.address)

        return rawTx


    # Hash Methods
    def finalize(self):
        import hashlib
        md = hashlib.sha256()
        md.update(self.getRawTx().encode('utf-8'))
        self.hash = md.hexdigest()

    def getHash(self):
        return self.hash
