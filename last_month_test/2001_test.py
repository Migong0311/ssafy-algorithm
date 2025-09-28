import sys

sys.stdin = open('sun.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    panel = [list(map(int, input().split())) for _ in range(N)]
    lens = [list(map(int, input().split())) for _ in range(M)]
    # lens 배열 총 합
    lens_sum = 0

    for i in range(M):
        for j in range(M):
            lens_sum += lens[i][j]

    print(f'#{t}')

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            panel_sum = 0

            for x in range(M):
                for y in range(M):
                    panel_sum += panel[i + x][j + y]

            result = panel_sum + lens_sum

            print(result, end=' ')
        print()
'''         
#1
20 20 20 20
20 20 20 20
20 20 20 20
20 20 20 20
#2
90 99 108 117 126
153 162 171 180 189
216 225 234 243 252
279 288 297 306 315
342 351 360 369 378
'''
