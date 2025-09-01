'''
2072. 홀수만 더하기
출처 : https://buly.kr/1c9huEg
'''

# import sys

# sys.stdin = open('input.txt', 'r')
T = int(input())  # 테스트 케이스 입력

for t in range(1, T + 1):  # test case 입력 값 만큼 순회
    arr = list(map(int, input().split()))  # 입력 받는 값들을 리스트로 입력받음
    odd_num = []  # 홀수를 담을 리스트
    for i in range(len(arr)): # 입력 받을 리스트 길이 만큼 순회
        if arr[i] % 2 == 1: # 순회 중 만일 홀수를 찾을 시
            odd_num.append(arr[i]) # 홀수를 담을 리스트에 추가
        result = sum(odd_num) # 리스트 속 요소 즉, 홀수들의 합을 result 변수에 할당
    print(f'#{t} {result}') # 출력 형식에 맞게 설정
