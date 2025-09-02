'''
12712. 파리퇴치3
'''

# 테스트 케이스 수 입력
T = int(input())

# 각 테스트 케이스 처리
for t in range(1, T + 1):
    # N: 격자 크기, M: 스프레이 범위
    N, M = map(int, input().split())

    # 격자 정보 입력
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 방향 벡터 정의
    plus_dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]      # 상하좌우
    cross_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]   # 좌상향 우상향 좌하향 우하향


    # 최대 파리 퇴치 수 저장
    max_kill = 0

    # 함수: 특정 방향 기준으로 (r, c)에서 M칸만큼 영향 주는 파리 수 합
    def spray_sum(r, c, directions):
        total = grid[r][c]  # 시작점 포함
        for dr, dc in directions:
            for dist in range(1, M):  # M-1 칸 이동
                nr, nc = r + dr * dist, c + dc * dist
                if 0 <= nr < N and 0 <= nc < N:
                    total += grid[nr][nc]
        return total

    # 모든 칸에서 시도
    for i in range(N):
        for j in range(N):
            # + 형태
            plus_kill = spray_sum(i, j, plus_dirs)
            # x 형태
            cross_kill = spray_sum(i, j, cross_dirs)
            # 최댓값 갱신
            max_kill = max(max_kill, plus_kill, cross_kill)

    # 결과 출력
    print(f"#{t} {max_kill}")
