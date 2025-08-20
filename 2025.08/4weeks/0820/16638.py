"""
16638 회전
"""
import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split()) # N : 배열 수 M : 이동횟수
    q = list(map(int, input().split()))

    front = 0  # 큐의 앞 인덱스
    K = M % N  # 불필요 회전 제거
    front = (front + K) % N  # K번 "앞을 뒤로" 보낸 효과

    print(f'#{t} {q[front]}')
