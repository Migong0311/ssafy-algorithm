'''
16979. 5일차 응용 - 최소 생산 비용
'''

T = int(input())


# idx : 단계 이 문제에선 공장의 번호
# selected : 내가 지금까지 생산한 제품번호 모음
# now_cost : 현재 단계까지 선택한 공장들의 비용 합
# idx번 공장에서 생산할 제품을 고르는 것
def perm(idx, selected, now_cost):
    global min_cost

    # 현재단계까지 계산한 비용 now_cost 보다
    # 이전에 내가 계산한 최소비용 min_cost 보다 큰 경우 답이 될 가능성 없음
    # 가지치기
    if now_cost >= min_cost:
        return

        # 종료조건
    if idx == N:
        # 모든 공장에서 어떤 제품을 생산할건지 선택 완료
        # 최소값을 비교해서 구하면 됨
        min_cost = min(now_cost, min_cost)
        return

        # recursion
    # idx번 공장에서 생산할 제품을 선택
    # 선택할 수 있는 가지수 최대 N개
    # 0부터 idx-1번 공장에서 생산했던 제품은 선택 불가

    # idx번 공장에서 j번 제품 생산
    for j in range(N):
        if j not in selected:
            # j번 제품을 이전에 생산한적이 없음
            selected.append(j)
            new_cost = now_cost + arr[j][idx]
            # idx + 1번 공장으로 생산한 제품번호 목록 지금까지 생산비용
            perm(idx + 1, selected, new_cost)
            # j번 제품 생산 기록 취소
            selected.pop()


for t in range(1, T + 1):
    # 제품 공장 개수
    N = int(input())
    # 생산비용 표
    # i번 제품을 j번 공장에서 생산하는 비용
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 문제 최소값
    min_cost = 10 ** 10

    # 공장 순서는 고정 제품순서만 바꿔서 순열만드록
    # 공장에서 생산하는 제품의 생산 비용을 모두 계싼해서 합핀후
    # 그 중 최소를 구하면 됨

    # perm(공장번호,지금까지 선택한 제품번호리스트,현재 단계까지 선택한 공장들의 비용 합
    perm(0, [], 0)

    print(f'#{t} {min_cost}')
