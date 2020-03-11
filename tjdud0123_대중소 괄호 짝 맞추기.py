def solution(s):
    bracket = {'}':'{', ']':'[', ')':'('}
    stack = []
    
    for b in s:
        if not stack or b in bracket.values():
            stack.append(b)
        elif bracket[b] == stack[-1]:
            stack.pop()
        else:
            return False
            
    return not stack