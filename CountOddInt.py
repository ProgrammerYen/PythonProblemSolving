def find_odd_int(seq):
    return [i for i in seq if seq.count(i) % 2 == 1][0]