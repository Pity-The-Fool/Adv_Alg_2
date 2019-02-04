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

    def get_message_value(self):
        m = hashlib.sha256();
        message_bytes = bytes(self.message, encoding='utf-8')
        m.update(message_bytes)
        return int.from_bytes(m.digest(), 'big')

    def generateKeys(self):
        self.secret = random.getrandbits(self.n)
        self.public = pow(self.generator, self.secret, self.prime)
        return

    def sign(self):
        message_value = self.get_message_value()
        self.signature = pow(self.generator, (message_value - self.secret) % (self.prime - 1), self.prime)
        return

    def verify(self):
        message_value = self.get_message_value()
        return (self.signature * self.public) % self.prime == pow(self.generator, message_value, self.prime)

    def printHashed(self):
        print("Hashed Message: " + self.message.hexdigest() + "\n\n")
        return
