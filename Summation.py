def summation(num):
	answer = None
	for i in range(num + 1):
		if i == 0:
			answer = 0
		if i > 0:
			answer += i

	return(answer)
print(summation(2))


def summation(num):
	answer = sum(list(range(num + 1)))
	return(answer)
# n = 5
# summation=lambda n:n*-~n>>1
# print(summation)