def solution(n, words):
    answer = []
    people = {}
    for i in range(n):
        people[i] = words[i::n]
    
    cnt = 0
    idx = 0
    compare_set = set()
    compare_list = []
    last_eng = ''
    while True:
        if cnt < n:
            compare_set.add(people[cnt][idx])
            compare_list.append(people[cnt][idx])
            if len(compare_set) != len(compare_list) or not people[cnt][idx].startswith(last_eng):
                answer.append(cnt + 1)
                answer.append(idx + 1)
                break
            last_eng = people[cnt][idx][-1]
            cnt += 1
        else:
            cnt = 0
            idx += 1
            if len(people[cnt]) <= idx:
                break
        
    return answer if answer else [0,0]