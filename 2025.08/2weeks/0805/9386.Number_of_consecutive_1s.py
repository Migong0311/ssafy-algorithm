# import sys
#
# sys.stdin = open("input.txt", "r")

"""
N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램을 만드시오.
첫 줄에 테스트케이스 개수 T,
다음 줄부터 테스트케이스별로 첫 줄에 수열의 길이 N,
다음 줄에 N개의 0과1로 구성된 수열이 공백없이 제공된다.
"""
# 테스트 케이스 수 입력
T = int(input())

# 테스트 케이스만큼 반복
for t in range(1, T + 1):
    N = int(input())  # 수열의 길이 입력
    line = input().strip()  # 수열 문자열 입력 (공백 없이)

    max_count = 0      # 지금까지의 최대 연속 1의 개수
    current_count = 0  # 현재 연속으로 이어진 1의 개수

    for char in line:
        if char == '1':
            current_count += 1  # 1이면 연속 카운트 증가
            if current_count > max_count:
                max_count = current_count  # 최대값 갱신
        else:
            current_count = 0  # 0이 나오면 연속이 끊기므로 초기화

    # 결과 출력
    print(f'#{t} {max_count}')
# 1 3
# 2 1
# 3 4
