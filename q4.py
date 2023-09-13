"""
Write a program that helps to find the greatest common divisor of any five
numbers given as input by the user.

Written By: Medhansh Sharma
"""

def greatest_common_divisor(n1: int, n2: int):
    if (n1 == 0):
        return n2
    
    if (n1 == n2):
        return n1
    
    while (n1 > 0 and n2 > 0):
        if (n1 > n2):
            n1 = n1 % n2
        else:
            n2 = n2 % n1  
     
    return n1
 

if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    gcd = 0
    for i in range(len(numbers)):
        gcd = greatest_common_divisor(gcd, numbers[i])
    
    print(gcd)
