# 태양열 에너지 (가장 단순한 브루트포스 버전)
'''
2
5 2
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
4 4
4 4
7 3
1 2 3 4 5 6 7
8 9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31 32 33 34 35
36 37 38 39 40 41 42
43 44 45 46 47 48 49
1 1 1
1 1 1
1 1 1
'''
import sys
sys.stdin = open('sun.txt','r')
T = int(input().strip())  # 테스트 케이스 개수

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 패널 크기 N, 렌즈 크기 M

    panel = []                        # N x N 패널
    for _ in range(N):
        panel.append(list(map(int, input().split())))  # 패널의 한 행 입력

    lens = []                         # M x M 렌즈
    for _ in range(M):
        lens.append(list(map(int, input().split())))   # 렌즈의 한 행 입력

    # 렌즈 전체 합 (위치와 무관하게 항상 동일)
    lens_sum = 0
    for i in range(M):                # 렌즈의 모든 칸 순회
        for j in range(M):
            lens_sum += lens[i][j]    # 렌즈 값 누적

    # 결과 판넬의 크기 = (N - M + 1) x (N - M + 1)
    out_h = N - M + 1
    out_w = N - M + 1

    print(f"#{tc}")                   # SWEA 케이스 헤더 출력

    # 각 출력 칸 (i, j)에 대한 값 계산
    for i in range(out_h):            # 시작 행 좌표 i
        row_vals = []                 # 한 줄에 출력할 값들(문자열)
        for j in range(out_w):        # 시작 열 좌표 j
            panel_sum = 0             # 패널의 MxM 부분합 초기화

            # 패널의 [i..i+M-1][j..j+M-1] 구간을 직접 더함
            for x in range(M):        # M개의 행
                for y in range(M):    # M개의 열
                    panel_sum += panel[i + x][j + y]

            value = panel_sum + lens_sum   # 문제 정의: 부분합 + 렌즈합
            row_vals.append(str(value))    # 문자열로 바꿔서 행에 추가

        print(" ".join(row_vals))     # 한 줄 출력 (공백 구분)

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