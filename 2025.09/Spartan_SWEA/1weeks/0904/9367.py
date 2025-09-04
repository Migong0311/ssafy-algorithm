'''
9367. 점점 커지는 당근의 개수
출처 : https://buly.kr/H6iOP5O
'''

T = int(input())

for t in range(1, T + 1):
    N = int(input())  # 당근 개수
    arr = list(map(int, input().split()))  # 당근의 크기 C를 의미

    # 연속된 오름차순 숫자 젤 마지막 출력
    # 만약 번호가 4 5 1 2 3 이면 가장 마지막으로 오름차순에 마지막으로 이어진 번호는 3
    # 그러니까 우선 최소값을 찾은후 우측을 비교해서 수가 더 작아지면 다시 처음부터 인식하도록 설계
    max_v = 1  # 연속으로 커지는 당근 개수의 최대값
    curr = 1  # 현재위치

    for i in range(1, N):  # # 2번째 당근부터 마지막 당근까지 순회
        if arr[i] > arr[i - 1]:  # # 바로 이전 당근보다 크면
            curr += 1  # # 연속 길이를 1 늘림
        else:
            curr = 1  # 만일 오른쪽으로 가도 숫자가 계속 작아질경우 1 출력
        # 지금까지의 최대 길이와 비교하여 갱신
        if curr > max_v:
            max_v = curr
    print(f'#{t} {max_v}')
