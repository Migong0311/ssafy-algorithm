

T = int(input())  # 테스트케이스 개수

for t in range(1, T + 1):
    num = int(input())  # baby-gin 확인할 6자리 수

    c = [0] * 12  # 숫자 개수 세기 위한 리스트 (0~11까지 인덱스 사용. run 체크시 answer+2 방지)

    # 숫자 등장 횟수 카운트
    for i in range(6):  # 6자리 수니까 6번 반복
        digit = num % 10  # 일의 자리 추출
        c[digit] += 1  # 해당 숫자의 개수 증가
        num //= 10  # 다음 자리 수로 이동

    i = 0
    tri = 0      # triplet 개수
    run_cnt = 0  # run 개수

    while i < 10:
        # triplet 처리
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue  # 같은 자리에서 한 번 더 검사 가능성

        # run 처리
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run_cnt += 1
            continue  # 같은 자리에서 한 번 더 검사 가능성

        i += 1  # 아무 것도 아니면 다음 숫자 자리로 이동

    # 출력 형식에 맞게 결과 출력
    if tri + run_cnt == 2:
        print(f"#{t} Baby Gin")
    else:
        print(f"#{t} Lose")
