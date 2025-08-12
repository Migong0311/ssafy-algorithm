# import sys
#
# sys.stdin = open('input.txt', 'r')

T = int(input())  # 테스트 케이스 입력

for tc in range(1, T + 1):
    txt = input()  # 온전한 형태이거나 괄호만 남긴 한 줄의 코드 추가

    top = -1  # 탐색지점은 아예없는 인덱스인 -1부터 시작
    stack = [0] * 100  # 100칸의 스택 생성

    ans = 1  # default True -> 괄호 쌍이 맞음

    for i in txt:  # 입력받은 괄호넣은 문장 순회
        if i == '(' or i == '{':  # 열린괄호라면? 중괄호 포함
            top += 1  # 탐색지점 증가
            stack[top] = i  # i번째 값을 stack 에 push
        elif i == ')' or i == '}':  # 닫힌 괄호라면?
            if (stack[top] == '(' and i == ')') or (stack[top] == '{' and i == '}'): # 괄호와 중괄호가 닫히는 방식이 올바른지 검증
                top -= 1 # pop 실행
            else:
                ans = 0 # 짝이 안맞는다면 False
                break
        else:
            pass
    if top != -1:  # 만일 스택에 남은 열린 괄호가 남아있다면
        ans = 0  # return false

    print(f'#{tc} {ans}')  # 출력 형식에 맞게 설정
