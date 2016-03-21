import sys
import math

# Detecting if the given value is prime number by checking it from 2 to it's squre-root
def is_prime(value):
	for i in xrange(2, int(math.sqrt(value) + 1)):
		if value%i == 0:
			return False
	return True

# Printing prime numbers from given minimum to maximum value
def find_primes_in_range(range_min, range_max):
	prime_list = []
	for i in xrange(range_min, range_max):
		if is_prime(i):
			prime_list.append(i)
	# Print the list of primes
	print "Total %d Prime Numbers between %d and %d inclusive. They are:\n%r" \
		%(len(prime_list), range_min, range_max, prime_list)

if __name__ == '__main__':
	find_primes_in_range(19900, 20000)
