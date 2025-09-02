'''
9367. 점점 커지는 당근의 개수
출처 : https://buly.kr/H6iOP5O
'''
import sys

sys.stdin = open('sample_input.txt', 'r')
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 연속된 오름차순 숫자 젤 마지막 출력
    # 만약 번호가 4 5 1 2 3 이면 가장 마지막으로 오름차순에 마지막으로 이어진 번호는 3
    # 그러니까 우선 최소값을 찾은후 우측을 비교해서 수가 더 작아지면 다시 처음부터 인식하도록 설계
    max_v = 1
    curr = 1

    for i in range(1, N):
        if arr[i] > arr[i - 1]:
            curr += 1
        else:
            curr = 1     # 만일 오른쪽으로 가도 숫자가 계속 작아질경우 1 출력

        if curr>max_v:
            max_v = curr
    print(f'#{t} {max_v}')
