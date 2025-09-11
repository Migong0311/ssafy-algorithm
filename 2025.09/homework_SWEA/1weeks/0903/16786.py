'''
16786. 1일차 응용 - 이진수
'''

# import sys
# sys.stdin = open('test.txt','r')

T = int(input())

for t in range(1,T+1):
    N,hex_string = input().split()

    # N만 숫자로
    N = int(N)

    # 16진수 -> 2진수
    # 변환표 만들기
    hex_to_bin = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    # 결과로 만들 2진수 문자열
    result_bin = ''

    # 변환표 참고해서 2진수로 바꾸기
    for i in hex_string:
        result_bin += hex_to_bin[i]

    print(f'#{t} {result_bin}')
