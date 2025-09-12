'''
5789. 현주의 상자 바꾸기
'''

T = int(input())

for t in range(1, T + 1):
    N, Q = map(int, input().split()) # N번까지 N개의 상자 Q회동안 일정범위 상자 동일 숫자 변경
    arr = [0] * (N + 1) # 초기값 모두 0 으로 되있는 리스트 생성 단 1부터 시작이기때문에 0은 버림
    for i in range(1, Q + 1): # 1부터 Q회만큼 순회
        L, R = map(int, input().split()) # L번 상자부터 R번 상자까지
        for k in range(L, R + 1): # 상자 범위 사이에값을
            arr[k] = i # i로 변환

    print(f'#{t}', *arr[1:]) # 출력시 1부터 시작이기때문에 초기 0으로 초기화 했기때문에 0번 인덱스는 슬라이싱
