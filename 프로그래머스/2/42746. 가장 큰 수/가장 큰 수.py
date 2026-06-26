from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

def solution(numbers):
    answer = ''
    
    str_numbers = [str(n) for n in numbers]
    
    str_numbers.sort(key = cmp_to_key(compare))
    
    answer = ''.join(str_numbers)
    
    if answer[0] == "0":
        return "0"
    
    return answer