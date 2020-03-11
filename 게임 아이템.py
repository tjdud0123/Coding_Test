import heapq
from collections import deque

def solution(healths, items):
    healths.sort()
    items = [(*item,index) for index, item in enumerate(items, 1)]
    ATTACK, HP, IDX = 0, 1, 2
    items = deque(sorted(items, key= lambda x:x[HP]))
    
    answer = []
    cand = []
    for health in healths:
        while items and health - items[0][HP] >= 100:
            item = items.popleft()
            heapq.heappush(cand, (-item[ATTACK], item[IDX]))
        if cand:
            answer.append(heapq.heappop(cand)[1])
    return sorted(answer)
            
    
    