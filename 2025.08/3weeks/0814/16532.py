T = int(input())


# 탐색 시작 좌표 si, sj

def dfs(si, sj):
    # 중복체크 배열도 2차원
    visited = [[0] * N for _ in range(N)]

    # x,y 를 탐색한적이 있다 => visited[x][y] = 1
    # x,y 를 탐색한적이 있다 => visited[w][z] = 0

    stack = []

    # 현재 탐색중인 위치
    vi, vj = si, sj

    visited[vi][vj] = 1

    while True:
        if maze[vi][vj] == 3:
            return 1

        # 현재 위치에서 나온 탐색
        # vi,vj 에서 갈 수 있는 다른 위치 찾기
        # ni,nj 다른위치
        # 4방향
        di = [-1, 1, 0, 0]
        dj = [0, 1, 0, -1]
        for d in range(4):
            ni = vi + di[d]
            nj = vj + dj[d]
            # 1. ni,nj 2차원배열안인지
            # 2 .실제로 갈 수 있다라고 표시된 곳인지
            # 3. 이전에 방문하였는지

            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and not visited[ni][nj]:
                # ni,nj로 이동할것이시 때문에 현재위치를 스택에 저장
                stack.append((vi, vj))
                visited[ni][nj] = 1
                vi, vj = ni, nj
                break

        else:
            # 중간에 브레이크 한적없다 갈수있는 방향이없다
            # 길이 없다는 것은 돌아가자
            # 어디로 돌아가는진 스택이알고있음
            if stack:
                vi.vj = stack.pop()
            else:
                break
    return 0


for t in range(1, T + 1):
    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]

    # 탐색 시작 좌표 si, sj
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j
                print(f'#{t} {dfs(si, sj)}')
