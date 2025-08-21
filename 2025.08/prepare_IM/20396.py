import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T + 1):
    i, j = map(int, input().split())  # i : 바뀌는 색 대상 j : i + j번째까지 i번색으로 변경
    arr = list(map(int,input().split())) # 초기상태 배열

    # i번째 색 즉 번호로 j번째 까지 바꿔져애됨
    # 그러기위핸 전체 arr길이만큼 순회 하면서 조건 추가해줘야함
    for color in range(len(arr)):
        arr[i] = arr[i-1] # i번째 원소 나오도록 처리
        if color == i:
            arr[color] = arr[i]
        for j in arr[color]:
            result = arr[color] + j
    print(f'{t} {result}')
