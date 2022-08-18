import math
from typing import Counter


class Solution:
    def countPairs(nums, k):
        ans = 0
        gcds = Counter()

        for num in nums:
            #calc gcd of 'num' in 'nums' with k
            gcd_i = math.gcd(num, k)
            for gcd_j, count in gcds.items():
                #'count' indicates how many numbers in 'nums' are divisible by 'gcd_i'
                #checking if former gcd's are divisible by k.
                if gcd_i * gcd_j % k == 0:
                    #summing up the amount of times numbers that were divisible by 'gcd_i'
                    # (which adds up to pairs that are divisible by k)
                    ans += count
            gcds[gcd_i] += 1

        return ans

    # https://leetcode.com/problems/count-array-pairs-divisible-by-k/discuss/1785662/Python-line-by-line-detailed-explanation