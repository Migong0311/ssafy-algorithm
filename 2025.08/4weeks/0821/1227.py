import sys

sys.stdin = open('input.txt', 'r')

"""
1226. 미로 2
입력 형식: 테스트케이스 번호 1줄 + 100줄의 미로(문자열) * 10세트
출력 형식: #<tc> <정답(가능:1, 불가:0)>
"""
from collections import deque  # BFS 큐로 사용할 deque 임포트

for _ in range(10):
    tc = int(input())

    maze = []  # 100x100 미로를 저장할 리스트
    start = 0  # 시작 좌표(값 2)의 위치를 저장할 변수 (y, x)
    goal = 0  # 도착 좌표(값 3)의 위치를 저장할 변수 (y, x)

    # 16줄을 읽어 미로 구성
    for y in range(100):
        line = input()
        row = [int(ch) for ch in line]  # 각 문자를 정수로 변환하여 리스트로 저장
        maze.append(row)  # 미로에 한 행 추가

        # 이 행에서 시작점(2)와 도착점(3)을 찾으면 좌표 저장
        # -> 입력 예시마다 2와 3의 위치가 다를 수 있으므로 동적 탐색
        if 2 in row:
            start = (y, row.index(2))  # (행=y, 열=x)
        if 3 in row:
            goal = (y, row.index(3))  # (행=y, 열=x)

    # 방문 여부를 기록할 100 * 100 배열
    visited = [[0] * 100 for _ in range(100)]

    # 상, 하, 좌, 우 네 방향 이동 벡터 (dy, dx)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # BFS를 위한 큐 초기화 및 시작점 인큐
    q = deque()
    sy, sx = start  # 시작 좌표 분해
    q.append((sy, sx))  # 시작 좌표 넣기
    visited[sy][sx] = True  # 시작점 방문 표시

    # 도달 가능 여부
    is_reach = 0

    # BFS 루프
    while q:
        y, x = q.popleft()  # 현재 위치 디큐

        # 현재 위치가 도착점이면 탐색 종료 및 성공 처리
        if (y, x) == goal:
            is_reach = 1
            break

        # 4방향으로 인접 칸 탐색
        for d in range(4):
            ny = y + dy[d]  # 다음 행
            nx = x + dx[d]  # 다음 열

            # 범위를 벗어나면 스킵
            if not (0 <= ny < 100 and 0 <= nx < 100):
                continue

            # 다음 행렬이 벽(1)일경우 통과 불가 -> 스킵
            if maze[ny][nx] == 1:
                continue

            # 아직 방문하지 않은 길(0) 또는 도착점(3)이라면 방문
            if not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))

    # 형식에 맞게 결과 출력
    print(f"#{tc} {is_reach}")
    """
    출력
    #1 1
    #2 1
    #3 1
    #4 0
    #5 1
    #6 1
    #7 0
    #8 1
    #9 1
    #10 1
    """
