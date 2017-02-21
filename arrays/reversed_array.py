# https://www.hackerrank.com/challenges/arrays-ds
# Given an array, A, of N integers, print each element in reverse order as a single line of space-separated integers.

n = int(input().strip())
arr = [int(arr_element) for arr_element in input().strip().split(' ')]

for i in range(len(arr)-1, -1, -1):
    print(str(arr[i]) + ' ', end='')

