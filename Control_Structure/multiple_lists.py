"""
Iterating multiple lists at the same time
"""

l1 = [1, 2, 3]
l2 = [6, 7, 8, 9, 10, 11]

for a, b in zip(l1, l2):
    if a > b:
        print(a)
    else:
        print(b)