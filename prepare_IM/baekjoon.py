import sys

sys.stdin = open('test.txt', 'r')

'''
https://www.acmicpc.net/problem/10810
입력
5 4
1 2 3
3 4 4
1 4 1
2 2 2

출력
1 2 1 1 0

바구니 개수 : N
바구니에 1 ~ N까지 번호 있음
0번인덱스엔 공이없음

공을 넣는 횟수 : M
이미 공이 있는 경우 공을 뺴고 새로 넣어야함

요구사항
공을 어떻게 넣을지가 주어졌을때 -> 2차원배열
M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어있는지 구해라

단 각각 입력하는 값들은 i번바구니부터 j번바구니까지 k번 공을 넣는다는 의미
예를들어 1 2 3은 1번 바구니부터 2번바구니까지 3번공을 넣는다는 의미

'''
n, m = map(int, input().split()) # n : 바구니 개수 m: 공을 넣는 횟수
arr = [list(map(int, input().split())) for _ in range(m)]


