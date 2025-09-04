'''
9386. 연속한 1의 개수
출처 : https://buly.kr/4bibVI2
'''
import sys

sys.stdin = open('a.txt', 'r')

T = int(input()) # tc개수

for t in range(1, T + 1):# T만큼 반복
    N = int(input()) # arr의 개수
    arr = input() # 0과 1로 이루어진 arr

    cnt = 0 # 1의 연속된 개수
    cnt_m = 0 # 그 중 최대값
    for i in range(N):# arr 인덱스만큼 순회
        if arr[i] == '1': # 1찾음
            cnt += 1 # 증가
            if cnt > cnt_m: # 최대값
                cnt_m = cnt # 갱신
        else:
            cnt = 0 # 1없음 때리치아라

    print(f'#{t} {cnt_m}') # 형식대로
