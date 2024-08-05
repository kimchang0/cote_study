def solution(nums):
    answer = 0
    nums_dict = {i: 0 for i in nums}
    for i in nums:
        nums_dict[i] += 1
    
    for i in set(nums):
        if nums_dict.get(i, 0) != 0:
            nums_dict[i] -= 0
            answer += 1
            
    return answer if len(nums) // 2 > answer else len(nums) // 2