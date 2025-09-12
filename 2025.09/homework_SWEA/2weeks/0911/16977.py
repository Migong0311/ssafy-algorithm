'''
16977. 5일차 응용 - 전기버스2

최소 교체 횟수
0번 재외

'''

T = int(input())

for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    M = arr[N - 1]
    change_cnt = 0
    