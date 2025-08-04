'''
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.

v = [1,2,3,4,5]
이웃한 M개의 합이 가장 작은 경우 1 + 2 + 3 = 6

이웃한 M개의 합이 가장 큰 경우 3 + 4 + 5 = 12

답은 12와 6의 차인 6을 출력한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

'''

T = int(input())  # 테스트 케이스 개수 입력

for test_case in range(1, T + 1):  # 각 테스트 케이스 반복
    n, m = map(int, input().split())  # n: 정수 개수, m: 부분 구간의 크기
    numbers = list(map(int, input().split()))  # n개의 정수 입력받기

    # 초기 구간 합 계산 (0번 인덱스부터 m개)
    current_sum = 0
    for i in range(m):  # 첫 번째 구간의 합 계산
        current_sum += numbers[i]

    max_sum = current_sum  # 최대 구간 합 초기화
    min_sum = current_sum  # 최소 구간 합 초기화

    # 슬라이딩 윈도우 기법을 이용해 모든 구간 합을 계산
    for start in range(1, n - m + 1):  # 시작 인덱스 1부터 끝까지 반복
        # 이전 구간에서 첫 번째 숫자 제거하고, 다음 숫자 추가
        current_sum = current_sum - numbers[start - 1] + numbers[start + m - 1]

        if current_sum > max_sum:  # 최대값 갱신
            max_sum = current_sum
        if current_sum < min_sum:  # 최소값 갱신
            min_sum = current_sum

    # 최대 구간 합과 최소 구간 합의 차이 출력
    print(f"#{test_case} {max_sum - min_sum}")
