'''
...(중략)
그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.
빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.

현재 건물이 양 옆 두 칸씩 총 4개의 건물보다 모두 더 높아야 조망이 확보된다.


당신이 한 건물(building[answer])에 살고 있다고 가정
당신은 양쪽 창문을 열고 풍경을 보고 싶음

하지만,
당신 집 바로 양옆 1칸, 2칸 거리에
(buildings[answer - 1],
buildings[answer - 2],
buildings[answer + 1],
buildings[answer + 2])
이웃집들이 존재
이 이웃집들 중 조금이라도 더 높은 집이 하나라도 있다면, 풍경은 가려짐

마치 내가 롤러코스터 제일 높은 지점에 있어야
모든 아래 풍경이 보이는 것과 같은 원리

'''

# 양쪽 2곳은 0 0 ~~~ 0 0
# 테스트케이스는 10개로 고정
T = 10

for t in range(1, T + 1):
    N = int(input())  # 건물 개수
    buildings = list(map(int, input().split()))  # 건물 높이 정보 리스트

    total_view = 0  # 전체 조망 세대 수 초기화

    # 양끝 2칸은 조망권을 가질 수 없으므로 2부터 N-2 전까지 반복
    for i in range(2, N - 2):
        curr = buildings[i]  # 현재 위치 건물 높이

        # 왼쪽 두 칸
        left1 = buildings[i - 1]
        left2 = buildings[i - 2]

        # 오른쪽 두 칸
        right1 = buildings[i + 1]
        right2 = buildings[i + 2]

        # 네 칸 중에서 가장 높은 값 직접 구하기
        max_neighbor = left1 # 첫 기준값은 왼쪽 1칸

        if left2 > max_neighbor:
            max_neighbor = left2 # 왼쪽 2칸이 더 높으면 교체

        if right1 > max_neighbor:
            max_neighbor = right1 # 오른쪽 1칸이 더 높으면 교체

        if right2 > max_neighbor:
            max_neighbor = right2 # 오른쪽 2칸이 더 높으면 교체

        # 현재 건물이 주변 4칸보다 모두 높을 경우만 조망 확보
        if curr > max_neighbor:
            view = curr - max_neighbor  # 확보된 세대 수
            total_view += view  # 누적 합산

    print(f'#{t} {total_view}')


