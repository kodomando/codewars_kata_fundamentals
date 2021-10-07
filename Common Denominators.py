from collections import Counter
from math import pow, prod

def convert_fracts(lst):
    print(lst)
    def primes(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    denominator = [bottom for (top, bottom) in lst]
    denominator.sort()

    hold = {}
    def getMultiples(*x):
        for things in x:
            l_prime = primes(things)
            temp_dict = {}
            # print('l_prime:', l_prime)
            temp_dict.update(zip(Counter(l_prime).keys(), Counter(l_prime).values()))
            for key in temp_dict:
                # print(temp_dict)
                if key not in hold.keys():
                    hold[key] = temp_dict[key]
                    print('hold:', hold)
                elif key in hold.keys():
                    max_val = max(temp_dict[key], hold[key])
                    hold[key] = max_val

    getMultiples(*denominator)
    # print('hold:', hold)
    lcm = prod([int(pow(key, value)) for key, value in hold.items()])
    print('lcm:', lcm)
    print('list before return:', lst)
    return [[top, bottom] if bottom == lcm else [(lcm//bottom)*top, lcm] for (top, bottom) in lst]

'''
    //NOTES
    1) Create a list from denominators and sort lowest to highest n
    2) Function for prime factors
    3) Function to get Lowest Common Multiple
        - Compare Each dict of factors for each denominator to the
          master dictionary. If value exists compare and set key val to
          max of the two.
        - If doesn't exist, simply update dict with new key-val pair
    4) Multiply n in LCM list
    5) Final list consists of:
        - Turn each respective denominators into LCM
        - Multiply each respective numerators by (LCM//original_numerator)
    6) If All denominators come in as the same, make no changes.'''



##### TESTS #####
# convert_fracts([(1, 24), (2, 16),(3, 14)])
print(convert_fracts([[69, 130], [87, 1310], [3, 4]]))
# print(convert_fracts([(1, 2), (1, 3), (1, 4), (1, 16), (1, 12)]))
# convert_fracts([(1, 2)])
# print(convert_fracts([(6, 12), (4, 12), (3, 12)]))
# print(convert_fracts([[2, 7], [1, 3], [1, 12]]))

