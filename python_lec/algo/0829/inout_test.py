import sys
# sys.stdin: 표준 입력
# open('input.txt', 'r') : input.txt를 r(읽기 전용)으로 열겠다.
# text파일에서 input값 수정후 shift + F10 누르면 바로 결과 확인 가능
sys.stdin = open('input.txt', 'r')
# open('output.txt', 'w') : output.txt를 w(쓰기 전용)으로 열겠다.
# 더이상 콘솔에 결과가 나오는 것이 아닌 output.txt 파일에 출력 결과가 나옴
sys.stdout = open('output.txt', 'w')

A, B = map(int, input().split())
print(A+B)