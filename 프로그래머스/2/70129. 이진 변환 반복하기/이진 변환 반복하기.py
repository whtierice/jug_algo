def finder(x):
    if x == "1":
        return False
    else:
        return True

def solution(s):
    answer = 0
    countt = 0
    while (finder(s)):
        countt += 1
        count = 0
        for i in range(len(s)):
            if s[i] == "1":
                count += 1
        answer += len(s) - count
        
        s = ""
        
        for i in range(count):
            s = bin(count)[2:]
        
        
    
        
    return [countt, answer]