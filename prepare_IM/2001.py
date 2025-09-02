"""
2001. 파리퇴치
출처 : https://buly.kr/D3esbMC
"""

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    fly_cnt = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly_sum = 0
            for r in range(M):
                for c in range(M):
                    fly_sum += arr[i+r][j+c]

            if fly_sum > fly_cnt:
                fly_cnt = fly_sum

    print(f'#{t} {fly_cnt}')
