def solution(skill, skill_trees):
    answer = 0
    for sk in skill_trees:
        item = [ alpha for alpha in sk if alpha in skill ]
        if skill.startswith(''.join(item)):
            answer +=1
    return answer
