# 최소 연료로 목적지까지 이동하는 문제
# 규칙: 상하좌우로만 이동 가능
# 한 칸 이동 기본 비용 1
# 더 높은 칸으로 이동할 경우 (높이차)만큼 추가 비용 발생
# 가중치가 양수이므로 다익스트라 알고리즘 사용

import heapq        # 우선순위 큐 구현용


T = int(input().strip())    # 테스트케이스 개수

for tc in range(1, T + 1):  # 각 테스트케이스 처리 루프
    N = int(input().strip())        # 격자 한 변의 길이 N (N x N)
    # 높이 정보를 2차원 리스트로 입력
    H = [list(map(int, input().split())) for _ in range(N)]

    # 다익스트라를 위한 거리(비용) 배열 초기화
    INF = 10**18                                # 매우 큰 값
    dist = [[INF] * N for _ in range(N)]        # 각 칸까지의 최소 비용
    dist[0][0] = 0                               # 시작점 (0,0) 비용 0

    # 우선순위 큐에는 (현재까지 비용, 행, 열) 저장
    pq = []
    heapq.heappush(pq, (0, 0, 0))                # 시작점 푸시

    # 4방향 이동 벡터 (상 하 좌 우)
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 다익스트라 메인 루프
    while pq:
        cost, i, j = heapq.heappop(pq)          # 가장 비용이 작은 칸 꺼내기

        # 이미 더 좋은 경로가 있으면 건너뜀
        if cost != dist[i][j]:
            continue

        # 목적지에 도달하면 조기 종료 가능
        if i == N - 1 and j == N - 1:
            break

        # 4방향 이웃 탐색
        for d in range(4):
            ni = i + di[d]                      # 다음 행
            nj = j + dj[d]                      # 다음 열

            # 격자 범위를 벗어나면 무시
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue

            # 기본 이동 비용 1
            base = 1

            # 높이 차가 양수일 때만 추가 연료 발생
            diff = H[ni][nj] - H[i][j]          # 다음 칸 높이 - 현재 칸 높이
            extra = diff if diff > 0 else 0     # 음수면 0 처리

            # 후보 비용 계산
            new_cost = cost + base + extra

            # 더 짧은 경로를 찾았으면 갱신하고 큐에 삽입
            if new_cost < dist[ni][nj]:
                dist[ni][nj] = new_cost
                heapq.heappush(pq, (new_cost, ni, nj))

    # 최종 답은 도착지 (N-1, N-1)의 최소 비용
    ans = dist[N - 1][N - 1]

    # SWEA 형식 출력
    print(f"#{tc} {ans}")
