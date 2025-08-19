"""
16118 구간합
출처 : https://buly.kr/AaqH71o
"""

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())  # N : 배열개수 M : 이웃한 M개의 합
    arr = list(map(int, input().split()))  # 검증할 배열
    s = 0  # 현재 합계
    for i in range(M):  # 이웃한 배열의 개수만큼 순회
        s += arr[i]  # 현재값부터 i번원소까지 더함
        max_s = s  # 최대 init
        min_s = s  # 최소 init

    for j in range(1, N - M + 1):  # 1부터 전체 중 해당 배열만큼 순회
        s = s - arr[j - 1] + arr[j + M - 1]  # 이전구간에서 첫번째 숫자 제거 다음숫자 추가

        if s > max_s:  # 최대값 갱신
            max_s = s
        if s < min_s:  # 최소값 갱신
            min_s = s
    print(f"#{t} {max_s - min_s}")

