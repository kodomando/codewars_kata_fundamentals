'''Given a positive number n > 1 find the prime factor
decomposition of n.
The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"'''


def prime_factors(n):
	primes = [2, 3, 5, 7, 11, 13, 17, 19]
	prime_dict = {'2': 0, '3': 0, '5': 0, '7': 0, '11': 0, '13': 0, '17': 0, '19': 0}

	def loop(n):
		for number in primes:
			if n % number == 0 and n == 0:
				break

			elif n % number == 0:
				prime_dict[str(number)] += 1
				n //= number
				loop(n)

			elif n % number != 0:
				primes.pop(primes.index(number))
	loop(n)

	answer= [f'({key})' if value == 1 else f'({key}**{value})' for (key, value) in prime_dict.items() if value >= 1]
	return ''.join(answer)


# def prime_factors(n):
# 	# def primes(n):
# 	# 	odds = range(3, n + 1, 2)
# 	# 	sieve = set(sum([list(range(q * q, n + 1, q + q)) for q in odds], []))
# 	# 	return [2] + [p for p in odds if p not in sieve]
#
# 	def get_primes(n):
# 		numbers = set(range(n, 1, -1))
# 		primes = []
# 		while numbers:
# 			p = numbers.pop()
# 			primes.append(p)
# 			numbers.difference_update(set(range(p * 2, n + 1, p)))
# 		return primes
#
# 	primes = get_primes(n)
# 	# prime_dict = {str(key):0 for key in primes if key}
# 	# prime_dict = {'2': 0, '3': 0, '5': 0, '7': 0, '11': 0, '13': 0, '17': 0, '19': 0}
# 	prime_dict = {}
# 	print(primes)
#
# 	# def loop(n):
# 	# 	for number in primes:
# 	# 		if n % number == 0 and n == 0:
# 	# 			print(number)
# 	# 			print(n)
# 	# 			print(prime_dict)
# 	# 			break
# 	#
# 	# 		elif n % number == 0:
# 	# 			if str(number) not in prime_dict:
# 	# 				prime_dict[str(number)] = 0
# 	# 			else:
# 	# 				prime_dict[str(number)] += 1
# 	# 				n //= number
# 	# 				print(number)
# 	# 				print(n)
# 	# 				print(prime_dict)
# 	# 				loop(n)
# 	#
# 	#
# 	# 		elif n % number != 0:
# 	# 			print(number)
# 	# 			print(n)
# 	# 			print(prime_dict)
# 	# 			primes.pop(primes.index(number))
# 	# loop(n)
#
# 	answer= [f'({key})' if value == 1 else f'({key}**{value})' for (key, value) in prime_dict.items() if value >= 1]
# 	print(answer)
# 	return ''.join(answer)

# for number in primes:
# 	while n % number == 0:
# 		prime_dict['2'] += 1
# 		if n % number != 0:
# 			continue

# def prime_factors(n):
# 	dict_answers = {}
# 	while n > 0:


# def gen_primes(n):
# 	D = {}
# 	q = 2
#
# 	while q <= n:
# 		if q not in D:
# 			yield q
# 			D[q * q] = [q]
# 		else:
# 			for p in D[q]:
# 				D.setdefault(p + q, []).append(p)
# 			del D[q]
# 		q += 1
#
#
# def prime_string(m, k):
# 	if k < 1:
# 		return ''
# 	if k == 1:
# 		return '(%i)' % m
#
# 	return '(%i**%i)' % (m, k)
#
#
# def prime_factors(n):
# 	if n < 3:
# 		return n
# 	s = ''
# 	for p in gen_primes(n / 2):
# 		if n < 2:
# 			break
# 		if n % p != 0:
# 			continue
# 		ni = 0
# 		while n % p == 0:
# 			ni += 1
# 			n /= p
# 		s += prime_string(p, ni)
# 	if not s:
# 		return '(%i)' % n
#
# 	return s

# def primes(n):
#     n += 1
#     sieve = [True] * n
#     for i in range(3,int(n**0.5)+1,2):
#         if sieve[i]:
#             sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
#     return [2] + [i for i in range(3,n,2) if sieve[i]]
#
#
# def mults(n):
#     res = []
#     for p in primes(n):
#         rest = n
#         s = 0
#         while rest >0:
#             j = rest // p
#             s += j
#             rest = j
#         if s > 1:
#             res.append(f'{p}^{s}')
#         else:
#             continue
#     return ' * '.join(res)

n = 7775460
print(mults(n))
