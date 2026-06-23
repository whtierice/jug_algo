def solution(clothes):
    answer = 1
    
    cloth_counts = {}
    
    for name, category in clothes:
        cloth_counts[category] = cloth_counts.get(category, 0) + 1
        
    for count in cloth_counts.values():
        answer *= count + 1
        
    return answer - 1