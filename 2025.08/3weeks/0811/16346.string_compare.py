import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1, T + 1):
    str1 = input()  # 작은 문자열
    str2 = input()  # 큰 문자열
    # str2안에 str1과 일치하는 부분?
    N = len(str1)
    M = len(str2)
    # 답을 일치하는 부분이 없다 라고 가정
    answer = 0

    # 큰 문자열의 인덱스를 비교 시작 위치(기준위치)로 잡는다.
    # 작은 문자열을 한칸씩 밀면서 비교
    # 밀고 나서 큰 문자열의 범위를 벗어나면 안되니 N-M+1
    for i in range(N - M + 1):
        for j in range(N):
            if str2[i + j] != str1[j]:
                break
    else:
        answer = 1
    print(f'#{tc} {answer}')