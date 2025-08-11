import sys

sys.stdin = open('algo2_sample_in.txt', 'r')

T = int(input())  # 지도 개수 입력

for t in range(1, T + 1):
    N, M = map(int, input().split())  # 지도의 크기 입력
    arr = [list(map(int, input().split())) for _ in range(N)]  # 지도의 N*M 크기의 배열 입력

    max_high = 0  # 가장 높은 지역 초기화
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(N):
        for j in range(M):
            is_safe = True

            for d in range(4):
                # 움직인 행  = 현재+ d방향i변화량
                ni = i + di[d]
                # 움직인 열  = 현재+ d방향 j변화량
                nj = j + dj[d]

                if 0 <= ni < N and 0 <= nj < M:
                    if arr[i][j] <= arr[ni][nj]:
                        is_safe = False
                else:
                    is_safe = False
            if is_safe:
                max_high += 1
    print(f'{t} {max_high}')
