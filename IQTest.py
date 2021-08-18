def iq_test(numbers):
    div_arr = [int(i) % 2 for i in numbers.split()]
    m = 0
    print(div_arr)
    if div_arr.count(1) > div_arr.count(0):
        m = 0
    else:
        m = 1
    return div_arr.index(m) + 1

print(iq_test('50 22 44 14 20 14 24 42 99 3 3 24 14 18 4 16 28 30 50 1 46 42 10 12 50 16 2 36 10 2 28 20'))
# 1 2 4 2 3 4 5 5 5 5 6
# 1 0 0 0 1 0 1 1 1 1 0
# o e e e o e o o o o e

# 6 o  5 e
