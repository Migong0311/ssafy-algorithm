import sys  # 표준 입출력 제어용 모듈

sys.stdin = open('input.txt', 'r')  # 로컬 테스트 시 사용 (채점 환경에서는 주석 처리 권장)

T = int(input().strip())  # 테스트 케이스 개수 입력

# 방향 문자와 델타 이동, 전차 기호 매핑
DIRS = {
    'U': (-1, 0, '^'),
    'D': (1, 0, 'v'),
    'L': (0, -1, '<'),
    'R': (0, 1, '>')
}
# 전차 기호에서 현재 방향 키를 역으로 알아내기 위한 매핑
TANK_TO_DIRKEY = {
    '^': 'U',
    'v': 'D',
    '<': 'L',
    '>': 'R'
}

for tc in range(1, T + 1):  # 각 테스트 케이스 처리
    H, W = map(int, input().split())  # 맵의 높이 H, 너비 W
    grid = [list(input().rstrip()) for _ in range(H)]  # 맵을 문자 2차원 리스트로 저장

    # 전차의 초기 위치와 방향 찾기
    tank_r, tank_c = -1, -1  # 전차 좌표 초기화
    dir_key = 'U'            # 기본값(임시), 곧 실제 기호로부터 역매핑
    for r in range(H):
        for c in range(W):
            if grid[r][c] in TANK_TO_DIRKEY:  # 전차 기호를 발견하면
                tank_r, tank_c = r, c         # 전차 좌표 기록
                dir_key = TANK_TO_DIRKEY[grid[r][c]]  # 현재 방향 키로 변환
                break
        if tank_r != -1:
            break

    N = int(input().strip())  # 명령 개수
    cmds = input().strip()    # 명령 문자열

    # 명령 처리
    for cmd in cmds:
        if cmd in 'UDLR':  # 이동 관련 명령
            dr, dc, face = DIRS[cmd]     # 해당 명령의 델타와 전차 기호
            dir_key = cmd                # 전차의 현재 방향 갱신
            # 우선 바라보는 방향 기호만 바꿈
            grid[tank_r][tank_c] = face

            # 이동 가능한지 확인: 맵 안이면서 다음 칸이 평지('.')
            nr, nc = tank_r + dr, tank_c + dc
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == '.':
                # 이동: 현재 칸을 평지로 만들고, 다음 칸에 전차 기호 배치
                grid[tank_r][tank_c] = '.'
                grid[nr][nc] = face
                tank_r, tank_c = nr, nc  # 전차 좌표 갱신

        elif cmd == 'S':  # 포격
            # 현재 방향으로 직진하며 처리
            dr, dc, _ = DIRS[dir_key]  # 현재 바라보는 방향의 델타
            sr, sc = tank_r, tank_c    # 시작 위치(전차 위치)
            r, c = sr + dr, sc + dc    # 포탄은 전차 바로 앞 칸부터 시작
            # 맵을 벗어나거나 벽을 만날 때까지 전진
            while 0 <= r < H and 0 <= c < W:
                if grid[r][c] == '*':   # 벽돌벽이면 파괴 후 종료
                    grid[r][c] = '.'
                    break
                elif grid[r][c] == '#': # 강철벽이면 아무 변화 없이 종료
                    break
                else:
                    # 평지('.') 또는 물('-') 등은 통과만 함
                    r += dr
                    c += dc
        # 그 외 문자는 없음(입력 보장)

    # 최종 맵 출력
    print(f"#{tc}", end=" ")
    for r in range(H):
        print(''.join(grid[r]))
# test