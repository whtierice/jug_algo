def solution(clothes):
    answer = 1
    
    counter = {}
    
    for names, category in clothes:
        counter[category] = counter.get(category, 0) + 1
    
    print(counter)
    
    for count in counter.values():
        answer *= count + 1
        
    return answer - 1
        