import sys

sys.stdin = open('../../../swea_homework/1weeks/0903/test.txt', 'r')

'''
1288. 새로운 불면증 치료법
출처 : https://buly.kr/FsJ5tJC
'''

'''
    입력
    5
    1  
    2
    11
    1295
    1692

    위에 테스트 케이스 중 #1 인 1일경우
    N = 1
    sheep = [1]
    2N = 2
    sheep = [1,2]
    3N = 3
    sheep = [1,2,3]
    ...
    10N = 10
    sheep = [1,2,3,4,5,6,7,8,9,0]
    이렇게 0~9까지 다 나오면 종료

    필요조건 
    1. 우선 N의 결과 값을 sheep에 한 자리 수 단위로 구분
    예 : 1259 -> 1,2,5,9 
    2. 최종 cnt 로 sheep 에 append 될때마다의 카운트 함께 증가
    3. 만일 sheep에 최초 수 이후 중복이 발생하면 이후는 들어오지 못하게 설정
    예 : 첫 번째로 N = 1295번 양을 센다. 현재 본 숫자는 1, 2, 5, 9이다.
        두 번째로 2N = 2590번 양을 센다. 현재 본 숫자는 0, 2, 5, 9이다.
        여기에서 2번째에 2,5,9가 2번 채워지지 않도록 설정을 해줘야함
    4. while로 N이 sheep의 숫자가 다 채워질때까지 반복
    '''
T = int(input())  # 테스트 케이스 개수

for t in range(1, T + 1):  # 테스트 케이스 만큼 순회
    N = int(input())  # N의 배수 번호 양을 새기 위한 변수

    sheep = [0] * 10  # 0부터 9까지 나오는 수를 담는 리스트
    cnt = 0  # sheep이 0~9까지 다 채워지는데 걸리는 횟수

    k = 0  # 배수 인덱스
    last_multi = 0  # 모든 숫자를 다 본 시점의 마지막 배수 값 저장용
    # N이 10개의 수를 모두 다 볼때가지 반복
    while cnt < 10:
        k += 1  # 다음 배수 인덱스로 증가
        multi = N * k  # 현재 배수 값 계산
        last_multi = multi  # 현재 배수 값을 임시로 저장
        for j in str(multi):
            d = int(j)  # str -> int 형 변환
            if not sheep[d]:  # 아직 보지 않은 숫자
                sheep[d] = True  # 그것을 본것으로 표시
                cnt += 1  # 서로 다른 숫자 개수 증가
                if cnt == 10:  # 모든 값을 다 봤다면
                    break  # 자릿수 순회중단
    print(f'#{t} {last_multi}')
    """
    출력
    #1 10
    #2 90
    #3 110
    #4 6475
    #5 5076
    """
