def solution(array, commands):
    answer = []
    
    for i,j,k in commands:
        sorted_array = sorted(array[i-1:j])
        
        
        answer.append(sorted_array[k-1])
    return answer