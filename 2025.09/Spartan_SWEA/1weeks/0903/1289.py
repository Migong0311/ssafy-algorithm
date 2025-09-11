'''
1289. 원재의 메모리 복구하기
출처 : https://buly.kr/DwElIrD
'''
'''
초기 bit = '0'
입력 비트값 왼쪽부터 탐색
현재값 유지하면서 -> 비트 달라지면 cnt++ -> 현재값-> 해당 비트로 수정 
'''
import sys
sys.stdin = open('../../../homework_SWEA/1weeks/0903/test.txt', 'r')
T = int(input())

for t in range(1, T + 1):
    bit = input() # 메모리의 원래값
    curr = '0' # 초기상태 비트 값
    cnt = 0 # 수정 카운트 초기화

    for c in bit: # 왼쪽부터 한 비트씩 확인
        if c != curr: # 현재 기대값과 목표 비트가 다르면?
            cnt += 1 # 이 위치부터 끝까지 한 번 덮어쓰기 수행
            curr = c # 이후 기대값을 새로 덮어쓴 값으로 갱신함

    print(f'#{t} {cnt}') # 출력 형식에 맞게 출력