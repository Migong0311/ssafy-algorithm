import sys

sys.stdin = open('test.txt', 'r')
##################################
# 아래부터 복붙하셈
##################################

remain_42 = []
no_remain = []
cnt = 0
for _ in range(10):
    n = int(input())
    remain_42.append(n % 42)

for r in remain_42:
    if r not in no_remain:
        no_remain.append(r)

print(len(no_remain))
