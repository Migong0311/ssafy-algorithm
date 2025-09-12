"""
1244. [S/W 문제해결 응용] 2일차 - 최대 상금
- 숫자판의 자리를 정확히 cnt번 교환하여 만들 수 있는 최대 금액을 구한다.
- DFS로 모든 answer < j 교환을 탐색하되, (k, 상태) 방문 체크로 중복을 가지치기한다.
"""

T = int(input())  # 테스트 케이스 개수


def solve_max_prize(nums_str, cnt):
    """
    nums_str: 숫자판을 문자열로 받은 값 예) '32888'
    cnt: 반드시 수행해야 하는 교환 횟수
    반환값: 정확히 cnt번 교환하여 만들 수 있는 최대 정수 값
    """
    digits = list(nums_str)  # 자리 교환이 쉬우도록 리스트로 변환
    n = len(digits)  # 자리수 길이
    visited = set()  # (교환횟수k, 상태문자열) 방문 집합
    best = [0]  # 최댓값을 외부 스코프에서 갱신하기 위한 리스트 래핑

    def dfs(k):
        """
        k: 지금까지 수행한 교환 횟수
        깊이가 cnt에 도달하면 현재 숫자값으로 최댓값 갱신
        가지치기: (k, 상태) 중복 방문 방지
        """
        state = ''.join(digits)  # 현재 숫자열 상태
        key = (k, state)  # 방문 키
        if key in visited:  # 이미 같은 깊이에서 같은 상태를 본 적이 있다면
            return  # 중복 가지치기
        visited.add(key)  # 방문 기록 추가

        if k == cnt:  # 종료 조건: 정확히 cnt번 교환 완료
            val = int(state)  # 현재 숫자열을 정수로 변환
            if val > best[0]:  # 최댓값 갱신
                best[0] = val
            return

        # 다음 단계: 모든 answer < j 쌍에 대해 자리 교환 시도
        for i in range(n - 1):  # 앞자리 인덱스 answer
            for j in range(i + 1, n):  # 뒷자리 인덱스 j
                # 자리 교환
                digits[i], digits[j] = digits[j], digits[i]
                # 다음 교환 횟수로 재귀
                dfs(k + 1)
                # 원상 복구
                digits[i], digits[j] = digits[j], digits[i]

    dfs(0)  # 교환 0회에서 시작
    return best[0]  # 최종 최댓값 반환


for t in range(1, T + 1):
    # 한 줄에 "숫자판 교환횟수" 형태로 주어진다 예) "32888 2"
    nums_str, cnt_str = input().split()  # 숫자판과 교환 횟수 문자열 분리
    cnt = int(cnt_str)  # 교환 횟수 정수 변환

    ans = solve_max_prize(nums_str, cnt)  # 최대 상금 계산
    print(f"#{t} {ans}")  # 출력 형식에 맞게 출력
