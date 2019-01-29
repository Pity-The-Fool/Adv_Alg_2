import math
import random
import hashlib
from common import constant



class DigitalSignature:
    def __init__(self, args):
        self.args = args
        self.n = constant.N
        self.prime = constant.PRIME
        self.generator = constant.GENERATOR
        self.secret = None
        self.public = None
        self.signature = None
        return
    
    def generateKeys(self):
        self.secret = random.getrandbits(self.n)
        self.public = pow(self.generator, self.secret, self.prime)
        return

    def sign(self):
        self.signature = pow(self.generater, (self.args.message - self.secret) % (self.prime - 1), self.prime)
        return

    def verify(self):
        return (self.generateKeys * self.secret) % self.prime == self.signature