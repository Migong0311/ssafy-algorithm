'''
2805. 농작물 수확하기
- N*N 배열에서 마름모 영역만 합산하는 문제
'''

import sys
sys.stdin = open('test.txt', 'r')

# 테스트 케이스 개수
T = int(input())

for t in range(1, T + 1):  # tc만큼 순회
    N = int(input())  # 변의 길이
    # N*N 배열 입력
    # 중앙 인덱스 mid 계산
    # 전체 합을 저장할 변수 초기화
    # 모든 행을 순회하며 마름모 범위 열만 합산
    # 결과 출력
