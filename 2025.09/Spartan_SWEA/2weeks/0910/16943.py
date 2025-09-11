'''
16943. 4일차 응용 - 이진 탐색
'''


def alt_binary_search(A, x):
    l, r = 0, len(A) - 1  # 탐색 구간: 처음은 배열 전체
    prev = 0  # 직전 선택 방향 (0: 시작 전, -1: 왼쪽, +1: 오른쪽)

    while l <= r:  # 탐색 구간이 남아있는 동안 반복
        m = (l + r) // 2  # 중앙 인덱스 계산
        if A[m] == x:  # 중앙 원소가 찾는 값이라면
            return True  # 조건과 관계없이 성공 (탐색 종료)

        if A[m] < x:  # 중앙값이 찾는 값보다 작으면
            # 오른쪽 구간 선택
            if prev == +1:  # 직전에도 오른쪽을 갔다면 -> 같은 방향 연속 선택 -> 실패
                return False
            prev = +1  # 이번 방향은 오른쪽
            l = m + 1  # 탐색 범위를 오른쪽 절반으로 줄임
        else:  # 중앙값이 찾는 값보다 크면
            # 왼쪽 구간 선택
            if prev == -1:  # 직전에도 왼쪽을 갔다면 -> 같은 방향 연속 선택 -> 실패
                return False
            prev = -1  # 이번 방향은 왼쪽
            r = m - 1  # 탐색 범위를 왼쪽 절반으로 줄임

    return False  # 끝까지 못 찾으면 실패


T = int(input())  # 테스트 케이스 개수 입력
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N: 리스트 A 크기, M: 리스트 B 크기
    A = list(map(int, input().split()))  # A 리스트 입력
    B = list(map(int, input().split()))  # B 리스트 입력

    A.sort()  # A를 정렬 (이진 탐색 조건)

    ans = 0  # 조건을 만족하는 원소 개수
    for x in B:  # B의 각 원소에 대해
        if alt_binary_search(A, x):  # 조건 만족하면
            ans += 1  # 카운트 증가

    print(f"#{tc} {ans}")  # 테스트 케이스별 정답 출력
