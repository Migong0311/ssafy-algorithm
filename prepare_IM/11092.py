'''
11092. 최대 최소의 간격
출처 : https://buly.kr/NkPCBA
'''
import sys

sys.stdin = open('sample_input.txt', 'r')
T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # N : 숫자개수
    arr = list(map(int, input().split()))  # 입력 받을 숫자 리스트

    # 초기값 최소 & 최대
    min_val = arr[0]
    max_val = arr[0]
    min_pos = 1 # 최소값 첫번째 위치
    max_pos = 1 # 최댓값 마지막 위치 if 동일값 나올시 계속 갱신

    for i in range(N):
        x = arr[i]
        # 최대값 및 최소값 갱신
        #
        if x < min_val:
            min_val = x
            min_pos = i + 1
        if x > max_val:
            max_val = x
            max_pos = i + 1
        elif x == max_val:
            max_pos = i + 1
    print(f"#{tc} {abs(max_pos - min_pos)}")
