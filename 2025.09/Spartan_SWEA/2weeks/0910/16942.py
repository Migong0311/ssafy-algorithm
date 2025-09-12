import sys
sys.stdin = open('test.txt','r')

'''
16942. 4일차 응용 - 퀵 정렬
'''

T = int(input())


# 피벗 : 제일 중앙 요소
# 일반적으로 더 균형 잡힌 분할이 가능하며, 퀵 정렬의 성능을 최적화 가능
def hoare_partition1(left, right):
    mid = (left + right) // 2
    p = arr[mid]  # 피벗을 중간 요소로 설정
    arr[left], arr[mid] = arr[mid], arr[left]  # 필요시 중간 요소를 왼쪽으로 이동

    i = left + 1  # 피벗 옆
    j = right  # 젤 끝에

    while i <= j:  # 교차가 되면 끝
        # i는 피벗보다 큰 값을 검색 (작거나 같으면 answer += 1)
        while i <= j and arr[i] <= p:
            i += 1
        # j는 피벗보다 작은 값을 검색 (크거나 같으면 j -= 1)
        while i <= j and arr[j] >= p:
            j -= 1

        if i < j:  # swap
            arr[i], arr[j] = arr[j], arr[i]
    # 피벗과 j의 위치를 swap
    arr[left], arr[j] = arr[j], arr[left]
    return j


def quick_sort(left, right):
    if left < right:
        p = hoare_partition1(left, right)
        quick_sort(left, p - 1)
        quick_sort(p + 1, right)


for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, len(arr) - 1)
    print(f'#{t} {arr[N//2]}')
