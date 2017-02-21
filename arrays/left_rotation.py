# https://www.hackerrank.com/challenges/array-left-rotation

N, d = [int(a) for a in input().strip().split(' ')]

arr = [0] * N

input_arr = [int(elem) for elem in input().strip().split(' ')]

for i in range(N):
    arr[((i-d) % N)] = input_arr[i]

for i in range(N):
    print(str(arr[i]) + " ", end='')

