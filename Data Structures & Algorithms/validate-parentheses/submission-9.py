class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '[' or char == '{' or char == '(':
                stack.append(char)
            else:
                if stack:
                    if char == ']':
                        if stack.pop() != '[':
                            return False
                    elif char == '}':
                        if stack.pop() != '{':
                            return False
                    else:
                        if stack.pop() != '(':
                            return False
                else:
                    return False
        if not stack:
            return True
        return False
    

# we can iterate through the string and for every open parentheses, push it on to the
# stack and for every closed parentheses we can pop. 


