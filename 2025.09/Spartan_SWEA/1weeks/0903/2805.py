'''
2805. 농작물 수확하기
출처 : https://buly.kr/2feGP2t
'''
import sys

sys.stdin = open('test.txt', 'r')
'''
N * N 정사각형 단, N은 홀수
정사각형 마름모 형태로 증가 
마름모가 어찌 증가하냐
정사각형 배열을 90도 오른쪽으로 돌린기준으로
N = 5 일경우
1 len = 1
1 2 3 len = 3
1 2 3 4 5 -> 젤 가운데가 N값이 되는 길이가 1부터 N까지 차례대로 늘어났다가 다시 줄어드는 방식? 
1 2 3
1


'''
T = int(input())  # tc

for t in range(1, T + 1):  # tc만큼 순회
    N = int(input())  # 변의길이
    arr = [list(map(int, input())) for _ in range(N)]  # N * N 배열 생성
    total = 0  # 마름모 영역의 총합
    mid = N // 2  # 가운데 인덱스

    # 모든 행 순회하면서 마름모에 해당하는 열구간만 합산
    for i in range(N):  # i는 현재 행 인덱스
        offset = abs(mid - i)  # 중심 행으로부터의 세로 거리
        start = offset  # 이 행에서 합산을 시작할 열 인덱스
        end = N - offset  # 이 행에서 합산을 종료할 열 인덱스(미포함)

        row_sum = 0  # 현재 행에서 마름모 구간 합
        j = start  # 열 인덱스 초기화

        # start <= j < end 범위 합산
        while j < end:
            row_sum += arr[i][j]  # 해당 칸의 값을 누적
            j += 1  # 다음 열로 이동

        total += row_sum  # 전체 합에 현재 행 합을 누적

    print(f'#{t} {total}')

# 1 23
