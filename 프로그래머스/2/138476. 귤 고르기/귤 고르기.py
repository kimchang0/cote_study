from collections import Counter
def solution(k, tangerine):
    answer = 1
    tangerine_count = dict(Counter(tangerine))
    classificationed_tangerine = sorted([i for i in tangerine_count.values()], reverse=True)
    for i in classificationed_tangerine:
        if k - i > 0:
            k -= i
            answer += 1
        else:
            break
        
    return answer