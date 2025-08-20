"""
1225 암호생성기
"""

from collections import deque  # 큐 연산을 효율적으로 하기 위해 deque 사용

# 총 10개의 테스트 케이스 처리
for _ in range(10):
    tc = int(input())          # 테스트케이스 번호 입력
    nums = list(map(int, input().split()))  # 8개의 숫자 입력

    q = deque(nums)   # 숫자 8개를 큐로 변환
    dec = 0           # 감소량 초기값(사이클 1~5를 만들기 위해 0에서 시작)

    while True:
        dec = (dec % 5) + 1    # 감소량: 1,2,3,4,5 다시 1,2 ...
        x = q.popleft()        # 큐 맨 앞의 값을 꺼냄
        x -= dec               # 규칙에 따라 감소

        if x <= 0:             # 0 이하가 되면
            q.append(0)        # 0으로 고정하여 뒤에 넣음
            break              # 사이클 종료(암호 완성)
        else:
            q.append(x)        # 아직 0보다 크면 뒤로 이동시켜 계속 진행

    # 출력 형식: #번호 + 공백 + 암호 8자리
    print(f"#{tc}", *q)