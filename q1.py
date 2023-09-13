"""
Write a program to check if two strings are balanced. Strings s1 and s2 are
balanced if all the characters in the s1 are present in s2. The character's position
doesn't matter.

Written By: Medhansh Sharma
"""

def is_balanced(s1: str, s2: str) -> bool:
    """Checks if two strings are balanced or not."""
    if (len(s1) != len(s2)):
        return False
    
    # sorted() uses O(n logn) time complexity
    # so we should be okay using it twice
    s1 = "".join(sorted(s1))
    s2 = "".join(sorted(s2))

    return s1 == s2

if __name__ == "__main__":
    s1 = input()
    s2 = input()

    print(is_balanced(s1, s2))