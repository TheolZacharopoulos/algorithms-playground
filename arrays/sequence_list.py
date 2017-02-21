# https://www.hackerrank.com/challenges/dynamic-array

N, Q = [int(a) for a in input().strip().split(' ')]

seq_list = [[] for _ in range(N)]
last_ans = 0

for _ in range(Q):
    query_type, x, y = [int(arr_temp) for arr_temp in input().strip().split(' ')]

    if query_type == 1:
        seq_list[(x ^ last_ans) % N].append(y)
    elif query_type == 2:
        seq = seq_list[(x ^ last_ans) % N]
        last_ans = seq[y % len(seq)]
        print(last_ans)
