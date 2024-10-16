def solution(a, b):
    answer = []
    gcd_n_m = gcd(a, b)
    answer.append(gcd_n_m)
    answer.append(lcm(a, b, gcd_n_m))
    return answer

def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)
    
def lcm(n, m, gcd_n_m):
    return (n // gcd_n_m) * m