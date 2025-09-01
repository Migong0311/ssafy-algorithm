'''
1959. 두 개의 숫자열
출처 : https://buly.kr/DwEkc4D
'''

# 테스트 케이스 개수 입력
T = int(input())  # 첫 줄: 테스트 케이스 수

for tc in range(1, T + 1):  # 1부터 T까지 순회
    N, M = map(int, input().split())  # 각 케이스의 N, M 입력
    A = list(map(int, input().split()))  # 길이 N의 수열 A 입력
    B = list(map(int, input().split()))  # 길이 M의 수열 B 입력

    # 어떤 수열이 더 긴지에 따라 슬라이딩 기준을 결정
    # 더 긴 수열 위로 더 짧은 수열을 좌->우로 겹치며 곱의 합을 계산해 최댓값을 찾음
    best = 0  # 현재까지의 최댓값(초기 None으로 설정)

    if N <= M:  # A가 더 짧거나 같은 길이인 경우
        shift_max = M - N  # 가능한 시프트(겹침) 횟수
        for s in range(shift_max + 1):  # s=0..shift_max까지 모든 정렬 위치 시도
            acc = 0  # 이번 정렬에서의 곱의 합 누적값
            for i in range(N):  # A의 모든 원소에 대해
                acc += A[i] * B[i + s]  # 마주보는 원소끼리 곱하여 누적
            if best is None or acc > best:  # 최댓값 갱신(내장 max() 미사용)
                best = acc
    else:  # B가 더 짧은 경우 (혹은 A가 더 김)
        shift_max = N - M  # 가능한 시프트(겹침) 횟수
        for s in range(shift_max + 1):  # s=0..shift_max까지 모든 정렬 위치 시도
            acc = 0  # 이번 정렬에서의 곱의 합 누적값
            for i in range(M):  # B의 모든 원소에 대해
                acc += A[i + s] * B[i]  # 마주보는 원소끼리 곱하여 누적
            if best is None or acc > best:  # 최댓값 갱신
                best = acc

    print(f"#{tc} {best}")  # 형식에 맞게 출력
