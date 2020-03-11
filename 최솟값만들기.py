def solution(A,B):
    answer = 0
    for x,y in zip(sorted(A),sorted(B, reverse = True)):
        answer += x*y
    return answer