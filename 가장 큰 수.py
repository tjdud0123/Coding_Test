def solution(numbers):
    
    num_dict = [str(x) for x in numbers]
    num_dict.sort(key = lambda x: (str(x)*4)[:4], reverse = True)
    
    return ''.join(num_dict) if num_dict[0] != '0' else '0'