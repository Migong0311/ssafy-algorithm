import sys
sys.stdin = open('input.txt', 'r')  # 표준 입력을 input.txt 파일로 변경함

T = int(input())  # 테스트 케이스 개수 입력받음

for t in range(1, T + 1):  # 테스트 케이스 수만큼 반복
    N, K = map(int, input().split())  # 퍼즐 크기 N과 단어 길이 K 입력받음
    arr = [list(map(int, input().split())) for _ in range(N)]  # 퍼즐 격자 입력받음

    count = 0  # 단어가 들어갈 수 있는 자리 수 세기 위한 변수 초기화

    # 행 우선 탐색
    for i in range(N):  # 각 행에 대해 반복
        for j in range(N - K + 1):  # 연속 K칸 탐색 가능 범위 내에서 반복
            if arr[i][j:j + K] == [1] * K:  # K칸 연속으로 1인지 확인
                left = j == 0 or arr[i][j - 1] == 0  # 왼쪽이 경계 밖이거나 0인지 확인
                right = j + K == N or arr[i][j + K] == 0  # 오른쪽이 경계 밖이거나 0인지 확인
                if left and right:  # 양쪽이 막혀 있어야 단어가 딱 들어감
                    count += 1  # 조건 만족하면 카운트 증가

    # 열 우선 탐색
    for j in range(N):  # 각 열에 대해 반복
        for i in range(N - K + 1):  # 연속 K칸 탐색 가능 범위 내에서 반복
            segment = [arr[i + x][j] for x in range(K)]  # 세로로 K칸 뽑아 리스트로 만듦
            if segment == [1] * K:  # 뽑은 구간이 전부 1인지 확인
                top = i == 0 or arr[i - 1][j] == 0  # 위쪽이 경계 밖이거나 0인지 확인
                bottom = i + K == N or arr[i + K][j] == 0  # 아래쪽이 경계 밖이거나 0인지 확인
                if top and bottom:  # 양쪽이 막혀 있어야 단어가 딱 들어감
                    count += 1  # 조건 만족하면 카운트 증가

    print(f"#{t} {count}")  # 테스트 케이스 번호와 함께 결과 출력
