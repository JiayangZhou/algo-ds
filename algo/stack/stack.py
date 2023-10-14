# https://leetcode.com/problems/valid-parentheses/
def isValid(self, s: str) -> bool:
    d = {'(':')', '{':'}','[':']'}
    stack = []
    for _ in s:
        if _ in d:  
            stack.append(_)
        else:
            if not stack:
                return False
            last = stack.pop()
            if last not in d:
                return False
            if d[last] != _:
                return False
    return len(stack) == 0