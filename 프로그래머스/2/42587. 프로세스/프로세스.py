def solution(priorities, location):
    loc = []

    for _ in range(len(priorities)):

        for i in range(len(priorities)):
            if max(priorities) == priorities[i]:
                loc.append(i)
                priorities[i] = 0

            if len(loc) == len(priorities):        
                break

        if len(loc) == len(priorities):            
                break    
            
    return loc.index(location) + 1