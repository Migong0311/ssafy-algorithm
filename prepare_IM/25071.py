'''
25071. 포탈이동
출처 : https://buly.kr/8IwVPlh
'''

T = int(input())

for t in range(1, T + 1):
    N = int(input())  # 방의 개수
    pi = list(map(int, input().split()))  # 해당 방 첫 방문시 초기화되는 방번호
    idx = 0  # 인덱스번호
    cnt = 0  # 방문카운트
    visited = [0] * (N - 1)  # 방문리스트

    while idx < N - 1: # 인덱스가 마지막번쨰 도달 시 종료
        if idx == 0: # 시작지점일경우 증가
            cnt += 1
            idx += 1
        elif visited[idx] == 1: # 1은 무조건 2로 이동
            cnt += 1
            idx += 1
        else:
            visited[idx] = 1 # default 1
            cnt += 1
            idx = pi[idx] - 1 # 입력받은 방번호의 인덱스랑 차이는 1

    print(f'#{t} {cnt}')
