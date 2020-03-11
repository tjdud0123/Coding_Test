def solution(d, budget):
    d.sort(reverse = True)
    answer = 0
    while d and budget >= d[-1]:
        budget -= d.pop()
        answer +=1
    return answer