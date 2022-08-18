import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #איחוד של של שני המערכים על מנת למיין אותם כאחד
        sorted_merged_list = nums1+nums2
        #מיון המערך הממוזג
        sorted_merged_list.sort()
        #טיפול במקרה של אורך זוגי של המערך
        if len(sorted_merged_list) % 2 == 0:
            #החישוב הוא :
            # merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5. 
            return (sorted_merged_list[(int(len(sorted_merged_list) / 2) -1)] + sorted_merged_list[int(len(sorted_merged_list) / 2)]) / 2
        else:
            #במידה והמערך באורך אי זוגי אנו מחזירים פשוט את האיבר האמצעי :
            #merged array = [1,2,3] and median is 3 / 2 = 2.5 -> מעבירים לאינטיג'ר שזה יוצא 2.
            return sorted_merged_list[int(len(sorted_merged_list) / 2)]