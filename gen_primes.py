def gen_possible_primes(n):
	result = []
	i = 1
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
	while i <= (len(possible_primes)+1):
		if (i % prime) == 0:
			possible_primes[i-2] = 0
		i = i + 1
	return possible_primes

def convert(primes):
	result = []
	i = 0
	while i < len(primes):
		if primes[i] == 1: result.append(i+2)
		i = i+1
	return result

def gen_primes(n):
	if n < (2**20):
		possible_primes = gen_possible_primes(n)

		i = 2
		possible_primes = mark_composite(i, possible_primes)
		
		while (i**2) <= n: 
			prime = next_prime(i)
			possible_primes = mark_composite(prime, possible_primes)
			i = i + 1
		primes = convert(possible_primes)
		return primes

