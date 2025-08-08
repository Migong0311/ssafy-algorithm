# 테스트 케이스는 총 10개로 고정되어 있음
for t in range(1, 11):

    # 테스트 케이스 번호 읽기
    tc = int(input())

    # 100x100 크기의 사다리판 데이터를 이중 리스트로 받기
    ladder = []
    for _ in range(100):
        row = input().split()
        temp = []
        for r in row:
            temp.append(int(r))
        ladder.append(temp)

    # 도착지점(값이 2인 위치)의 x 좌표를 찾음
    for x in range(100):
        if ladder[99][x] == 2:  # 맨 아래 행에서 2를 찾음
            start_x = x  # 해당 x 좌표가 출발점
            break

    # 방향 이동을 위해 변수 설정
    y = 99  # y는 아래에서 위로 올라가므로 99부터 시작
    x = start_x  # x는 도착 지점에서 시작

    # 방문 여부는 필요 없음 (1인 곳만 따라가므로)
    while y > 0:
        # 왼쪽으로 이동 가능한지 확인 (x>0은 index error 방지)
        if x > 0 and ladder[y][x - 1] == 1:
            # 왼쪽 끝까지 이동
            while x > 0 and ladder[y][x - 1] == 1:
                x -= 1
            y -= 1  # 이후 위로 한 칸 이동

        # 오른쪽으로 이동 가능한지 확인
        elif x < 99 and ladder[y][x + 1] == 1:
            # 오른쪽 끝까지 이동
            while x < 99 and ladder[y][x + 1] == 1:
                x += 1
            y -= 1  # 이후 위로 한 칸 이동

        # 좌우 모두 없으면 위로 이동
        else:
            y -= 1

    # 출력은 형식에 맞게
    print(f"#{tc} {x}")