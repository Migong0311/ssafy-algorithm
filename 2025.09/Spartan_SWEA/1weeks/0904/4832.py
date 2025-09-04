'''
4832. 정곤이의 단조 증가하는 수
https://buly.kr/7mCF9q3
'''


def is_danjyo(num):
    """
    단조 증가(비내림차순) 판정 함수
    - 정수 num의 십진수 자릿수가 왼쪽->오른쪽으로 비내림차순 인지 검사
    - 문자열로 변환해 인접 문자 비교
    """
    s = str(num)  # 정수를 문자열로 변환
    # 인접한 두 자리씩 비교하여, 앞자리가 뒷자리보다 크면 실패
    for i in range(len(s) - 1):  # 0 ~ len(s)-2
        if s[i] > s[i + 1]:  # 앞자리 > 뒷자리면 비내림차순 위배
            return False  # 단조 증가 아님
    return True  # 끝까지 위배 없으면 단조 증가


# 테스트 케이스 개수 입력
T = int(input())

for t in range(1, T + 1):  # 1번부터 T번까지 반복
    N = int(input())  # 수의 개수 N
    A = list(map(int, input().split()))  # 수열 A1..AN 입력

    best = -1  # 조건 만족 최댓값 (없으면 -1 유지)

    # 모든 서로 다른 쌍(i < j)에 대해 곱을 계산
    for i in range(N):  # 첫 번째 인덱스 i
        for j in range(i + 1, N):  # 두 번째 인덱스 j (i보다 큰)
            prod = A[i] * A[j]  # 두 수의 곱
            # 곱이 단조 증가(비내림차순)인지 판정
            if is_danjyo(prod):
                if prod > best:  # 현재까지의 최댓값 갱신
                    best = prod

    # 형식에 맞게 출력
    print(f'#{t} {best}')
