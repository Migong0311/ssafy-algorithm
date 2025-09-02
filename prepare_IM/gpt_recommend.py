# 테스트 케이스 수 입력
T = int(input().strip())

for tc in range(1, T + 1):                  # 1부터 T까지
    N, M = map(int, input().split())        # 격자 크기
    board = [list(map(int, input().split())) for _ in range(N)]  # 격자 값

    # 상하좌우 델타(순서는 결과에 영향 없음: 단순 합산 문제)
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    best = 0                                # 최대 점수

    # 모든 칸을 시작점 후보로 시도
    for i in range(N):                      # 행 순회
        for j in range(M):                  # 열 순회
            k = board[i][j]                 # 폭죽의 거리(해당 칸 값)
            total = board[i][j]             # 본인 칸 점수 포함

            # 거리 d=1..k에 대해 상하좌우로 더함
            for d in range(1, k + 1):       # 거리 1부터 k까지
                for dir in range(4):        # 4방향
                    ni = i + di[dir] * d    # d칸 떨어진 행
                    nj = j + dj[dir] * d    # d칸 떨어진 열
                    if 0 <= ni < N and 0 <= nj < M:  # 격자 내부만
                        total += board[ni][nj]       # 점수 누적

            # 최대값 갱신
            if total > best:
                best = total

    # 형식에 맞게 출력
    print(f"#{tc} {best}")
