import sys
sys.stdin = open('2001.txt','r')

T = int(input())  # 테스트 케이스 개수 입력

for t in range(1, T + 1):           # 1번 케이스부터 T번 케이스까지 반복
    N, M = map(int, input().split())  # N: 배열 크기, M: 파리채 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # N x N 배열 입력

    fly_cnt = 0   # 최대로 죽일 수 있는 파리 수 저장할 변수 (초기값 0)

    # (i, j) : 파리채를 올려놓는 왼쪽 위 시작 좌표
    for i in range(N - M + 1):         # 세로 방향 가능한 시작 위치
        for j in range(N - M + 1):     # 가로 방향 가능한 시작 위치
            fly_sum = 0                # 현재 위치에서 잡힌 파리 수 합

            # M x M 영역 순회
            for r in range(M):         # 파리채 높이만큼
                for c in range(M):     # 파리채 너비만큼
                    fly_sum += arr[i+r][j+c]  # 해당 칸의 파리 수 더하기

            # 지금까지 구한 최대값보다 크면 갱신
            if fly_sum > fly_cnt:
                fly_cnt = fly_sum

    # 결과 출력 (SWEA 스타일)
    print(f'#{t} {fly_cnt}')
'''

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