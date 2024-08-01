from collections import deque
def solution(people, limit):
    answer = 0
    
    d = deque(sorted(people, reverse=True))
    while(len(d) != 0):
        l = d.popleft()
        if len(d) == 0:
            answer += 1
            break
        r = d.pop()
            
        if l + r > limit:
            d.append(r)
            answer += 1
        else:
            answer += 1
        
    return answer