# 선택 정렬과 기본 정렬 랄이브러리의 수행 시간 비교
from random import  randint
import time

# 배열에 10,000 개의 정수를 삽입
array = []
for _ in range(10000):
    array.append(randint(1, 100)) #1에서 100 사이의 랜덤한 정수

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_idex = i #가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if(array[min_idex] > array[j]):
            min_idex = j
    array[i], array[min_idex] = array[min_idex], array[i] #스와프

end_time = time.time() #측정종료
print("선택 정렬 성능 측정:", end_time-start_time)

#배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    array.append(randint(1, 100))

#기본 정렬 라이브러리 성능 측정
start_time = time.time()

#기본정렬 라이브러리 사용
array.sort()

end_time = time.time()

print("기본 정렬 라이브러리 성능 측정:", end_time-start_time)