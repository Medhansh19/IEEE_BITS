"""
You have an array A of length N. The alternating sum of the array is
defined as:
S = ∣A1∣ - ∣A2∣ + ∣A3∣ - ∣A4∣ + ... (-1)^N-1 |An|
⋅∣AN∣
You are allowed to perform the following operation on the array at most once:
 Choose two indices i and j (1 ≤ i < j ≤ N) and swap the elements Ai and Aj
Find the maximum alternating sum you can achieve by performing the
operation at most once.
Note: ∣X∣ denotes the absolute value of X. For example, ∣-4∣ = 4 and ∣7∣ = 7.

Written By: Medhansh Sharma 
"""

def max_sum(arr):
    # [index, value]
    min_positive = [0, max(arr)]
    max_negative = [0, min(arr)]
    for index, ele in enumerate(arr):
        if (index % 2 == 0):
            if ele < min_positive[1]:
                min_positive = [index, ele]
        
        else:
            if ele > max_negative[1]:
                max_negative = [index, ele]

    # switch the max_positive and max_negative element
    arr[min_positive[0]], arr[max_negative[0]] = arr[max_negative[0]], arr[min_positive[0]]
    return arr

def sum_arr(arr):
    arr = max_sum(arr)
    s = 0
    for index, ele in enumerate(arr):
        if (index % 2 == 0):
            s += ele
        else:
            s -= ele
    
    return s

if __name__ == "__main__":
    cases = int(input())
    for t in range(cases):
        n = int(input())
        arr = list(map(lambda x: abs(int(x)), input().split()))
        print(sum_arr(arr))
