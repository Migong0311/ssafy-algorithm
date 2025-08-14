T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())  # v는 정점 E는 간선

    # 연결정보 인접행렬 or 리스트
    adjM = [[0] * (V + 1) for _ in range(V + 1)]
    # 간선정보가 E개
    for i in range(E):
        # s에서 e로 가는 길이 있다. 역방향 없음(유향그래프)
        s, e = map(int, input().split())

        adjM[s][e] = 1  # e,s는 없음

        # 출발 정점 s와 목표 정점 g
        s, g = map(int, input().split())

        # 문제에서 원하는 답 : s에서 출발해서 G로 갈 수 있는가
        # 일단 못간다 라고 가정하고 탐색중에 g를 만나면 가능하다고 고칠것이다
        answer = 0

        # DFS
        visited = [0] * (V + 1)

        # stack
        stack = []

        # 시작지점은 방문했다거 처리
        # 현재 위치를 v라고 했을떄 s에서 탐색 시작
        v = s
        visited[s] = 1

        while True:
            # 현재 위치가 도착지점 g인가?
            if v == g:
                # s에서 g로 가는길 발견
                answer = 1
                break
            # 현재 정점 v에서 방문가능한 다음정점mv 탐색
            for mv in range(1, v + 1):
                # mv 정점이 v와 인접해있고 이전에 방문한 적 없어야 갈 수 있다
                if adjM[v][mv] == i and visited[mv] == 0:
                    # mv정점은 갈 수있다
                    # 현재 정점 v를 스택에 저장
                    stack.append(v)
                    # mv는 방문했다고 표시
                    visited[mv] = 1
                    # mv로 이동
                    # 현재 위치v를 mv로이동
                    v = mv
                    # 이동했으니 다른 정점탐색 x
                    break
                else:
                    # 갈 수 있는 정점 mv를 발견 못할시
                    # 스택에서 돌아갈 위치를 하나 꺼내서 현재위치 변경
                    # 스택이 비어있는지?
                    if stack:
                        v = stack.pop()
                    else:
                        # 스택이 비어있다 = 갈수있는곳도 돌아갈곳도 없다 즉 탐색종료
                        break
        print(f'#{t} {answer}')