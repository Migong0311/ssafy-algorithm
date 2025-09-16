T = int(input())  # 테스트 케이스 수 입력

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N: 학생 수, M: 쌍의 개수

    # 인접 리스트 생성 (1번 ~ N번 사용, 편의상 N+1 크기로)
    graph = [[] for _ in range(N + 1)]

    # M개의 쌍 입력 처리
    data = list(map(int, input().split()))
    for i in range(M):
        a, b = data[2 * i], data[2 * i + 1]  # 두 학생 번호
        graph[a].append(b)  # 양방향 그래프
        graph[b].append(a)

    visited = [0] * (N + 1)  # 방문 여부 배열


    # DFS 함수 정의
    def dfs(v):
        visited[v] = 1  # 현재 정점 방문 처리
        for nxt in graph[v]:  # 인접한 정점 탐색
            if not visited[nxt]:  # 아직 방문하지 않았다면
                dfs(nxt)  # 재귀 호출


    groups = 0  # 조 개수 카운트

    # 모든 정점을 돌면서 방문하지 않은 곳에서 DFS 시작
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)  # 새로운 연결 요소 탐색
            groups += 1  # 조 개수 증가

    # SWEA 형식 출력
    print(f"#{tc} {groups}")