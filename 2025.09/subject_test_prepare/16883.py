import sys
sys.stdin = open('test.txt','r')

'''
16883. 2일차 응용 - 최소 합
'''
delta = [(0, 1), (1, 0)]
T = int(input())


# 현재위치 (answer,j) (행,열)
# (0,0) -> 우or하 이동 반복 -> (N-1.N-1)
def solve(i, j, now):
    global min_sum, N, arr
    #  가지치기
    if now >= min_sum:
        return

        # 종료 - 도착점(N-1,N-1)
    if i == N - 1 and j == N - 1:
        if now < min_sum:
            min_sum = now  # 최소값일경우 갱신

        return
        # 재귀적으로 우하단 탐색
    for di, dj in delta:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N:
            solve(ni, nj, now + arr[ni][nj])


for t in range(1, T + 1):
    N = int(input())  # 한변의 길이

    # N * N
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 문제에서 원하는 답 : 합이 최소가 되도록
    min_sum = 10 ** 9

    # 시작점(0,0)에서 탐색
    solve(0,0,arr[0][0])

    print(f'#{t} {min_sum}')