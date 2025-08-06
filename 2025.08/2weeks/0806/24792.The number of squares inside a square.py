# 테스트 케이스 수 입력 받기
T = int(input())

# T번 만큼 테스트 케이스 반복
for tc in range(1, T + 1):
    # 각 테스트 케이스마다 N (전체 격자 크기), M (작은 정사각형 크기) 입력
    N, M = map(int, input().split())

    # N x N 격자판을 0으로 초기화
    matrix = [[0] * N for _ in range(N)]

    # 채워넣을 숫자를 1부터 시작
    number = 1

    # 작은 정사각형의 시작 위치는 (i, j)
    # 정사각형이 N x N 격자를 벗어나지 않게 하기 위해 N - M + 1 만큼만 반복
    for i in range(N - M + 1):  # 행 인덱스
        for j in range(N - M + 1):  # 열 인덱스

            # M x M 정사각형 채우기
            for r in range(M):  # 0부터 M-1까지 반복
                for c in range(M):  # 0부터 M-1까지 반복
                    matrix[i + r][j + c] = number  # 격자에 숫자 덮어쓰기

            number += 1  # 다음 정사각형에는 더 큰 숫자를 씀

    # 출력
    print(f"#{tc}")
    for row in matrix:
        print(*row)  # 리스트의 요소를 공백으로 구분하여 출력