# import sys
#
# sys.stdin = open('input.txt', 'r') 입력

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split()) # 전체행렬 및 해당행렬 값 입력
    arr = [list(map(int, input().split())) for _ in range(N)] # 시작 전체 행렬 입력 N * N

    max_fly = 0  # 죽일 수 있는 파리 수의 최대값

    # 시작점 answer,j 를 N-m+1만큼 순회 (전체행렬에서 M의 정사각형 행렬만큼 순회)
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly_sum = 0 # 파리들의 합계 초기화
            for di in range(M): # 죽이는 범위 내에서 순회
                for dj in range(M):
                    fly_sum += arr[i + di][j + dj] # 죽인 범위 값들의 합계

            if fly_sum > max_fly: # 그 중에서 가장 많이 죽인 범위를
                max_fly = fly_sum # max_fly에 할당
    print(f"#{t} {max_fly}")
'''
[출력]
#1 49
#2 159
#3 428
#4 620
#5 479
#6 941
#7 171
#8 968
#9 209
#10 1242
'''