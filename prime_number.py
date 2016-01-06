#!usr/bin/python
# coding: utf-8

import time

def time_it(func):
	def wrapper(*args, **kwargs):
		try:
			s = time.time()
			return fun(*args, **kwargs)
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
def prime_list(num):                             #  0      1     2       num
    isprime_list = [True for i in range(num+1)]  # [True, True, True,...,True]
    for i in range(2, int(num**0.5)+1):
        if isprime_list[i]:
            for j in range(i*i, num, i):
                isprime_list[j] = False

    isprime_list[0] = False
    isprime_list[1] = False         
    
    return isprime_list


@time_it
def test_1():
	ans = 0
    for i in range(2, 10000):
    	if isprime(i):
        	ans += i
    return ans

@time_it
def test_2():
	ans = 0
	for i,tf in enumerate(prime_list(10000)):
		if tf:
			ans += i
	return ans

if __name__ == '__main__':
    print test_1()
    print test_2()
