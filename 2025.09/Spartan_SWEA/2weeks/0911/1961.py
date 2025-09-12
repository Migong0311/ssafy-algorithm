

'''
1961. 숫자 배열 회전
'''


# 90도 회전함수
def rotate(mat):
    n = len(mat)  # 행렬크기
    res = [[0] * n for _ in range(n)]  # 회전된결과를 저장할 n*n행렬
    for i in range(n):  # 회전한 행 인덱스
        for j in range(n):  # 회전한 열 인덱스
            '''
            새로운행 = 예전열
            새로운열 = (맨 끝에서부터) 예전행

            '''
            res[i][j] = mat[n - 1 - j][i]
    return res  # 회전한 결과값 반환


T = int(input())
for t in range(1, T + 1):
    N = int(input())  # 가로세로 길이
    arr = [list(map(int, input().split())) for _ in range(N)]  # 초기 N * N 베열 입력

    r90 = rotate(arr)  # 90도회전
    r180 = rotate(r90)  # 180도회전
    r270 = rotate(r180)  # 270도회전

    print(f'#{t}')
    for answer in range(N):
        s90 = ''.join(map(str, r90[answer]))  # 90도 회전 결과의 i번째 행 (숫자를 붙여 문자열로 변환)
        s180 = ''.join(map(str, r180[answer]))  # 180도 회전 결과의 i번째 행
        s270 = ''.join(map(str, r270[answer]))  # 270도 회전 결과의 i번째 행
        print(s90, s180, s270)  # 회전된 결과값 출력
