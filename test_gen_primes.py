from nose.tools import *

from gen_primes import *

class TestPrimeGeneration():

	def test_gen_possible_primes(self):
		n = 2
		expected_result = [1, 1]
		result = gen_possible_primes(n)
		assert_equals(result, expected_result)

		n = 4
		expected_result = [1, 1, 1, 1]
		result = gen_possible_primes(n)
		assert_equals(result, expected_result)

	def test_gen_next_prime(self):
		i = 2
		expected_result = 3
		result = next_prime(i)
		assert_equals(result, expected_result)

		i = 3
		expected_result = 5
		result = next_prime(i)
		assert_equals(result, expected_result)

	def test_is_prime(self):
		result = is_prime(5)
		assert_true(result)

		result = is_prime(6)
		assert_false(result)

		result = is_prime(7)
		assert_true(result)

	def test_mark_composite(self):
		possible_primes = [1, 1, 1, 1]
		prime = 2
		expected_result = [1, 1, 1, 0]
		result = mark_composite(prime, possible_primes)
		assert_equals(result, expected_result)

		possible_primes = [1, 1, 1, 1, 1, 1]
		prime = 2
		expected_result = [1, 1, 1, 0, 1, 0]
		result = mark_composite(prime, possible_primes)
		assert_equals(result, expected_result)

		possible_primes = [1, 1, 1, 1, 1, 1, 1, 1, 1]
		prime = 3
		expected_result = [1, 1, 1, 1, 1, 0, 1, 1, 0]
		result = mark_composite(prime, possible_primes)
		assert_equals(result, expected_result)

	def test_convert(self):
		primes = [1, 1, 1, 0]
		expected_result = [1, 2, 3]
		result = convert(primes)
		assert_equals(result, expected_result)
