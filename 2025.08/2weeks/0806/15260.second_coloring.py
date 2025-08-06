"""
10 x 10 격자에 파란색 빨간색 칠할려고 함
N개영역이 주어질 때 좌상과 우하 모서리 인덱스 칠할 색상이 주어질때 칠이 끝난 후 색이 겹쳐
보라색이 된 색의 칸 수를 구하시오

예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.

N = 2
2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )
3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )

입력
테스트케이스 : T
칠할 영역의 개수 : N
각각 좌상단 인덱스 r1,c1
각각 우하단 인덱스 r2,c2
색 : color
"""
T = int(input())

for t in range(1, T + 1):
    N = int(input())  # 칠할 영역의 개수
    arr = [[0] * 10 for _ in range(10)]  # 10x10 격자 초기화
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        # 주어진 범위 안에서 색칠
        for i in range(r1, r2 + 1):  # 행 범위
            for j in range(c1, c2 + 1):  # 열 범위
                arr[i][j] += color  # 색상 덧셈 누적 (1 + 2 = 3)

    s = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                s += 1
    print(f'#{t} {s}')