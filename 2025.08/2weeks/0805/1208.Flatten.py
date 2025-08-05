# 테스트 케이스는 10개로 고정
T = 10

# 각 테스트 케이스마다 처리
for tc in range(1, T + 1):
    N = int(input())  # 덤프 가능한 횟수 입력
    heights = list(map(int, input().split()))  # 상자들의 높이 입력 받기

    # 덤프를 최대 N번까지 반복
    for _ in range(N):
        # 현재 가장 높은 상자와 가장 낮은 상자의 값과 인덱스 초기화
        max_val = 0         # 최대값은 0부터 시작
        min_val = 101       # 최소값은 문제 조건 상 최대값보다 큰 수로 초기화
        max_idx = -1        # 인덱스도 초기화
        min_idx = -1

        # 최대값과 최소값 및 인덱스를 찾기 위한 반복문
        for idx in range(len(heights)):
            if heights[idx] > max_val:
                max_val = heights[idx]
                max_idx = idx
            if heights[idx] < min_val:
                min_val = heights[idx]
                min_idx = idx

        # 덤프 수행: 최대값 -1, 최소값 +1
        heights[max_idx] -= 1
        heights[min_idx] += 1

        # 덤프 중에 이미 높이 차이가 1 이하인 경우는 생략 가능 (효율적이진 않음)
        # if max_val - min_val <= 1:
        #     break

    # 덤프 이후 다시 최대/최소 높이 차이를 계산
    max_val = 0
    min_val = 101
    for idx in range(len(heights)):
        if heights[idx] > max_val:
            max_val = heights[idx]
        if heights[idx] < min_val:
            min_val = heights[idx]

    # 최종 결과 출력
    print(f"#{tc} {max_val - min_val}")
