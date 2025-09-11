## 스도쿠 검증 함수

# 스도쿠 검증 함수 생성
def checkSudoku(M):
    for i in range(9):  # 0번째 행/열부터 8번째 행/열까지 순회
        row_num = [0] * 10  # 행에서 숫자 사용 여부 체크 (1~9 인덱스 활용)
        col_num = [0] * 10  # 열에서 숫자 사용 여부 체크 (1~9 인덱스 활용)
        for j in range(9):  # 각 행과 열을 순회
            # 가로 검사: i번째 행, j번째 열 원소
            row = M[i][j]
            # 세로 검사: j번째 행, i번째 열 원소
            col = M[j][i]

            # 이미 행에 같은 숫자가 있다면 0 반환 (스도쿠 조건 위배)
            if row_num[row]:
                return 0
            # 이미 열에 같은 숫자가 있다면 0 반환 (스도쿠 조건 위배)
            if col_num[col]:
                return 0

            # 처음 등장한 숫자라면 해당 위치를 1로 기록
            row_num[row] = 1
            col_num[col] = 1

            # 3x3 작은 정사각형 검사 (i, j가 3의 배수일 때만 검사 시작)
            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10  # 3x3 내 숫자 사용 여부 체크
                for r in range(i, i + 3):  # 3행 순회
                    for c in range(j, j + 3):  # 3열 순회
                        num = M[r][c]
                        # 이미 사용된 숫자면 0 반환
                        if square[num]:
                            return 0
                        # 처음 등장한 숫자는 기록
                        square[num] = 1

    # 모든 조건을 통과하면 유효한 스도쿠 -> 1 반환
    return 1


# 테스트 케이스 개수 입력
T = int(input())
for tc in range(1, T + 1):
    # 9x9 스도쿠 보드 입력
    mat = [list(map(int, input().split())) for _ in range(9)]

    # 스도쿠 검증 함수 호출
    result = checkSudoku(mat)

    # 결과 출력 (f-string 사용)
    print(f'#{tc} {result}')
