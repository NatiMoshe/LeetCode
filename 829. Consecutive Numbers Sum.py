class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        num = n
        count = 0 
        i = 1
        #finding 
        while (num > 0):
            num -= i
            if num % i == 0:
                count += 1
            i += 1
        return count
    
    
""" we can simplify:  4 + 5 + 6 = 15  
    to be: (3+1) + (3+2) + (3+3) = 15
    or: 3 + 3 + 3 = 15 - 1 - 2 - 3
    so 3 is base here and the right side is also divisible by 3
    if right side is divisible by BASE = there is a conecutive sum"""