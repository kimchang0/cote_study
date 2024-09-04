import sys
import heapq
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().strip().split())
trees = list(map(int, input().strip().split()))
start = 0
end = heapq.nlargest(1, trees)[0]
result = 0
while start <= end:
	total = 0
	mid = (start + end) // 2
	for i in trees:
		if i > mid:
			total += i-mid
	if total < m:
		end = mid -1
	else:
		result = mid
		start = mid +1
print(str(result))