'''
16268. 풍선팡 노피티 ver.
'''
import sys
sys.stdin = open('input1.txt','r')
T = int(input())
for t in range(1, T + 1):
    # N : 새로 M : 가로
    N, M = map(int, input().split())
    # N줄에 걸친 꽃가루 개수
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 상하좌우
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 꽃가루 최대 값
    max_ball = 0


    # 각 위치에서 풍선을 터뜨렸을 때 날릴 수 있는 꽃가루 수를 계산하는 함수
    def ball_sum(r, c):
        # 시작위치의 꽃가루 수 포함
        total = arr[r][c]
        # 상하좌우 한 칸씩
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            # 격자 안에 있을때만
            if 0 <= nr < N and 0 <= nc < M:
                # 총 꽃가루 수 증가
                total += arr[nr][nc]
        # 꽃가루 수 반환
        return total

        # 최대 꽃가루 수 탐색


    for i in range(N):
        for j in range(M):
            plus_ball = ball_sum(i, j)
            result = max(max_ball, plus_ball)
    print(f'#{t} {result}')
