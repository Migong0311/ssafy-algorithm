"""
24449. 야구선수
출처 : https://buly.kr/58SkTde
"""

import sys

sys.stdin = open('input.txt', 'r')
T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    player = list(map(int, input().split()))

    player.sort()
    cnt_player = 0

    for i in range(N):
        for j in range(i, N):
            if player[j] - player[i] <= K:
                max_player = j - i + 1
                if max_player > cnt_player:
                    cnt_player = max_player
            else:
                break

    print(f'#{t} {cnt_player}')
