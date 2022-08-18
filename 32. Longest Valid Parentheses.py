# class Solution:
#     def longestValidParentheses(self, s: str) -> int:





# Whenever we see a new open parenthesis, we push the current longest streak to the stack. 
# Whenever we see a close parenthesis, 
# If there is no matching open parenthesis for a close parenthesis, 
#     reset the current count.
# else:
#     we pop the top value, and add the value (which was the previous longest streak up to that point) 
#     to the current one (because they are now contiguous) 
#     and add 2 to count for the matching open and close parenthesis. 

def longestValidParentheses(s):
    count = 0
    stack = [-1]
    for i, char in enumerate(s):
        if char == '(':
            #save previous streak 
            stack.append(i)
        elif char == ')':
            #poping from stack if
            if len(stack)>1 and s[stack[-1]] == '(':
                stack.pop()
                #saving streak
                count = max(count,(i-stack[-1]))
            else:
                #invalid parenthesis
                stack.append(i)
            
    return count
    
print(longestValidParentheses("(()()()"))