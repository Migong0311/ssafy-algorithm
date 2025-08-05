import sys

sys.stdin = open("input.txt", "r")
"""
삼성시에는 1번부터 5000번까지의 정류장이 있고, 
각 버스 노선은 정해진 범위(Ai ~ Bi)의 정류장을 지난다.

각 테스트케이스마다:
- N개의 버스 노선이 주어지고, 각 노선은 [Ai, Bi] 범위를 지난다.
- 이후 P개의 정류장 번호가 주어질 때, 각 정류장을 지나는 버스 노선의 수를 구한다.
"""

# 테스트 케이스 개수 입력
T = int(input())

# 테스트 케이스 반복
for t in range(1, T + 1):
    N = int(input())  # 버스 노선 수

    # 버스 정류장 수 초기화 (인덱스 0~5000까지 총 5001개)
    stops = [0] * 5001

    # 각 버스 노선 범위 [Ai, Bi]에 대해 해당 범위에 +1씩 누적
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            stops[i] += 1  # i번 정류장을 지나므로 1개 노선 추가

    P = int(input())  # 확인할 버스 정류장 수
    result = []  # 결과 저장용 리스트

    for _ in range(P):
        C = int(input())
        result.append(str(stops[C]))  # 해당 정류장에 다니는 노선 수

    # 출력 형식에 맞춰 출력
    print(f"#{t} {' '.join(result)}")

#1 1 2 2 1 1