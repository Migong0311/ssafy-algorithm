"""
종이 꽃가루가 들어있는 풍선이 M개씩 N개의 줄에 붙어있고,
어떤 풍선을 터뜨리면 안에 든 종이 꽃가루 개수만큼
상하 좌우의 풍선이 추가로 터지게 되는 게임이 있다.
예를 들어 풍선에 든 꽃가루가 1개씩일 때,
가운데 풍선을 터뜨리면 상하좌우의 풍선이
추가로 1개씩 터지면서 총 5개의 꽃가루가 날리게 된다.
NxM개의 풍선에 들어있는 종이 꽃가루 개수A가 주어지면,
한 개의 풍선을 선택했을 때 날릴 수 있는 꽃가루의 합 중
최대값을 출력하는 프로그램을 만드시오.
"""
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
plus_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

for t in range(1, T + 1):
    N, M = map(int, input().split())  # N * M 격자 만들기
    A = [list(map(int, input().split())) for _ in range(N)]  # 꽃가루 개수 A개

    max_ball = 0  # 최대로 날릴 수 있는 꽃가루 수 초기화

    # 모든 위치에 대해 풍선을 터뜨려보며 최대 꽃가루 개수 계산
    for i in range(N):
        for j in range(M):
            total = A[i][j]  # 현재 위치(answer,j) 의 풍선에서 나오는 꽃가루
            power = A[i][j]  # 해당 풍선의 파워로 꽃가루 수만큼 상하좌우로 터짐

            # 4방향 모두에 대해 반복
            for dr, dc in plus_dirs:
                for step in range(1, power + 1): # 현재 풍선의 파워만큼 확장
                    nr = i + dr * step  # 새로운 행 위치
                    nc = j + dc * step  # 새로운 열 위치

                    if 0 <= nr < N and 0 <= nc < M: # 격자 범위내일 경우에만
                        total += A[nr][nc] # 해당 위치의 꽃가루 개수 더하기

            max_ball = max(max_ball, total)  # 지금까지 중 최대값 업데이트
    print(f"#{t} {max_ball}")

# 1 10
# 2 26
# 3 40
