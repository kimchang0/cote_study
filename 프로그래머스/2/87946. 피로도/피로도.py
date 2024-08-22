from itertools import permutations
def solution(k, dungeons):
    answer = []
    
    for i in permutations(dungeons, len(dungeons)):
        temp = k
        cnt = 0
        for need_num, deducted_num in i:
            if temp >= need_num:
                temp -= deducted_num
                cnt += 1
        answer.append(cnt)
    
    return max(answer)