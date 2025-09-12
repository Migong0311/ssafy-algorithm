"""
종이 꽃가루가 들어있는 풍선이 NxM 크기의 격자판에 붙어있는데, 어떤 풍선을 터뜨리면 상하좌우의 풍선이 추가로 터진다고 한다.
다음의 경우 가운데 풍선을 터뜨리면 상하좌우의 풍선이 추가로 1개씩 터지면서 총 5개의 꽃가루가 날리게 된다.
NxM개의 풍선에 들어있는 종이 꽃가루 개수A가 주어지면,
한 개의 풍선을 선택해 터뜨렸을 때 날릴 수 있는 꽃가루 수 중 최대값을 출력하는 프로그램을 만드시오.
"""
# import sys
#
# sys.stdin = open('input.txt', 'r')
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())  # N * M 격자 만들기
    A = [list(map(int, input().split())) for _ in range(N)]  # 꽃가루 개수 A개

    plus_dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 상하좌우

    max_ball = 0 # 최대로 날릴 수 있는 꽃가루 수 초기화

    # 각 위치에서 풍선을 터뜨렸을 때 날릴 수 있는 꽃가루 수를 계산
    def ball_sum(r, c):
        total = A[r][c]  # 시작위치 (answer,j) 의 꽃가루 수 포함
        for dr,dc in plus_dirs:  # 상,하,좌,우 한칸씩
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:# 격자안에있을때만
                total += A[nr][nc] # 증가

        return total # 꽃가루 수 합 리턴
# 모든 격자 위치 순회 최대 꽃가루수 찾기
    for i in range(N):
        for j in range(M):
            plus_ball = ball_sum(i, j)
            max_ball = max(max_ball, plus_ball)
    print(f"#{t} {max_ball}")

# 1 8
# 2 16
# 3 17
