import sys
#
sys.stdin = open('input.txt', 'r')

T= int(input())
for t in range(1,T+1):
    txt = input() # 문자열 입력받음
    stack = []
    # data 하나씩 읽으면서 push
    # 만약에 top에 있는 요소가 나랑 같으면,pop 아니면 push
    for i in txt:
        # 1번부터 끝까지 순회 만약 같다면 pop
        # 계속 순회 후 달라질때 까지 순회후 다르다면
        if not stack:
            # 비어있을 경우 push해주기
            stack.append(i)
        else:
            if i == stack[-1]: # 입력받은값이 이전 인덱스 값과 같다면
                stack.pop() # pop 해줌
            else:
                stack.append(i) # 아니면 push
    print(f'#{t} {len(stack)}') # 최종 값의 length를 리턴
