T = int(input())

for t in range(1, T + 1):
    N = int(input())

    # 파스칼 삼각형 (N x N)
    arr = [[0] * N for _ in range(N)]

    # 첫 행 초기화
    arr[0][0] = 1

    # DP 점화식 채우기
    for i in range(1, N):
        arr[i][0] = 1  # 각 행의 첫 값은 1
        arr[i][i] = 1  # 각 행의 마지막 값은 1
        for j in range(1, i):  # 내부 값은 위 두 값의 합
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

    # 출력
    print(f'#{t}')
    for i in range(N):
        # 각 행 i는 0..i까지만 유효
        # 공백 규칙: 숫자 사이에만 한 칸, 행 끝에 공백 없음
        print(arr[i][0], end='')  # 첫 숫자 출력(앞 공백 없음)
        for j in range(1, i + 1):
            print(' ' + str(arr[i][j]), end='')  # 앞에 공백 추가 후 숫자
        print()  # 줄바꿈