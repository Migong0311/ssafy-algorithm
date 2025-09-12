"""
다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합,
 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.
다음과 같은 5X5 배열에서 최댓값은 29이다.


[제약 사항]
총 10개의 테스트 케이스가 주어진다.
배열의 크기는 100X100으로 동일하다.
각 행의 합은 integer 범위를 넘어가지 않는다.
동일한 최댓값이 있을 경우, 하나의 값만 출력한다.

[입력]
각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고
그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.

"""

for t in range(1, 11):
    input()

    # 100 * 100 크기의 2차원 리스트(배열) 생성
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 최대값을 저장할 변수 초기화 (행열이 100단위다 보니 마이너스 값이 들어갈경우 에도 가능할 경우를 대비해 무한대에 음수로 선언한다)
    max_v = -float('inf')

    # 1 .각 행의 합 구하기 - 행 우선 순회
    for r in range(100):  # 각 행에 대해 반복
        row_sum = 0  # 현재 행의 합을 저장할 변수 초기화
        for c in range(100):  # 각 열의 원소를 순회하며
            row_sum += arr[r][c]  # 해당 행의 열 값을 더함
        # 행의 최대값 구하기
        if row_sum > max_v:
            max_v = row_sum

    # 2. 각 열의 합 구하기 - 열 우선 순회
    for c in range(100):  # 각 열에 대한 반복
        col_sum = 0  # 햔제 열의 합을 저장할 변수 초기화
        for r in range(100):  # 긱 헹의 원소를 순회하며
            col_sum += arr[r][c]  # 해당 열의 행 값을 더함

            # 열의 최대값 구하기
            if col_sum > max_v:  # 최대값보다 현재 열의 합이 크면
                max_v = col_sum  # 촤대값 갱신

    # 3. 우하향 대각선 (좌상 --> 우하)
    right_down_diag_sum = 0
    for i in range(100):  # (0,0),(1,1)...(99,99) 형태의 인덱스
        right_down_diag_sum += arr[i][i]  # 같은 행 같은 열 인덱스의 값들을 누적

        if right_down_diag_sum > max_v:
            max_v = right_down_diag_sum  # 우하향 대각선의 합이 최대값보다 크면 갱신
    # 4. 우상향 대각선 (좌하 -> 우상)
    right_up_diag_sum = 0
    for r in range(100):
        right_up_diag_sum += arr[r][99 - r] # 반대로 (99,0), (98,1) ... (0,99) 즉 c랑r의 합은 99가 나옴 그래서 c + r = 99 에서 r을 99로 넘겨줘서 N-1-answer 라는 식이 나오게됨
        if right_up_diag_sum > max_v:
            max_v = right_up_diag_sum  # 우상향 대각선의 합이 최대값보다 크면 갱신

    print(f"#{t} {max_v}")
