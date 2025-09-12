import sys

sys.stdin = open('algo1_sample_in.txt','r')

T = int(input())  # 테스트 케이스 입력

for t in range(1, T + 1):
    N, M, K = map(int, input().split())  # N : 전체크기 M : 찾는 범위, K: 찾는 별의 개수
    arr = [list(map(str, input())) for _ in range(N)]  # N * N 정사각형 배열 입력

    # 우선 전체 범위(N * N)에서 M범위 만큼 제외하는 빌드업 과정
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            cnt_star = 0  # *의 개수 초기화
            for di in range(M):
                for dj in range(M):  # 찾고자 하는 범위안에서
                    cnt_star = arr[i + di][j + dj]
                    """
                    ❌ 문제 1:
                    여기서 cnt_star에 '*' 개수를 누적하지 않고, 
                    매번 arr[answer+di][j+dj]의 값(문자)을 그대로 '덮어쓰기' 하고 있음.
                    → int로 누적해야 하는데 str 할당을 하고 있어서 개수 세기가 불가능함.
                    """

                    if cnt_star == '*':  # cnt_star가 *인지 검증
                        cnt_star = K
                        """
                        ❌ 문제 2:
                        '*'일 경우 cnt_star를 1 증가시키는 것이 아니라 
                        K 값으로 '강제로 치환'해버림.
                        이렇게 하면 개수를 세는 로직이 아예 깨짐.
                        """

    print(f'#{t} {cnt_star} {cnt_star} ')
    """
    ❌ 문제 3:
    출력이 현재 영역의 시작 위치(row, col)가 아니라
    cnt_star를 그대로 두 번 출력하고 있음.
    원래 문제 요구사항은 별의 개수가 정확히 K개일 때 
    시작 위치 (row, col)를 출력해야 함.
    """

    if K != cnt_star:
        print(f'#{t} -1 -1')
        """
        ❌ 문제 4:
        K != cnt_star 조건은 루프가 끝난 뒤 전체 cnt_star 값에 대해서만 판단하는데,
        이 값은 마지막 영역의 결과만 반영되어 있음.
        즉, 중간에 맞는 영역이 나와도 무시될 수 있음.
        """
