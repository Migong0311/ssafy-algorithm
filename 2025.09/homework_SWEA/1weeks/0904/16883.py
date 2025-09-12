'''
16883. 2일차 응용 - 최소 합
'''
delta = [(0, 1), (1, 0)]
T = int(input())

# 현재위치 (answer,j) (행,열)
# (0,0) -> 우or하 이동 반복 -> (N-1.N-1)
def solve(i,j,now):
    # 종료

    # 재귀조건

    pass


for t in range(1, T + 1):
    N = int(input())  # 한변의 길이

    # N * N
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 문제에서 원하는 답 : 합이 최소가 되도록
    min_sum = 10 ** 9
