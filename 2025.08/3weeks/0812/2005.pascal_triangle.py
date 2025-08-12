T = int(input())
# 테스트 케이스 개수 입력

for t in range(1, T + 1):
    # 각 테스트 케이스 반복 (1번부터 T번까지)

    N = int(input())
    # 파스칼 삼각형의 크기 N 입력

    arr = [[0] * N for _ in range(N)]
    # N x N 크기의 2차원 배열 생성 (모두 0으로 초기화)
    # 파스칼 삼각형은 삼각형 형태지만 편의상 N x N 배열로 만든 뒤 필요한 값만 출력

    arr[0][0] = 1
    # 파스칼 삼각형의 첫 번째 값(맨 위 꼭짓점)은 항상 1

    for i in range(1, N):
        # 두 번째 행부터 마지막 행까지 순회
        for j in range(N):
            # 각 행의 열 순회
            if j == 0:
                # 첫 번째 열(맨 왼쪽)은 항상 1
                arr[i][j] = 1
            else:
                # 나머지는 위쪽 왼쪽 값과 위쪽 값의 합
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

    print(f'#{t}')
    # 테스트 케이스 번호 출력

    for k in range(N):
        # 파스칼 삼각형의 각 행 출력
        for l in range(N):
            # 해당 행의 열 순회
            if arr[k][l]:
                # 값이 0이 아닌 경우만 출력 (파스칼 삼각형 형태 유지)
                print(arr[k][l], end='')
        print()
