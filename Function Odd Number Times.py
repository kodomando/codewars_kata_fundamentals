def find_odds(seq):
    odds = set()
    for x in seq:
        odds.symmetric_difference_update([x])
    return odds

list = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
print(find_odds(list))