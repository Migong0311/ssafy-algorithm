# 파라미터 n은 누적값
def KFC(n):
    if n == 3:  # 종료조건 = 3이되면 종료됨
        return
    print(n, end=',')

    KFC(n + 1)
    KFC(n + 1)
    print(n, end=',')


KFC(0)  # 시작점 0으로 설정
