아래는 **화이트보드에 바로 적기 좋은 발표 흐름 요약**과, **`input()`만 사용**하도록 수정한 \*\*파이썬 전체 코드(라인별 주석 포함, 생략 없음)\*\*입니다.

---

# 🧾 화이트보드용 발표 흐름 요약

## 0) 문제 목표

* 중위표기식 → **후위표기식 변환** → **후위식 계산**
* 연산자: `+`, `*` (우선순위 `*` > `+`), 피연산자: 한 자리 정수

---

## 1) 후위 변환(Shunting-yard 간소화)

1. **왼→오 스캔**
2. **숫자**: 곧바로 출력
3. **연산자(+/\*)**:

   * 스택 top과 **우선순위 비교**
   * top 우선순위 **≥ 현재** → pop하여 출력, 반복
   * 현재 연산자 push
4. **끝**: 스택 남은 연산자 모두 출력

> 핵심: `*`가 `+`보다 높다. (괄호 없음, 좌결합)

---

## 2) 후위식 계산(값 스택)

1. **왼→오 스캔**
2. **숫자**: push
3. **연산자**: 두 개 pop → `a op b` → 결과 push
   *(두 번째 pop가 a, 첫 번째 pop가 b 순서 주의)*
4. **끝**: 스택의 마지막 값이 정답

---

## 3) 시간 복잡도

* 변환 O(N) + 계산 O(N) = **O(N)**

---

# 🧑🏻‍💻 파이썬 로직 (`input()`만 사용, 라인별 주석)

```python
# =========================
# 연산자 우선순위 함수
# =========================
def precedence(op):
    # '+'는 1, '*'는 2 (곱셈이 더 높은 우선순위)
    if op == '+':
        return 1
    if op == '*':
        return 2
    return 0  # 안전장치

# =========================
# 중위 → 후위 변환 (Shunting-yard 간소화)
# =========================
def infix_to_postfix(expr: str) -> str:
    output = []     # 후위표기 결과를 담을 리스트
    op_stack = []   # 연산자 스택

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

# =========================
# 후위 표기식 계산
# =========================
def eval_postfix(postfix: str) -> int:
    val_stack = []  # 값 스택

    for ch in postfix:
        if '0' <= ch <= '9':
            # 1) 피연산자면 정수로 변환하여 push
            val_stack.append(int(ch))
        elif ch == '+' or ch == '*':
            # 2) 연산자면 두 값 pop → 연산 → push
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

# =========================
# 메인: input()으로 10개 케이스 처리
# =========================
def main():
    # 문제 명시: 총 10개의 테스트 케이스
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

# 스크립트 직접 실행 시에만 main 호출
if __name__ == "__main__":
    main()
```

---

## ✅ 사용 방법 메모 (화이트보드 옆에 간단 표기용)

* 입력:
  `N` → `expr` (×10회 반복)
* 출력:
  `#케이스번호 결과`
* 체크 포인트:
  `*`의 우선순위 > `+`, 후위 계산 시 **pop 순서**(a, b) 유의
