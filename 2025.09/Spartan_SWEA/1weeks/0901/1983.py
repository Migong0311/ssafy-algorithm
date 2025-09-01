
'''
1983. 조교의 성적 매기기
출처 : https://buly.kr/31TllQD
'''
import sys

sys.stdin = open('input_1.txt', 'r')

# 상대평가에 따른 학점 리스트
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']


# (학생번호,총점) -> 여기서 총점만 알기위해서 만든 함수
def get_score(item):
    return item[1]


T = int(input())  # 테스트 케이스 입력
for t in range(1, T + 1):  # 입력 받는 값들을 리스트로 입력받음
    N, K = map(int, input().split())  # N : 학생수 K : 학점을 알고싶은 학생의 번호

    # 학생수 N명만큼 점수를 입력받을 2차원 배열 생성
    score = [list(map(int, input().split())) for _ in range(N)]

    # 각 학생의 총점을 담을 리스트
    result_score = []

    for i in range(N):  # 학생수 만큼 순회
        # 총점 구하는 공식 = 중간35% + 기말45% + 과제20%
        # 입력받은 수의 각각 1,2,3번째 점수를 퍼센트 만큼 곱함
        total_score = score[i][0] * 0.35 + score[i][1] * 0.45 + score[i][2] * 0.2
        # (학생번호 ->1부터 , 총점) 형태 저장
        result_score.append((i + 1, total_score))
    # 상위권 학생부터 점수를 줘야되기 때문에 내림차순 정렬
    result_score.sort(key=get_score, reverse=True)

    # 평가 항목이 10개이기 때문에 전체 인원수에서 10을 나눈값을 생성한다
    div = N // 10

    # K번째 학생의 총점 위치 찾기
    for i in range(N):  # 총점 기준으로 정렬된 리스트를 앞에서부터 순회
        # total[i] = (학생번호, 총점) -> 학생번호가 K와 같다면
        if result_score[i][0] == K:
            #  i번째 학생의 순위 구간(i // div)에 해당하는 학점 부여
            result = grade[i // div]
            # 원하는 학생의 학점을 찾았으므로 반복 종료
            break

    print(f'#{t} {result}')  # 출력 형식에 맞게 설정
