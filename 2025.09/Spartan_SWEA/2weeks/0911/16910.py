import sys

sys.stdin = open('test.txt', 'r')

'''
16910. 원 안의 점
'''

T = int(input())

for t in range(1, T + 1):
    N = int(input())  # 반지름
    cnt = 0  # 문제 요구사항
    for i in range(-N, N + 1):  # x축 좌표
        for j in range(-N, N + 1):  # y축 좌표
            if i * i + j * j <= N * N:  # x^2+y^2<=N^2인 격자점일 경우
                cnt += 1  # 카운팅

    print(f'#{t} {cnt}')
