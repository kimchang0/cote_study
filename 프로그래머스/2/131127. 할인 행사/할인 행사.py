def solution(want, number, discount):
    answer = 0
    want_zip = {i: k for i, k in zip(want, number)}
    idx = 0
    while True:
        temp = discount[idx : idx + 10]
        temp_want_zip = want_zip.copy()
        if len(temp) < 10:
            break
        
        for i in temp:
            if temp_want_zip.get(i) != None and temp_want_zip.get(i) != 0:
                temp_want_zip[i] -= 1
                
        if sum(temp_want_zip.values()) == 0:
            answer += 1
        idx += 1
            
    return answer