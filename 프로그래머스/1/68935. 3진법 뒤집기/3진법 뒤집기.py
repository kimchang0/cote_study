def solution(n):
    return int(''.join([i for i in decimal_to_ternary(n)]), 3)

def decimal_to_ternary(n):
    if n == 0:
        return "0"
    
    ternary = ""
    while n > 0:
        remainder = n % 3
        ternary = str(remainder) + ternary
        n = n // 3
    
    return reversed(ternary)