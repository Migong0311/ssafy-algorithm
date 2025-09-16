'''
9489. 고대 유적
'''
import sys

sys.stdin = open('test.txt', 'r')
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가장 긴 구조물 길이 기록 변수
    best = 0

    # 열 스캔
    for i in range(N):
        running = 0  # 연속된 1의 길이 누적
        for j in range(M):
            if arr[i][j] == 1:
                running += 1  # 1일경우 연속적 길이 증가
            else:
                # 0을 만나면 지금까지의run으로 최대값 갱신 시도
                if running > best:
                    best = running
                running = 0  # 연속 길이 초기화
        # 행의 끝에서도 갱신 필요
        if running > best:
            best = running

    # 행 스캔
    for j in range(M):
        running = 0  # 연속된 1의 길이 누적
        for i in range(N):
            if arr[i][j] == 1:
                running += 1
            else:
                # 0을 만나면 지금까지의run으로 최대값 갱신 시도
                if running > best:
                    best = running
                running = 0  # 연속 길이 초기화
        # 열의 끝에서도 갱신 필요
        if running > best:
            best = running
    # 구조물 최소 크기가 1 * 2 이므로 길이 1은 구조물로 보지않음
    # 최대값이 1일경우 0으로 처리
    if best == 1:
        best = 0

    print(f'#{t} {best}') # 형식에 맞게 출력
