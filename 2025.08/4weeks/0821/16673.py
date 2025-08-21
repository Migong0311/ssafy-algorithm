from collections import deque

"""
16673. 노드의 거리

- 무방향 그래프에서 두 노드 S, G 사이의 최단 경로(간선 개수)를 구하는 문제
- BFS를 사용하면 최단 간선 수를 쉽게 구할 수 있음
- 두 노드가 연결되어 있지 않다면 0을 출력
"""

# -------------------------------
# BFS 함수 정의
# -------------------------------
def bfs():
    visited = [0] * (V + 1)      # 방문 여부와 시작점으로부터의 거리 기록 (노드 번호 1~V)
    q = deque()                  # BFS용 큐 생성
    q.append(S)                  # 시작 노드를 큐에 삽입
    visited[S] = 1               # 시작 노드 방문 표시(거리=1로 시작)

    while q:                     # 큐가 빌 때까지 반복
        v = q.popleft()          # 현재 탐색할 노드를 큐에서 꺼냄

        if v == G:               # 목표 노드에 도착했으면
            return visited[G] - 1  # 실제 간선 수 = 거리-1 (시작을 1로 잡았기 때문)

        # 현재 노드와 연결된 모든 인접 노드 확인
        for nv in adj[v]:
            if not visited[nv]:               # 아직 방문하지 않은 노드라면
                q.append(nv)                  # 큐에 넣고
                visited[nv] = visited[v] + 1  # 현재 노드 거리 + 1로 갱신
    return 0                     # 큐를 다 돌았는데 목표 G를 못 찾으면 0 반환


# -------------------------------
# 메인 루프: 테스트케이스 처리
# -------------------------------
T = int(input())                 # 테스트케이스 개수 입력

for t in range(1, T + 1):
    V, E = map(int, input().split())     # V: 노드 수, E: 간선 수

    # 인접 리스트 초기화 (1번 노드부터 V번 노드까지)
    adj = [[] for _ in range(V + 1)]

    # E개의 간선 정보 입력
    for i in range(E):
        s, e = map(int, input().split())  # 간선 양 끝 노드
        adj[s].append(e)                  # 무방향 그래프이므로 양쪽 다 연결
        adj[e].append(s)

    # 출발 노드 S, 도착 노드 G 입력
    S, G = map(int, input().split())

    # BFS 실행 후 결과 저장
    answer = bfs()

    # 출력 형식: #테스트케이스번호 결과
    print(f'#{t} {answer}')