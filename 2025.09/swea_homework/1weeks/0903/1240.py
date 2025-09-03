import sys

sys.stdin = open('test.txt', 'r')
'''
1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드
'''
'''
2차원 0/1 배열에서 56비트(7비트 × 8개)의 암호코드를 찾아 해독/검증
오른쪽 끝에서부터 '1'을 찾으면 그 지점이 코드의 끝
(홀수합 * 3 + 짝수합) % 10 == 0 이면 유효, 합을 출력 / 아니면 0
'''

code_table = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9,
}


def decode_56bits(code):
    """
    56비트 문자열을 7bit 씩 8개로 나눠 8개 숫자 리스트로 변환
    :param code: 7비트×8개 코드
    :return: 해독된8자리 숫자결과,True or False
    """
    digits = []  # 해독된 8자리 숫자 결과 저장
    for k in range(0, 56, 7):  # 0,7,14 ... ,49 시작 인덱스
        seg = code[k:k + 7]  # 7비트 조각 추출
        if seg not in code_table:  # 매핑 테이블에 없으면 실패
            return [], False
        digits.append(code_table[seg])  # 매핑 성공 시 숫자 추가
    return digits, True  # 전부 성공 시 결과 리턴


def valid_and_sum(digits):
    """
    검증식 확인 후 유용한 결과는 합계
    공식은  (홀수 자리의 합 x 3) + (짝수 자리의 합)이 10의 배수
    자리 인덱스는 1~8 (사람 기준) dights 인덱스 기준
    홀수 : 0,2,4,6
    짝수 : 1,3,5,7
    :param digits: 해독성공 결과
    :return: 0 무효한 결과 시 반환값
    """
    odd_sum = digits[0] + digits[2] + digits[4] + digits[6]  # 홀수 자리 합
    even_sum = digits[1] + digits[3] + digits[5] + digits[7]  # 짝수 자리 합
    check = odd_sum * 3 + even_sum  # (홀수 자리의 합 x 3) + (짝수 자리의 합)
    if check % 10 == 0:  # 10의 배수에 해당되나
        return sum(digits)  # 그라문 더해라
    return 0  # 안되문 때리 치아라


# 코드 찾기 시작
def find_code(N, M, grid):
    for i in range(N):  # 모든 행을 순회
        row = grid[i]  # 현재 행(문자열)
        # j는 열 번호이데 뒤에서부터 1 찾기 시작
        # 왜 1을찾느냐 모든 암호 코드는 1로 끝남
        # 0으로 시작하는것도 당연하지만 0이 암호코드에 포함되는지 아닌지 확인
        for j in range(M - 1, 55, -1):
            if row[j] == '1':
                # 암호코드가 끝나는 위치j를 발견했으니까
                # [j-55,j+1]가 암호코드 후보 범위
                code = row[j - 55:j + 1]
                # code 를 앞에서부터 7개씩 잘라서 code_table에 일치하는 코드가 있는지 확인
                digits, ok = decode_56bits(code)  # 7비트×8개 해독
                if ok:  # 해독 성공 시 검증
                    return valid_and_sum(digits)
    return 0  # 끝까지 못 찾았거나 모두 무효


T = int(input())

# __main__
for t in range(1, T + 1):
    # N: 세로, M: 가로
    N, M = map(int, input().split())
    # N줄의 0/1 문자열을 그대로 저장
    arr = [input() for _ in range(N)]
    # 암호코드 찾기/해독/검증
    result = find_code(N, M, arr)
    # 형식에 맞게 출력
    print(f'#{t} {result}')
