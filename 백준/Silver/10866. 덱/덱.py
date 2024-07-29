from collections import deque
import sys
input = sys.stdin.readline

d = deque()

input_iter = int(input())

for _ in range(input_iter):
    s = input().split()
    if s[0] == 'push_front':
        d.appendleft(s[1])
        
    if s[0] == 'push_back':
        d.append(s[1])
        
    if s[0] == 'pop_front':
        if len(d) == 0:
            print(-1)
            
        else:
            print(d.popleft())
            
    if s[0] == 'pop_back':
        if len(d) == 0:
            print(-1)
            
        else:
            print(d.pop())
            
    if s[0] == 'size':
        print(len(d))
        
    if s[0] == 'empty':
        print(0 if d else 1)
        
    if s[0] == 'front':
        if len(d) == 0:
            print(-1)
            
        else:
            print(d[0])
            
    if s[0] == 'back':
        if len(d) == 0:
            print(-1)
            
        else:
            print(d[-1])
        
        
