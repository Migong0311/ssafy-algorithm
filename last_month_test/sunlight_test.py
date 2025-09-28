import sys

sys.stdin = open('sun.txt', 'r')
T = int(input())

for t in range(1, T + 1):

    # 태양열 에너지 (패널 + 렌즈) (SWEA 스타일)
    # ------------------------------------------------------------
    # [입력 형식]
    # T
    # N M
    # (N줄) 패널 NxN
    # (M줄) 렌즈 MxM
    # ...
    #
    # [문제 정의 요약]
    # - 새 판넬의 크기: (N-M+1) x (N-M+1)
    # - 새 판넬의 각 칸 값 = (패널의 해당 MxM 영역합) + (렌즈 전체 합)
    # - 예시처럼 렌즈 합은 위치에 상관없이 일정.
    #
    # [풀이 전략 A: 브루트포스]
    # - 렌즈 전체 합 lens_sum 미리 계산.
    # - 모든 시작점 (i, j)에 대해 패널의 MxM 부분합을 직접 더함.
    # - 해당 위치의 값 = 부분합 + lens_sum.
    # - 시간복잡도 O((N-M+1)^2 * M^2).
    #
    # [풀이 전략 B: 2D 누적합(프리픽스)로 최적화]
    # - 패널에 대해 (N+1)x(N+1) 누적합 ps 구성.
    # - 임의 MxM 구간합을 O(1)에 계산:
    #   sum = ps[r2][c2] - ps[r1][c2] - ps[r2][c1] + ps[r1][c1]
    #   (r1,c1)=(i,j), (r2,c2)=(i+M, j+M)
    # - 각 위치 값 = (구간합) + lens_sum.
    # - 전체 시간복잡도 O(N^2).
    #
    # [절차]
    # 1) 테스트케이스 T 입력
    # 2) 케이스 반복:
    #    2-1) N, M 입력
    #    2-2) 패널 NxN 입력
    #    2-3) 렌즈 MxM 입력
    #    2-4) 렌즈 전체 합 lens_sum 계산
    #    2-5) (브루트포스) 또는 (누적합) 중 한 방식으로 각 (i, j) 값 산출
    #    2-6) SWEA 형식으로 "#t" 출력 후, 결과 그리드 줄단위 출력
    #
    # [출력 형식]
    # #1
    # v11 v12 ...
    # v21 v22 ...
    # ...
    # #2
    # ...
    #
    # (아래에 실제 로직을 작성하시면 됩니다)
T = int(input())
 
for t in range(1, T + 1):
    N, M = map(int, input().split())
 
    panel = [list(map(int, input().split())) for _ in range(N)]
    lens = [list(map(int, input().split())) for _ in range(M)]
    # lens 배열 총 합
    lens_sum = 0
 
    for i in range(M):
        for j in range(M):
            lens_sum += lens[i][j]
 
    print(f'#{t}')
 
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            panel_sum = 0
 
            for x in range(M):
                for y in range(M):
                    panel_sum += panel[i + x][j + y]
 
            result = panel_sum + lens_sum
 
            print(result, end=' ')
        print()
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
