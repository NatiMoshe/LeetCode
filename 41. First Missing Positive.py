class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #אוקיי אז בשאלה הזאת אנחנו צריכים להחזיר את המספר החיובי!! לא כולל אפס!!! שחסר ברצף של המערך הלא ממויין
        #קודם כל מתחילים מהמספר החיובי הראשון כפוטנצייל : 1
        #יוצרים מערך עזר בעזרת הפקודה סט
        #creating set of nums paramas
        nums_set = set(nums)
        missing_num = 1
        
        #פשוט מתחילים לחפש מ - 1 ומגדילים אותו ב - 1.. זאת אומרת שאם המערך מתחיל מ - 3 לדוגמא,
        #אז האיבר החיובי הראשון שחסר ברצף הוא 1
        #iterating from the first positive number '1'
        while missing_num in nums_set:
            missing_num += 1
        return missing_num