import math
import random
import hashlib
from common import constant



class DigitalSignature:
    def __init__(self, args):
        self.message = args.message
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
        self.signature = pow(self.generator, (self.message - self.secret) % (self.prime - 1), self.prime)
        return

    def verify(self):
        return (self.signature * self.public) % self.prime == pow(self.generator, self.message, self.prime)

    def printHashed(self):
        print("Hashed Message: " + self.message.hexdigest() + "\n\n")
        return
