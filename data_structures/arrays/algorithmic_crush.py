# https://www.hackerrank.com/challenges/crush

N, M = [int(a) for a in input().strip().split(' ')]

arr = [0] * (N + 1)

for _ in range(M):
    a, b, k = [int(elem) for elem in input().strip().split(' ')]
    arr[a - 1] += k
    if b <= len(arr):
        arr[b] -= k

max_num = float('-inf')
arr_sum = 0
for i in arr:
    arr_sum += i
    max_num = max(max_num, arr_sum)

print(max_num)
