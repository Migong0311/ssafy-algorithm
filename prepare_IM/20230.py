"""
20230. 풍선팡 보너스게임 2
출처 : https://buly.kr/3CORget
"""


# 입력: 스테이지 개수 T
T = int(input())

for t in range(1, T + 1):
    # 격자 크기 N
    N = int(input())
    # 격자판 입력
    board = [list(map(int, input().split())) for _ in range(N)]

    # 각 행의 합
    row_sum = [sum(board[r]) for r in range(N)]

    # 각 열의 합
    col_sum = [0] * N
    for c in range(N):
        s = 0
        for r in range(N):
            s += board[r][c]
        col_sum[c] = s

    # 모든 칸 점수 중 최대값 찾기
    max_score = -10**9
    for r in range(N):
        for c in range(N):
            # 점수 = 해당 행 합 + 해당 열 합 - 중복된 교차 칸
            score = row_sum[r] + col_sum[c] - board[r][c]

            if score > max_score:
                max_score = score

    # 최대 점수를 출력
    print(f"#{t} {max_score}")
