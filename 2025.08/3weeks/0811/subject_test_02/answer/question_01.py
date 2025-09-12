import sys

sys.stdin = open('algo1_sample_in.txt','r')

T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    row= col = -1  # 없을떄 가정

    # 별을 정확히 K개 포함하고 있는영역의 시작위치
    # 시작 위치는 2차원 배열의  모든 위치에서 만들어봄
    # 만들기 가능한 위치는 M만큼(안에 있는 작은 영역의 크기만큼)

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # answer,j 에서부터 M*M크기의 작은 영역을 만들고
            # 이 작은 영역 안에 별이 몇개 있나 세어보기
            star = 0
            # 작은 영역의 범위를 인덱스로 지정해서 탐색
            # answer,j ~ answer+M-1,j+M-1
        # 직은 영역의 행번호 열번호  ni,nj
            for ni in range(i, i + M):
                for nj in range(j, j + M):
                    if arr[ni][nj] == '*':
                        star += 1
                if star == K:
                    row = i
                    col = j

    print(f'#{t} {row} {col}')
