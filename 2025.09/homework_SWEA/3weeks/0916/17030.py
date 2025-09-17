# SWEA 스타일: 여러 테스트케이스 입력을 받아 각 케이스 결과를 "#tc 값" 형태로 출력합니다.
# 문제 성격상 모든 간선 가중치가 양수이므로 다익스트라 알고리즘을 사용합니다.

import heapq                # 우선순위 큐(최소 힙) 사용


T = int(input().strip())    # 테스트케이스 개수 입력

for tc in range(1, T + 1):  # 각 테스트케이스 처리 루프
    N_E = input().split()   # N과 E가 한 줄에 들어옴
    # 공백이 여러 개일 수 있으므로 split()만 사용하고 정수 변환을 직접 수행
    N = int(N_E[0])         # 마지막 연결지점 번호(N)
    E = int(N_E[1])         # 도로(간선) 개수(E)

    # 정점 수는 0 ~ N까지 총 N+1개
    graph = [[] for _ in range(N + 1)]  # 인접 리스트 생성

    # E개의 간선 정보를 입력받아 그래프 구성
    # 단방향 간선이므로 시작 s에서 끝 e로만 추가
    for _ in range(E):
        s_str, e_str, w_str = input().split()  # s, e, w를 문자열로 받음
        s = int(s_str)                         # 시작 정점
        e = int(e_str)                         # 도착 정점
        w = int(w_str)                         # 간선 가중치
        # 인접 리스트에 (가중치, 다음정점) 형태로 저장
        graph[s].append((w, e))

    # 다익스트라 준비: 거리 배열을 매우 큰 수로 초기화
    INF = 10**18                               # 충분히 큰 값
    dist = [INF] * (N + 1)                     # 0~N까지의 최단거리 저장
    dist[0] = 0                                # 출발점 0의 거리는 0

    # 우선순위 큐에는 (현재까지의 비용, 정점) 형태로 저장
    pq = []
    heapq.heappush(pq, (0, 0))                 # 시작 정점 0을 큐에 삽입

    # 다익스트라 메인 루프
    while pq:
        cur_cost, cur = heapq.heappop(pq)      # 가장 비용이 작은 정점 꺼내기

        # 이미 더 좋은 경로로 방문한 적이 있으면 스킵
        if cur_cost != dist[cur]:
            continue

        # 목표 정점 N에 도달했다면 더 진행할 필요가 없음
        # 양의 가중치 그래프에서 꺼낸 순간이 최단거리 확정
        if cur == N:
            break

        # 현재 정점에서 나가는 모든 간선을 살펴보며 갱신 시도
        edges = graph[cur]                     # 현재 정점의 인접 간선 목록
        # 파이썬 내장 min() 등을 쓰지 않고 단순 순회로 처리
        for w, nxt in edges:
            new_cost = cur_cost + w            # cur을 거쳐 nxt로 가는 비용
            # 더 짧은 경로를 찾으면 갱신하고 우선순위 큐에 삽입
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))

    # dist[N]이 갱신되지 않았다면 경로 없음으로 간주
    # 문제 조건상 보통 경로가 존재하지만 안전하게 처리
    ans = dist[N] if dist[N] != INF else -1

    # SWEA 출력 형식에 맞게 결과 출력
    print(f"#{tc} {ans}")
