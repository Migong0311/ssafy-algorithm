import sys
sys.stdin = open('input.txt','r')

# 가로 구간이 회문인지 판정하는 함수
def is_pal_row(board, r, c, N):
    i = 0  # 비교를 진행할 내부 인덱스 i를 0으로 초기화
    # i가 N의 절반에 도달할 때까지 양끝에서 안쪽으로 이동하며 비교
    while i < N // 2:  # 두 포인터 방식으로 N//2번 비교하면 충분
        left_ch = board[r][c + i]  # 구간의 왼쪽 문자: 행 r, 열 (c+i)
        right_ch = board[r][c + (N - 1 - i)]  # 구간의 오른쪽 문자: 행 r, 열 (c+N-1-i)
        if left_ch != right_ch:  # 한 쌍이라도 다르면
            return 0  # 회문이 아니므로 즉시 0 반환
        i += 1  # 다음 비교를 위해 i를 1 증가
    return 1  # 모든 쌍이 같다면 회문이므로 1 반환


# 세로 구간이 회문인지 판정하는 함수
def is_pal_col(board, r, c, N):
    i = 0  # 내부 인덱스 i 초기화
    while i < N // 2:  # 위아래에서 가운데로 수렴하며 비교
        top_ch = board[r + i][c]  # 구간의 위쪽 문자: 행 (r+i), 열 c
        bottom_ch = board[r + (N - 1 - i)][c]  # 구간의 아래쪽 문자: 행 (r+N-1-i), 열 c
        if top_ch != bottom_ch:  # 서로 다르면
            return 0  # 회문 아님
        i += 1  # 다음 비교로 이동
    return 1  # 끝까지 통과하면 회문


# 8x8 보드에서 길이 N의 회문 개수를 가로·세로 전부 세는 함수
def count_palindromes(board, N):
    count = 0  # 최종 회문 개수 누적 변수

    # 1) 가로 방향 검사
    r = 0  # 행 인덱스 r을 0부터 시작
    while r < 8:  # 8행 모두 탐색
        c = 0  # 각 행에서 시작 열 c를 0으로 초기화
        while c <= 8 - N:  # 길이 N 구간이 벗어나지 않는 최대 시작열은 8-N
            # 행 r, 시작열 c에서 길이 N 구간을 회문 판정
            count += is_pal_row(board, r, c, N)  # 회문이면 1, 아니면 0 더해짐
            c += 1  # 시작열을 오른쪽으로 한 칸 이동
        r += 1  # 다음 행으로 이동

    # 2) 세로 방향 검사
    c = 0  # 열 인덱스 c를 0부터 시작
    while c < 8:  # 8열 모두 탐색
        r = 0  # 각 열에서 시작 행 r을 0으로 초기화
        while r <= 8 - N:  # 길이 N 구간이 벗어나지 않는 최대 시작행은 8-N
            # 열 c, 시작행 r에서 길이 N 구간을 회문 판정
            count += is_pal_col(board, r, c, N)  # 회문이면 1, 아니면 0 더해짐
            r += 1  # 시작행을 아래로 한 칸 이동
        c += 1  # 다음 열로 이동

    return count  # 가로+세로 전체 회문 개수 반환


tc = 1  # 테스트 케이스 번호를 1부터 시작
while tc <= 10:  # 총 10개 케이스 처리
    N = int(input().strip())  # 회문 길이 N 입력
    board = []  # 8줄 보드를 저장할 리스트
    i = 0  # 줄 수 카운터 초기화
    while i < 8:  # 정확히 8줄을 읽어 보드 구성
        line = input().strip()  # 공백 제거된 한 줄
        board.append(line)  # 보드에 추가
        i += 1  # 줄 수 1 증가

    ans = count_palindromes(board, N)  # 현재 케이스의 회문 개수 계산
    print("#" + str(tc) + " " + str(ans))  # 포맷에 맞춰 출력
    tc += 1
