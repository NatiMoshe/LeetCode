import math 
def isGoodArray(nums):
    n = len(nums)
    #if there is just the number '1' in nums return true
    if n == 1:
        return nums[0] == 1
    #calc the first gcd
    d = math.gcd(nums[0], nums[1])
    #all we have to see is if there is a combination with gcd = 1
    for num in nums:
        d = math.gcd(num, d)
    return d == 1

print(isGoodArray([3,6,7,3,1,2,10]))


""" Bézout's identity:  gcd(a,b) = d  ->  f(x,y) | ax + by = d """
# https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity