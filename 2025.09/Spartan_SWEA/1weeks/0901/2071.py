'''
2071. 평균값 구하기
출처 : https://buly.kr/9iGZ2Er
'''

import sys

sys.stdin = open('input.txt', 'r')
T = int(input())  # 테스트 케이스 입력

for t in range(1, T + 1):  # test case 입력 값 만큼 순회
    arr = list(map(int, input().split()))  # 입력 받는 값들을 리스트로 입력받음
    avg = sum(arr) / len(arr) # 평균값 = 입력받은 배열의 합 / 배열 길이
    # 그냥 출력하면 소수점이 나오니까 정수형태로 출력
    # 단, 요구사항에 반올림 하라고 했으니 int 형 변환이 아닌 built in function인 round() 시용
    result = round(avg)

    print(f'#{t} {result}') # 출력 형식에 맞게 설정