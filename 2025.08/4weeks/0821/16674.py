import sys

# 로컬 테스트 시 입력 파일을 표준 입력으로 연결 (온라인 저지에서는 제거해도 무방)
sys.stdin = open('input.txt', 'r')

"""
16674. 미로의 거리
- NxN 미로에서 2(출발) -> 3(도착)까지의 최소 이동 칸 수를 구한다.
- 이동은 상/하/좌/우 4방향만 가능, 1은 벽, 0은 통로.
- 경로가 없으면 0을 출력한다.
"""
# BFS 설계 메모
# visited 생성
# 큐 생성, 시작점 인큐
# 인큐 표시
# 반복
#     디큐
#     방문해서 할 일(목적지 검사 등)
#     방문 정점에 인접하고 미방문이면
#         인큐
#         인큐 표시


def find_start(N):
    """미로(전역 변수 maze)에서 값이 2인 출발 좌표를 찾아 (i, j)로 반환한다.
    M: 미로 한 변의 길이(N)"""
    for i in range(N):               # 모든 행을 돌면서
        for j in range(N):           # 해당 행의 모든 열을 확인
            if maze[i][j] == 2:      # 셀이 2(출발)이면
                return i, j          # 그 좌표를 즉시 반환


def bfs(i, j, N):
    """시작 좌표 (i, j)에서 BFS로 최단 칸 수를 구해 반환한다.
    - visited에는 '시작으로부터의 거리 + 1'을 기록
      예: 시작칸=1, 시작 인접칸=2, ... 도착칸=k 이면 실제 이동 칸 수는 k-2
    - 경로가 없으면 0 반환
    """
    visited = [[0] * N for _ in range(N)]  # 방문 및 거리 기록용 2차원 배열(0은 미방문)
    q = [[i, j]]                           # 큐 초기화 (시작 좌표 인큐)
    visited[i][j] = 1                      # 시작칸 방문 표시 및 거리=1로 설정

    while q:                               # 큐에 탐색할 좌표가 남아 있는 동안 반복
        ti, tj = q.pop(0)                  # 디큐: 현재 좌표를 하나 꺼냄
        if maze[ti][tj] == 3:              # 현재 칸이 도착(3)이면
            return visited[ti][tj] - 2     # 실제 이동 칸 수 = 기록값 - 2 (시작,도착 제외)

        # 상하좌우 4방향으로 이웃 좌표 탐색
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            wi, wj = ti + di, tj + dj      # 이웃 좌표 계산
            # 경계 내, 벽(1) 아님, 미방문(visited==0)인 경우에만 진행
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])                         # 인큐
                visited[wi][wj] = visited[ti][tj] + 1      # 거리 기록(부모+1)

    return 0                                # 큐 소진까지 도착을 못 찾으면 경로 없음 -> 0 반환


T = int(input())

for t in range(1, T + 1):
    N = int(input().strip())                # 미로 한 변의 길이 N

    # 미로 입력: 각 줄은 공백 없이 숫자들로 주어짐 → 각 글자를 int로 변환하여 리스트화
    maze = [list(map(int, input().strip())) for _ in range(N)]

    sti, stj = find_start(N)  # 출발 좌표(2) 탐색
    ans = bfs(sti, stj, N)                  # BFS로 최단 칸 수 계산

    print(f"#{t} {ans}")                    # 문제 요구 형식대로 출력: #T 결과

# 출력
# #1 5
# #2 5
# #3 0
