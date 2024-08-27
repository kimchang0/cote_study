import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    
    # 컴퓨터의 번호는 1~10번까지이므로 마지막 자릿수에 대해 주기를 찾습니다.
    last_digit = a % 10
    
    # 0인 경우는 10번 컴퓨터가 마지막이 되므로 예외 처리
    if last_digit == 0:
        print(10)
        continue
    
    # 반복되는 주기를 구합니다.
    cycle = []
    for i in range(1, 11):
        next_digit = (last_digit ** i) % 10
        if next_digit in cycle:
            break
        cycle.append(next_digit)
    
    # b를 cycle의 길이로 나눈 나머지에 해당하는 컴퓨터 번호 출력
    print(cycle[(b - 1) % len(cycle)])
