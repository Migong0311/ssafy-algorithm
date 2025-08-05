# import sys
#
# sys.stdin = open("input.txt", "r")

'''
N개의 양의 정수가 첫번째부터 N번째까지 주어진다.
최대값의 위치와 최소값의 위치의 차이를 절대값으로 출력 하시오.
단, 가장 작은 수가 여러 개이면 먼저 나오는 위치로 하고 가장 큰 수가 여러 개이면 마지막으로 나오는 위치로 한다.
예를 들어, {1, 1, 2, 3, 3} 가 주어지면 최대값의 위치는 5이고, 최소값의 위치는 1이다. 따라서 두 값 차이의 절대값은 4이다.

'''


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 가장 먼저 최소값을 찾기 위해 가장 먼저 등장한 인덱스로 초기화
    min_v = arr[0]
    min_idx = 0
    # arr의 길이만큼 순환
    for i in range(len(arr)):
        if arr[i] < min_v:  # 최소값 찾기위해 만일 i번의 인덱스가 최소값보다 작으면
            min_v = arr[i]  # 더 작은 값이 나왔기 때문에 갱신
            min_idx = i  # 최소값 등장 위치 저장

    # 그리고 가장 마지막 인덱스 값의 최대값을 찾기위한 초기화
    max_v = arr[0]
    max_idx = 0
    for i in range(len(arr)):
        if arr[i] >= max_v:  # 다음값이 크거나 같을때 즉 조건대로 다음값이 더 크면 그 값이 나와야 되기때문
            max_v = arr[i]  # i번 인덱스 값을 최대값에 할당
            max_idx = i  # 최대값 등장 위치 저장
    if max_idx > min_idx:  # 최대깂 최소값의 각각 절대값 비교후 연산
        result = max_idx - min_idx
    else:
        result = min_idx - max_idx  # 이것은 최대값 최소값 비교가 아닌 말그대로 양수의 절대값을 비교하는거임
        # 그러니 작은거에서 큰걸 뺸다고 잘못된게 아님
        # 예를들어 arr = [5,4,3,2,1] 여기에서 최대값의 위치는 1 최소는 5이기 때문에 else문 대로 해줘야 차이가 나옴
    print(f'#{t} {result}')
# 1 4
# 2 6
# 3 18
