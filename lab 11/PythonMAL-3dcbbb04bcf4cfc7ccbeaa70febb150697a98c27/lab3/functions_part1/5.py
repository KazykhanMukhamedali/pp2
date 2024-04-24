import itertools
def permut(word):
    lst = list(itertools.permutations(word))
    for tup in lst:
        print(''.join(tup))