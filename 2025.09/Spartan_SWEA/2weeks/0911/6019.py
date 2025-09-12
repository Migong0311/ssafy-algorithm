import sys

sys.stdin = open('test.txt', 'r')

'''
6019. 기차 사이의 파리
'''
T = int(input())

for t in range(1,T+1):
    # D는 두 기차 전면부 사이의 거리, A는 기차 A의 속력, B는 기차 B의 속력, F는 파리의 속력
    D,A,B,F = list(map(int,input().split()))
    # 시간 = 전체거리 / (A기차 속력 + B기차 속력)
    time = D/(A+B)

    # 거리 = 파리속력 * 시간
    dist = F*time
    print(f'#{t} {dist}')
