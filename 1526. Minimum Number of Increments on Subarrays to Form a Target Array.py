# class Solution(object):
def minNumberOperations(target):
    """
    :type target: List[int]
    :rtype: int
    """
    
    #בשאלה הזאת צריך לדעת מה מספר הפעולות המינימלי להשגת מערך המטרה ממערך האפסים
    #מתחילים בליסכום אתהאיבר הראשון כהתחלה של פעולות מינימאליות שככה או ככה ניצטרך לעשות
    #ואז בודקים צמדים רודפים של איברים וסוכמים את ההפררש ביניהם רק במידה והאיבר הרודף גדול מהקודם לו
    #וכך אנחנו לא צריכים לבצע פעולה אלא רק לסכום הפרשים בין איברים
    #count = initial amount of operations 
    count = target[0]
    #יצירת שני מערכים מאותו סוג רק עם אינדקסים רודפים מכל מערך
    for i, j in zip(target, target[1:]):
        if i < j:
            #sums up the difference of 2 elements
            count += j - i
    return count

print(minNumberOperations([3,1,5,4,2]))