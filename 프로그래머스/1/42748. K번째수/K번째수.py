def solution(array, commands):
    answer = []
    for i,j,k in commands:
        i -= 1 
        j -= 1 
        k -= 1
        chopped = sorted(array[i:j+1])
        answer.append(chopped[k])
    return answer