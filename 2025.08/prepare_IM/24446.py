"""
24446. 공굴리기 게임
출처 : https://buly.kr/Yf30fR
"""

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    