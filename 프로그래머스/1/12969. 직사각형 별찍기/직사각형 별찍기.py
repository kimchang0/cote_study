import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().strip().split(' '))

for i in range(m):
    for j in range(n):
        print("*")
    print("\n")