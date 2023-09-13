"""
Write a Python class to generate all distinct subsets of a set S, i.e., find
distinct power set of set S. A power set of any set S is the set of all subsets
of S, including the empty set and S itself.
Example:
Input: [4, 5, 6]
Output: [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

Written By: Medhansh Sharma
"""

import itertools

class PowerSet:
    def __init__(self, arr: list):
        self._arr = arr
    
    @property
    def power_set(self):
        prod = [itertools.combinations(d, r) for r in range(n + 1)]
        final = list(itertools.chain.from_iterable(prod))
        return [list(x) for x in final]

if __name__ == "__main__":
    n = int(input())
    d = list(map(int, input().split()))
    pset = PowerSet(d)
    print(pset.power_set)
