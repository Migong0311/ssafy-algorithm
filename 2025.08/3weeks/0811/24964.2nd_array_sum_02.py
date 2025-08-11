import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    arr_sum = 0
    for i in range(M):
        for j in range(N):
            arr_sum += arr[j][i]

    print(f'#{t} {arr_sum}')
