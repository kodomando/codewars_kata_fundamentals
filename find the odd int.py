def find_it(seq):
    odds = set()
    for x in seq:
        odds.symmetric_difference_update([x])
    odds = list(odds)
    return odds[0]
