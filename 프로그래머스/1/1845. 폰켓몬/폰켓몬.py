def solution(nums):
    answer = 0
    
    nums_set = set(nums)
    
    if len(nums) // 2 <= len(nums_set):
        return len(nums) // 2
     
    
    return len(nums_set)