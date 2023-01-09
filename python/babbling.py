from itertools import permutations
def solution(babbling):
    answer = 0
    arr = []
    
    for num in range(1, 5):
        for i in permutations(["aya", "ye", "woo", "ma"], num):
            arr.append(''.join(list(i)))
    
    for i in arr:
        answer += babbling.count(i)

    return answer