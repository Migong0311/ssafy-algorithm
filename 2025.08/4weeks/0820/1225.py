"""
1225 암호생성기
"""
for tc in range(1,11):
    input()
    q = list(map(int,input().split()))

    front = rear = 0

    while rear == 0:
        for i in q:
