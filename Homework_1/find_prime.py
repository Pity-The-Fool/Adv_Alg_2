from random import randrange, getrandbits

def generate_prime_candidate(length):
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p

def generate_prime_number(length=512):
    p = 4
    # keep generating while the primality test fail
    while not miller_rabin(p, 10):
        p = generate_prime_candidate(length)
    return p

def is_safe_prime(prime):
    return miller_rabin((prime - 1) / 2, 10)

def miller_rabin(n, k):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


p = generate_prime_number()

while not is_safe_prime(p):
    p = generate_prime_number()

print ((p - 1) / 2);

