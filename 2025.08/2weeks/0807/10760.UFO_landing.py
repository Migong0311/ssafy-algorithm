# import sys
#
# sys.stdin = open('input.txt', 'r')

T = int(input())
"""
구해야 하는 것
행열을 순회하면서 N값이하의 분포가 몇개인지 구하는 거임
단 4칸이상이 N값이하어야함
"""
for t in range(1, T + 1):
    N, M = map(int, input().split())  # N은 행 M은 열
    arr = [list(map(int, input().split())) for _ in range(N)]  # 지형정보 2차원
    cnt = 0  # 예비 후보지 개수

    # 8방향 탐색을 위한 델타
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]  # 행 변화
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]  # 열 변화

    for i in range(N):  # 모든 행
        for j in range(M):  # 모든 열열
            center = arr[i][j]  # 현재 착륙지 후보의 높이
            cnt_result = 0  # N값보다 낮은 개수

            for d in range(8):  # 8방향 모두확인
                ni = i + dx[d]  # 다음위치에 행
                nj = j + dy[d]  # 다음 위치에 열

                # 배열 범위 안에 있는 경우에만 확인
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] < center:
                        cnt_result += 1

                # 주변 8칸 중 4칸이상이 착률지보다 낮으면 예비후보지로 인정

            if cnt_result >= 4:
                cnt += 1

    print(f'#{t} {cnt}')
