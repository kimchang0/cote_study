def solution(arr):
    answer = 1
    for i in arr:
        answer = lcm(answer, i)

    return answer

def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)

def lcm(n, m):  
    return n // gcd(n, m) * m