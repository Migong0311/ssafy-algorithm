'''
돌뒤집기 2
'''

import sys

sys.stdin = open('sample_in (1).txt', 'r')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())  # N : 돌 개수 M : 뒤집기 횟수
    arr = list(map(int, input().split()))  # N개의 배열

    '''
    조건
    i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해,
    1. 각각 같은 색이면 뒤집고, 
    2. 다른 색이면 그대로 둔다.
    3. 주어진 돌을 벗어나는 경우 뒤집기는 중지된다.
    '''

    for _ in range(M):
        i, j = map(int, input().split())  # i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해,
        i -= 1
        for d in range(1, j + 1):  # 마주보는 j개의 돌에 대해 좌 우 탐색
            left = i - d
            right = i + d

            if left < 0 or right >= N:  # 주어진 돌을 벗어나는 경우 뒤집기는 중지된다.
                break

            if arr[left] == arr[right]:  # 각각 같은 색이면 뒤집고,
                arr[left] = 1 - arr[left]  # case는 1,0 둘 뿐이므로 1-0(arr[left]) = 1
                arr[right] = 1 - arr[right]  # 또는 1-1(arr[right]) = 0
            else:
                continue  # 다른 색이면 그대로 둔다.
    print(f'#{t}', *arr)
