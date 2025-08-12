import sys

sys.stdin = open('input.txt', 'r')

for t in range(1, 11): # 테스트 케이스 10개
    N, pwd = input().split() # 입력 자리수(N)와 비밀번호(pwd)를 각각 입력

    stack = [] # 비밀번호가 담길 스택

    # 비밀번호 전체를 순회하며 중복되는 번호 pop
    # 예를 들어 1238099084는 우선 중복되는 번호를 찾은후 pop
    # 12380084 그다음 00 ->123884 그다음 88 -> 1234
    # 더이상 중복되는 숫자가 없으므로 return
    for i in pwd:
        if not stack: # 비어있으면
            stack.append(i) # push
        else:
            if i == stack[-1]: # 순환하면서 이전인덱스와 동일하면
                stack.pop() # pop
            else:
                stack.append(i) # 해당되지않으면 push

    print(f'#{t} {"".join(stack)}') # 출력 형식에 맞춰 설정
