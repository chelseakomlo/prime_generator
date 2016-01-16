def gen_possible_primes(n):
	result = []
	i = 0
	while i < n: 
		result.append(1)
		i = i+1
	return result

# make this probablistic
def is_prime(i):
	x = 2
	while (i % x) != 0:
		x = x + 1
	if x == i: return True
	return False

def next_prime(i):
	i = i + 1
	if is_prime(i): return i 
	return next_prime(i)

def mark_composite(prime, possible_primes):
	i = prime+1
	while i <= len(possible_primes):
		if (i % prime) == 0:
			possible_primes[i-1] = 0
		i = i + 1
	return possible_primes

def gen_primes(n):
	while n < (2**20):
		possible_primes = gen_bool_list(n)
		i = 2

		while (i**2) < n: 
			# find the next prime
			next_prime = next_prime(i)
			
			# for all multiples of i to n, mark them as non-prime (composite)
			possible_primes = mark_composite(next_prime, possibe_primes)

			# this means, in our possible_primes list, we will set the boolean to 0 (false)
			i = i + 1
		return primes

