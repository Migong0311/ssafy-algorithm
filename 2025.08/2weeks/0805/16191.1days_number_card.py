'''
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오.
 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
'''
# import sys
#
# sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    n = int(input())
    cards = list(map(int, input()))  # 예시 입력

    # 0~9 숫자 카운트용 배열
    count = [0] * 10

    # 1. 각 숫자의 개수를 센다
    for i in range(len(cards)):
        num = cards[i]
        count[num] += 1

    # 2. 가장 많이 나온 숫자 찾기 (횟수가 같으면 숫자가 더 큰 쪽 우선)
    max_count = -1
    max_number = -1

    for i in range(10):
        if count[i] > max_count:
            max_count = count[i]
            max_number = i
        elif count[i] == max_count and i > max_number:
            max_number = i

    # 3. 결과 출력
    print(f"#{t} {max_number} {max_count}")

# 1 9 2
# 2 8 1
# 3 7 3
