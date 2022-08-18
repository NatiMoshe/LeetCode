from functools import reduce
import math


#בשאלה הזאת אנחנו צריחים להגיד כמה איברים נימחק עד שנשיג מערך שכל איבריו מחלקים את האיברים של המערך השני
#נעשה זאת על ידי חישוב המחלק המשותף הכי גדול של כל המערך הראשי
#לאחר מכן נעבור איבר איבר על המערך המחלק ונשאל האם הם מתחלקים ללא שארית עם הג'י סי די
#אם כן לא נעשה כלום
#אם לא נחזיר את האינדקס של אותו איבר כמספר מחיקות שנצטרך לבצע
def minOperations(nums, numsDivide):
    #
    #calc the gcd of all the elements of 'numsDivide'
    gcd = reduce(math.gcd, numsDivide)

    #sorting 'nums' and kepping track over every element index
    #find out who is the smallest element 'nums[i]' in 'nums' that divides gcd
    for i, num in enumerate(sorted(nums)):
        #checking if the element 'nums[i]' divides gcd
        if gcd % num == 0:
            return i

    return -1


print(minOperations([2,3,2,4,3], [9,6,9,3,15]))


"""
the phrase: 
"divides all the elements of numsDivide"

is equals to saying:
"divides gcd of all the elements of numsDivide"
where gcd is the greatest common divisor.

So the first step, find out the gcd of numsDivide,
then sort input nums,
and find out the smallest element nums[i] in nums divides gcd.

We need to remove all elements smaller than nums[i].
If no such nums[i], return -1"""