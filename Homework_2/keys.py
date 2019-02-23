import math
import random
import hashlib
from common import constant

n = constant.N

# Generator
g = constant.GENERATOR

# Prime
p = constant.PRIME

def genkeys(n, p, g):
  secret = random.getrandbits(n)
  public = pow(g, secret, p)
  return secret, public

def sign(sk, msg, p, g):
  return pow(g, (msg - sk) % (p - 1), p)

def verify(pk, sig, msg, p, g):
  return (sig * pk) % p == pow(g, msg, p)
