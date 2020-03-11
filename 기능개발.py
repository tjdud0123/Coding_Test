import math
from collections import deque

def solution(progresses, speeds):
    temp = map(lambda a,b:(100-a)/b, progresses,speeds)
    days = deque([math.ceil(num) for num in list(temp)])
    
    cur_func = days.popleft()
    count = 1
    answer = []
    while days:
        if cur_func >= days[0]:
            days.popleft()
            count += 1
        else:
            answer.append(count)
            cur_func = days.popleft()
            count = 1
    answer.append(count)
            
    return answer