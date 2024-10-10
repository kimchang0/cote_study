def solution(x, n):
    answer = []
    i = x
    while 1:
        if n == 0:
            return answer
        answer.append(i)
        i += x
        n -= 1