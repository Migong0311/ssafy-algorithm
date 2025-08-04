'''

N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.


[입력]

첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )

각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )

다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

T = int(input())  # 테스트 케이스 개수를 입력받음

for t in range(1, T + 1):  # 1부터 T까지 반복함
    N = int(input())

    lst = list(map(int, input().split()))

    max_v = lst[0] # 최대값 위치
    min_v = lst[0] # 최소값 위치
    for i in range(1, N):
        if max_v < lst[i]: # 최대값이 i번째 인덱스값 보다 작을경우
            max_v = lst[i] # 최대값에 i번째 인덱스값을 할당

    for j in range(1, N):
        if min_v > lst[j]:  # 최소값이 j번째 인덱스값 보다 클경우
            min_v = lst[j] # 최대값에 j번째 인덱스값을 할당

    result = max_v - min_v # 요구사항 실행
    print(f'#{t} {result}') # 출력형식 맞춰서 실행
