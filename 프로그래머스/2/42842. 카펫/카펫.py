def solution(brown, yellow):
    a = 1
    b = - (brown / 2 + 2)
    c = brown + yellow

    d = b**2 - 4*a*c

    x1 = (-b + d ** 0.5) / (2*a)
    x2 = (-b - d ** 0.5) / (2*a)

    answer = []
    answer.append(int(x1))
    answer.append(int(x2))


    return answer