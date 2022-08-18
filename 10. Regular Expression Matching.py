import re 
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # s = "aabbbb"
        # p = ".*"

        #קראתי קצת וראיתי שהספרייה הזאת פשוט מחשבת ועושה את הבדיקה של החוקיות הרגולרית
        patern = re.compile(r'%s' %p)
        #ופה היא פשוט בודקת האם החוקיות תואמת את הביטוי הרגולרי
        match = patern.fullmatch(s)
        #אם יש התאמה, מחזירים "אמת" אחרת "שקר"
        if match : 
            return True 
        return False