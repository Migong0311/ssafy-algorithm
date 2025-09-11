'''
16944. 4일차 - 병합 정렬
'''

# 병합 정렬을 연습하는 로직입니다
import sys

sys.stdin = open('test.txt', 'r')
'''
문제
N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할 한다.

병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.
정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다.  N//2 번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수를 출력

입출력 예제

입력
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8

출력
#1 2 0
#2 6 6


'''

T = int(input())


# 병합 담당 함수: 두 정렬된 리스트를 하나로 합침
def merge(left, right):
    global cnt
    # 왼쪽 마지막 > 오른쪽 마지막일때 카운트
    if left and right and left[-1] > right[-1]:
        cnt += 1
    result = []  # 병합 결과 담을 리스트
    i, j = 0, 0  # 좌,우 인덱스 초기화

    while i < len(left) and j < len(right):  # 양쪽 리스트 모두 값이 남아있을때
        # 안정정렬을 위한 이상 사용
        if left[i] <= right[j]:
            result.append(left[i])  # 더 작은 값을 결과에 추가
            i += 1
        else:  # 오른쪽 값 추가
            result.append(right[j])
            j += 1

    # 남은 요소들 처리(한쪽 리스트가 끝난 경우)
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


# 병합 정렬 함수
def merge_sort(array):
    if len(array) <= 1:  # 원소가 하나 이하라면 정렬 불필요
        return array

    mid = len(array) // 2  # 중간 인덱스 계산
    left = merge_sort(array[:mid])  # 왼쪽 절반 재귀 정렬
    right = merge_sort(array[mid:])  # 오른쪽 절반
    return merge(left, right)  # 두개를 서로 합침


for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    sorted_arr = merge_sort(arr)
    print(f'#{t} {sorted_arr[N//2]} {cnt}')
