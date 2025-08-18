"""
24446. 공굴리기 게임
출처 : https://buly.kr/Yf30fR
"""

T = int(input())

for t in range(1, T + 1):
    N = int(input())  # N * N 배열 설정
    arr = [list(map(int, input().split())) for _ in range(N)]  # 배열 입력

    # dp[r][c] = (r,c)에서 시작했을 때 방문 칸 수(시작 포함)
    dp = [[0] * N for _ in range(N)]

    # 상,하,좌,우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]


    def pick_next(r, c):
        """
        (r,c)에서 규칙에 맞는 다음 좌표를 고른다.
        - 현재 값보다 작은 이웃 중 최솟값
        - 동점이면 상,하,좌,우 우선
        - 없으면 None
        :param r: 가로 좌표값
        :param c: 새로 좌표값
        :return: default None
        """
        curr = arr[r][c]  # 현재 시작점 기준

        # 먼저 네 이웃 중 현재보다 작은 값들의 최소값을 찾는다
        min_v = 10 ** 9
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]  # r,c에서 4방향으로 한 칸 이동한 죄표 계산
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] < curr:
                # 이동한 죄표가 격자판 범위 안에 있고 현재 칸 값보다 더 작은 값일 때만 확인
                if arr[nr][nc] < min_v:
                    min_v = arr[nr][nc]  # 지금까지 찾은 후보 중 가장 작은 값을 갱신
        if min_v == 10 ** 9:
            return None  # 네 방향 중 더 작은 칸이 없으면 이동불가로 None반환
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]  # 다시 네 방향 좌표 계산
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == min_v:
                # 최소값과 같은 칸을 만나면 그 좌표룰 반환
                return nr, nc
        return None


    # 모든 칸을 값 오른차순 정렬
    cells = [(arr[r][c], r, c) for r in range(N) for c in range(N)]
    for i in range(len(cells)): # 선택정렬로 최소값부터 정렬
        min_idx = i
        for j in range(i + 1, len(cells)):
            if cells[j][0] < cells[min_idx][0]:
                min_idx = j
        cells[i], cells[min_idx] = cells[min_idx], cells[i]  # 값이 작은 칸부터 처리

    # 작은 칸부터 dp채우기

    for _, r, c in cells:
        nxt = pick_next(r, c)
        if nxt is None:
            dp[r][c] = 1
        else:
            nr, nc = nxt
            # nxt는 항상 더 작은 값이므로 이미 dp[nr][nc]가 계산되어 있음음
            dp[r][c] = 1 + dp[nr][nc]
        # 최대 방문 칸 수 계산
    ans = 0
    for r in range(N):
        for c in range(N):
            if dp[r][c] > ans:
                ans = dp[r][c]

    print(f"#{t} {ans}")
