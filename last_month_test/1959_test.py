'''
1959. 두 개의 숫자열
출처 : https://buly.kr/DwEkc4D
'''
import sys

sys.stdin = open('1959.txt', 'r')

# 테스트 케이스 개수 입력
T = int(input())  # 첫 줄: 테스트 케이스 수

for tc in range(1, T + 1):  # 1부터 T까지 순회
    # N, M 입력 (수열의 길이)
    # 수열 A, 수열 B 입력

    # 풀이 전략:
    # - 두 수열 중 짧은 수열을 긴 수열 위로 슬라이딩
    # - 각 위치마다 같은 인덱스끼리 곱한 값을 모두 더한 합을 구함
    # - 그 중 최댓값을 선택

    # 절차:
    # 1) N, M, A, B 입력

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    best = -10 ** 11
    # 2) 어떤 배열이 짧은지 확인
    if N <= M:

        # 3) 짧은 배열을 긴 배열 위에서 0..shift_max 만큼 이동시키며 곱합 계산
        shift_max = M - N
        for i in range(shift_max + 1):
            acc = 0
            for j in range(N):
                acc += A[j] * B[i + j]
            # 4) 최대 합 갱신
            best = max(acc, best)
    else:
        # 3) 짧은 배열을 긴 배열 위에서 0..shift_max 만큼 이동시키며 곱합 계산
        shift_max = N - M
        for i in range(shift_max + 1):
            acc = 0
            for j in range(M):
                acc += A[j + i] * B[j]
            # 4) 최대 합 갱신
            best = max(acc, best)

    # 5) 결과를 "#tc 값" 형식으로 출력
    print(f'#{tc} {best}')
