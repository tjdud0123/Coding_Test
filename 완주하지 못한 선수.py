def solution(participant, completion):
    num_dict = {}
    
    for parti in participant:
        num_dict[parti] = num_dict.get(parti, 0) + 1
        
    for comple in completion:
        num_dict[comple] -= 1
        
    return sorted(num_dict.items(), key = lambda x:x[1]).pop()[0]