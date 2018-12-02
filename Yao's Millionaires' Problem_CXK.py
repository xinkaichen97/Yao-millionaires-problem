# -*- coding:utf-8 -*-
import random
import time

Alice_i = int(raw_input('Please input the money of Alice(1-10):\n'))
Bob_j = int(raw_input('Please input the money of Bob(1-10):\n'))
print 'Calculating...'

def range_prime(start, end):
    l = list()
    for i in range(start, end + 1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag:
            l.append(i)
    return l


def generate_keys(p, q):
    numbers = range_prime(10, 100)
    N = p * q
    C = (p - 1) * (q - 1)
    e = 0
    for n in numbers:
        if n < C and C % n > 0:
            e = n
            break
    if e == 0:
        raise StandardError("e not found")

    d = 0
    for n in range(2, C):
        if (e * n) % C == 1:
            d = n
            break
    if d == 0:
        raise StandardError("d not found")
    return ((N, e), (N, d))


def encrypt(m, key):
    C, x = key
    return (m ** x) % C


decrypt = encrypt

pub, pri = generate_keys(101, 197)

def isprime(x):
    if x == 1:
        return False
    k = int(x ** 0.5)
    for j in range(2, k + 1):
        if x % j == 0:
            return False
    return True

def largerthan2(seq):
    s = sorted(seq)
    for i in range(len(s) - 1):
        if s[i + 1] - s[i] < 2:
            return False
        else:
            continue
    return True

def getdigits(num):
    count = 0
    while num != 0:
        num /= 10
        count += 1
    return count

p, u = 0, 1

while True:
    a = random.choice(range(1000, 999999))
    N = getdigits(a)
    if N % 2 == 0:
        if N == 2:
            pub, pri = generate_keys(11, 29)
        elif N == 4:
            pub, pri = generate_keys(101, 197)
        elif N == 6:
            pub, pri = generate_keys(1013, 2039)
    else:
        continue

    b = encrypt(int(a), pub)
    #print b
    print 'Bob sent to Alice [Encrypted] : ' + str(b - Bob_j + 1)
    time.sleep(0.5)
    print 'Alice is decrypting... Could be time-consuming. Please be patient.'

    Alice_y, Alice_z = [], []

    while u <= 10:
        c = decrypt(b - Bob_j + u, pri)
        Alice_y.append(c)
        u += 1

    lower = 10 ** (N / 2 - 1)
    upper = (10 ** (N / 2)) - 1

    primes = []
    for i in range(lower, upper):
        if isprime(i):
            primes.append(i)

    k = 0
    while k < len(primes):
        p = primes[k]
        for y in Alice_y:
            z = y % p
            Alice_z.append(z)
        if largerthan2(Alice_z):
            break
        else:
            Alice_z = []
            k += 1

    if k == len(primes):
        continue
    else:
        break

for w in range(len(Alice_z)):
    if w > Alice_i - 1:
        Alice_z[w] += 1

print 'Alice sent to Bob: p= ' + str(p) + ', z= ' + str(Alice_z)
time.sleep(2)

s = Alice_z[Bob_j - 1]
print 'The j-th number in {z}: ' + str(s)
time.sleep(0.5)

t = int(a) % p
print 'X mod p: ' + str(t)

if t == s:
    print 'Alice has more!'
else:
    print 'Bob has more!'