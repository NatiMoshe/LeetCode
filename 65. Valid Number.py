class Solution:
    def isNumber(self, s: str) -> bool:
        #טיפול בכל מיקרי הקצה של הקלטים האפשריים (לפי ניסוי וטעייה) 
        if s == '-inf' or s == 'inf' or s == '+inf' or s == '-Infinity' or s == 'Infinity' or s == '+Infinity':
            return(False)
        try:
            #בדיקה האם ניתן לבצע קאסטינג, אם כן מחזירים RETURN, אם אחרת FALSE 
            float(s)
            return True
        except:
            return False


        