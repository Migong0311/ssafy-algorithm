'''
버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
'''


def drive(K, N):
    # k = 한 번 충전시 이동 가능 거리
    # N = 버스 도착 마지막 번호

    # return ==  0 : 버스가 마지막까지 도착 하지 못함
    # return >  0 : 버스가 마지막까지 도착함
    last = 0  # 마지막 충전위치
    bus = K  # 최대 이동 거리
    count = 0  # 충전횟수 시작횟수는 재외
    # 버스 위치가 N보다 작으면 계속 움직여라
    while bus < N:
        # 현재 위치 충전기 유무확인
        # 없으면 다시 한칸씩 돌아오기
        while stop[bus] == 0:
            bus -= 1
            # 마지막 운행지로 돌아오면 운행 불가
            if bus == last:
                return 0

        # stop[bus] == 1 만나면 반복 중단
        # 더 갈수 있다는 것을 의미
        # 마지막 충전 위치 현재 위치로 기록
        last = bus
        # 충전했으니 충전 횟수 +1
        count += 1
        # 충전했으니 K칸만큼 쭉 땡기기
        bus += K
    return count


T = int(input())

for t in range(1, T + 1):
    K, N, M = map(int, input().split())
    # k = 한 번 충전시 이동 가능 거리
    # N = 버스 도착 마지막 번호
    # M = 충전기 개수
    charger_list = list(map(int, input().split()))
    # 정류장 번호는 0번부터 N번까지 존재하므로 N+1 크기로 생성한다.
    stop = [0] * (N + 1)  # 정류장 리스트
    # stop[1] == 1 1번엔 없다
    # stop[2] == 2 2번엔 없다
    for i in charger_list:
        stop[i] = 1  # 있으면 1
    result = drive(K, N)
    print(f'#{t} {result}')
