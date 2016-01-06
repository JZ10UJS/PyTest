#!usr/bin/python
# coding: utf-8

import time


def time_it(func):
    def wrapper(*args, **kwargs):
        try:
            s = time.time()
            return func(*args, **kwargs)
        finally:
            e = time.time()
            print 'using time: ', e-s
    return wrapper


# return True if num is prime else False
def isprime(num):
    assert isinstance(num, int) and num>1, 'num must be an integer and greater than 1'
    for i in range(2, int(round(num**0.5,0)+1)):
        if not num%i:
            return False
    return True


# get all the prime numbers <= num
def prime_list(plist, lo, hi):                          
    for i in range(2, int((hi-lo)**0.5)):
        if plist[i]:
            for j in range(i*i, (hi-lo), i):
                plist[j] = False

    plist[0] = False
    plist[1] = False         


@time_it
def test_1():
    ans = 0
    for i in range(2, 10**5):
        if isprime(i):
            ans += i
    return ans


@time_it
def test_2():
    isprime_list = [True for i in range(10**5+1)]  # [True, True, True,...,True]
    prime_list(isprime_list, 0, len(isprime_list))
    ans = 0
    for i,tf in enumerate(isprime_list):
        if tf:
            ans += i
    return ans


if __name__ == '__main__':
    print test_1()
    print test_2()
