# 25472. 16진수의합

# # 16진수 문자 -> 정수값 매핑 딕셔너리
# hex_n = {
#     'A': 10,
#     'B': 11,
#     'C': 12,
#     'D': 13,
#     'E': 14,
#     'F': 15,
#     'a': 10,
#     'b': 11,
#     'c': 12,
#     'd': 13,
#     'e': 14,
#     'f': 15,
# }

T = int(input())

for t in range(1, T + 1):
    N = int(input())  # 문자열 길이
    S = input().strip()  # 16진수 문자열

    total = 0  # 합계 초기화

    for i in S:  # 문자열의 각 자리 처리
        total += int(i,16)  # 그대로 정수 변환해서 더함

    print(f'#{t} {total}')
