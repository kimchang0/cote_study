def solution(n):
    return int(((n ** 0.5) + 1) * ((n ** 0.5) + 1)) if n == int(n ** 0.5) * int(n ** 0.5) else -1