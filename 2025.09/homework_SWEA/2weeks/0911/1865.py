# 동철이의 일 분배 - 재귀(백트래킹) 풀이



T = int(input())                     # 테스트케이스 개수 입력
for tc in range(1, T + 1):
    N = int(input())                 # 직원 수 == 일의 수
    P = [list(map(int, input().split())) for _ in range(N)]  # 확률 입력 (퍼센트 단위)

    # 확률을 0~1 사이 실수로 변환
    prob = [[p / 100.0 for p in row] for row in P]

    # 각 직원(행)에서 낼 수 있는 최대 확률
    row_max = [max(row) for row in prob]

    # suffix_max[i] = i번째 직원부터 끝까지 "각자 최대로 성공한다" 가정했을 때 곱
    # 가지치기(상한선 계산)에 사용
    suffix_max = [1.0] * (N + 1)
    for i in range(N - 1, -1, -1):           # 뒤에서부터 채워감
        suffix_max[i] = suffix_max[i + 1] * row_max[i]

    # order[i] = i번째 직원이 맡을 수 있는 일을 확률 큰 순서대로 정렬한 인덱스
    # 확률 높은 일부터 시도하면 빠르게 최적해에 도달 -> 가지치기 강화
    order = []
    for i in range(N):
        idxs = list(range(N))                # 가능한 일의 번호 0 ~ N-1
        idxs.sort(key=lambda j: prob[i][j], reverse=True)
        order.append(idxs)

    best = 0.0                               # 지금까지 찾은 최대 성공 확률 (곱)

    # i번째 직원부터 일을 배정하는 DFS
    # used_mask: 지금까지 배정된 일을 비트마스크로 기록 (1이면 이미 배정됨)
    # cur: 지금까지 배정된 확률의 곱
    def dfs(i, used_mask, cur):
        global best

        # 가지치기: 지금 확률 * 남은 직원들의 "최대 가능 확률" <= best면 더 볼 필요 없음
        if cur * suffix_max[i] <= best:
            return

        # 모든 직원 배정 완료 시
        if i == N:
            if cur > best:                   # 최댓값 갱신
                best = cur
            return

        # i번째 직원에게 가능한 일을 배정
        for j in order[i]:
            # j번째 일이 이미 배정됐으면 건너뜀
            if (used_mask >> j) & 1:
                continue
            # 확률이 0이면 시도할 필요 없음
            pj = prob[i][j]
            if pj == 0.0:
                continue
            # i번째 직원에게 j번 일을 배정하고 다음 직원으로 진행
            # used_mask | (1<<j) -> j번째 일을 이제 사용했다고 표시
            dfs(i + 1, used_mask | (1 << j), cur * pj)

    # DFS 시작: 0번째 직원부터, 아직 배정된 일 없고(cur=1.0)
    dfs(0, 0, 1.0)

    # 퍼센트 단위로 환산해서 소수점 6자리까지 출력
    print(f"#{tc} {best * 100:.6f}")
