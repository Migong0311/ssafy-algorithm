# 연산자 우선순위 함수

def precedence(op):
    # '+'는 1, '*'는 2 (곱셈이 더 높은 우선순위)
    if op == '+':
        return 1
    if op == '*':
        return 2
    return 0  # 안전장치


# 중위 -> 후위 변환 (Shunting-yard 간소화)

def infix_to_postfix(expr: str) -> str:
    output = []  # 후위표기 결과를 담을 리스트
    op_stack = []  # 연산자 스택

    # 수식을 왼쪽에서 오른쪽으로 한 글자씩 순회
    for ch in expr:
        if '0' <= ch <= '9':
            # 1) 피연산자(숫자): 바로 출력 리스트에 추가
            output.append(ch)
        elif ch == '+' or ch == '*':
            # 2) 연산자: 스택 top과 우선순위 비교
            #    top 우선순위가 현재 연산자보다 크거나 같으면 pop하여 출력
            while op_stack and precedence(op_stack[-1]) >= precedence(ch):
                output.append(op_stack.pop())
            #    현재 연산자를 push
            op_stack.append(ch)
        else:
            # 문제 조건상 등장하지 않음(공백/기타 문자 무시 가능)
            pass

    # 남은 연산자 모두 출력으로 이동
    while op_stack:
        output.append(op_stack.pop())

    # 리스트를 문자열로 합쳐 반환
    return ''.join(output)


# 후위 표기식 계산

def eval_postfix(postfix: str) -> int:
    val_stack = []  # 값 스택

    for ch in postfix:
        if '0' <= ch <= '9':
            # 1) 피연산자면 정수로 변환하여 push
            val_stack.append(int(ch))
        elif ch == '+' or ch == '*':
            # 2) 연산자면 두 값 pop -> 연산 -> push
            #    pop 순서 주의: 먼저 꺼낸 b가 오른쪽 피연산자
            b = val_stack.pop()
            a = val_stack.pop()
            if ch == '+':
                val_stack.append(a + b)
            else:  # ch == '*'
                val_stack.append(a * b)
        else:
            # 문제 조건상 등장하지 않음
            pass

    # 최종 결과(스택에 하나 남아야 함)
    return val_stack[-1]


T = 10
for tc in range(1, T + 1):
    # 1) 길이 N (사용하진 않지만 입력형식에 맞게 읽음)
    N_str = input().strip()
    # 혹시 공백/빈줄이 섞일 경우 대비하여, 숫자 나올 때까지 스킵
    while N_str == '':
        N_str = input().strip()
    # 정수 변환 (검증용)
    _N = int(N_str)

    # 2) 실제 수식 문자열
    expr = input().strip()

    # 3) 후위 변환
    postfix = infix_to_postfix(expr)

    # 4) 후위 계산
    ans = eval_postfix(postfix)

    # 5) 출력 형식
    print(f"#{tc} {ans}")