# 테스트 케이스 개수
T = int(input())
for tc in range(1, T + 1):
    # 소인수분해할 숫자
    N = int(input())

    # 밑
    lst = [2, 3, 5, 7, 11]
    cnt = [0] * 5
    # i(밑)으로 나누었을 때 나머지가 0이면 지수 1 추가 + N으로 나누기
    # i로 나누어지지 않을 때까지
    for i in range(5):
        while N % lst[i] == 0:
            cnt[i] += 1
            N //= lst[i]
    print(f'#{tc}', *cnt)