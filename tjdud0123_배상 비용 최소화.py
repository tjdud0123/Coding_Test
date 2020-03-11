import heapq

def solution(no, works):
    works = [-x for x in works] 
    heapq.heapify(works)
    
    for _ in range(no):
        if works[0] == 0:
            return 0
        else:
            heapq.heappush(works, heapq.heappop(works) + 1)

    return sum([x*x for x in works])