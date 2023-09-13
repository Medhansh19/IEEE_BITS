"""
Write a Python program that takes an integer n as input and prints a spiral
pattern of numbers, starting from 1 and spiralling outward. For example, if n is
5, the pattern should look like:
1  2  3  4  5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

1  2  3  4  5  6
20 21 22 23 24 7
19 32 33 34 25 8
18 31 36 35 26 9
17 30 29 28 27 10
16 15 14 13 12 11

1 2 3
8 9 4
7 6 5

1 2
4 3

Written By: Medhansh Sharma
"""

if __name__ == "__main__":
    n = int(input())
    grid = [[" -" for i in range(n)] for j in range(n)]

    ele = n*n
    dir = "r"   # "r", "d", "l", "u"
    row, col = 0, 0
    for i in range(1, ele+1):
        grid[row][col] = str(i) if i > 9 else f" {i}"
        s = n % col if col != 0 else 0
        r = n % row if row != 0 else 0
        if (dir == "r"):
            if (col == n - row - 1): # we are farmost right
                row += 1
                dir = "d"
            else:
                col += 1
        
        elif (dir == "d"):
            if (row == col): # we are farmost down
                col -= 1
                dir = "l"
            else:
                row += 1
        
        elif (dir == "u"):
            if (row == col + 1):
                col += 1
                dir = "r"
            else:
                row -= 1
        
        elif (dir == "l"):
            if (col == r - 1):
                row -= 1
                dir = "u"
            else:
                col -= 1
    
    for a in grid:
        print(*a)
