# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         num = nums[0]
#         for i in range(len(nums)):
#             if nums[i] <= num:
#                 num = nums[i]
#         return num



#מה שלמעלה זה מה  שהגשתי כניראה מהעתקה של מישהו וזה אשכרה יכול להיסתכם בשורה אחת שלא חשבתי עלייה


#בגדול צריך להחזיר את האיבר המינימלי
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)


# nums = [2,2,2,0,1]
# print(min(nums))