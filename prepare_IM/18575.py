"""
18575 풍선팡 보너스 게임
출처 : https://buly.kr/CB55i4k
"""
# 입력 첫 줄: 스테이지 개수 T
T = int(input())

# 각 스테이지에 대해 반복
for t in range(1, T + 1):
    # 격자 크기 N 입력
    N = int(input())
    # 격자 값 입력(정수 N줄)
    board = [list(map(int, input().split())) for _ in range(N)]

    # 각 행의 합을 미리 계산하여 저장
    row_sum = [sum(board[r]) for r in range(N)]

    # 각 열의 합을 미리 계산하여 저장
    col_sum = [0] * N
    for c in range(N):
        s = 0
        for r in range(N):
            s += board[r][c]
        col_sum[c] = s

    # 모든 칸을 한 번씩 보며
    # 해당 칸을 터뜨렸을 때의 점수(같은 행과 열의 풍선 합)를 계산
    # 점수의 최댓값과 최솟값을 동시에 갱신
    max_score = -10**9   # 충분히 작은 값으로 초기화
    min_score =  10**9   # 충분히 큰 값으로 초기화

    for r in range(N):
        for c in range(N):
            # 점수 = 해당 행 합 + 해당 열 합 - 교차 칸 값
            # 교차 칸 값은 행 합과 열 합에 모두 포함되어 두 번 더해졌으므로 한 번 빼줌
            score = row_sum[r] + col_sum[c] - board[r][c]

            # 최댓값 갱신
            if score > max_score:
                max_score = score
            # 최솟값 갱신
            if score < min_score:
                min_score = score

    # 같은 배치를 두 번 사용하므로
    # 첫 번째는 높은 점수를, 두 번째는 낮은 점수를 고르면
    # 최대 점수 차 = 최댓값 - 최솟값
    answer = max_score - min_score

    # 형식에 맞추어 출력
    print(f"#{t} {answer}")
