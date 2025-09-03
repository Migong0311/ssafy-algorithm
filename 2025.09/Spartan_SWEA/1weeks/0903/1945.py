'''
1945. 간단한 소인수분해
출처 : https://buly.kr/881kiw1
'''

# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 소인수분해할 숫자
    N = int(input())

    # 밑은 문제에 제시한 값을 리스트 형태로 저장
    arr = [2, 3, 5, 7, 11]
    # a,b,c,d,e 에 들어갈 숫자
    square = [0] * 5
    for i in range(5):
        # i(밑)으로 나누었을 때 나머지가 0이면 지수 1 추가 + N으로 나누기
        # i로 나누어지지 않을 때까지
        while N % arr[i] == 0:
            # 각각 제곱에 들어갈 숫자 증가
            square[i] += 1
            # 입력한 N값을 밑의 i값의 몫을 다시 N값으로 할당
            N //= arr[i]

    print(f'#{t}', *square)  # 출력형식에 맞게 설정
