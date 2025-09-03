'''
16788. 1일차 응용 - 이진수2
0보다 크고 1미만인 십진수 N을 이진수로
0.625를 이진 수로 바꾸면 0.101이 된다.

N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고,
 13자리 이상이 필요한 경우에는 ‘overflow’를 출력
'''

T = int(input().strip())  # 테스트 케이스 개수 입력

for tc in range(1, T + 1):
    N = float(input().strip())  # 변환할 소수 입력
    result = ""                 # 변환 결과를 저장할 문자열
    overflow = False            # 13자리 이상이 필요한지 여부

    for _ in range(12):         # 최대 12자리까지만 시도
        N *= 2                  # N에 2 곱하기
        if N >= 1:              # 정수부가 1인 경우
            result += '1'
            N -= 1              # 정수부 제거하고 소수부만 남김
        else:                   # 정수부가 0인 경우
            result += '0'

        if N == 0:              # 딱 떨어지면 종료
            break
    else:
        # for문이 정상 종료(12자리 다 써도 N이 0 안 됨) => overflow
        overflow = True

    if overflow:
        print(f"#{tc} overflow")
    else:
        print(f"#{tc} {result}")
