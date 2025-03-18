# pip install opencv-python
import cv2

# 이미지 읽기
image = cv2.imread('image.png')

# 이미지를 회색조로 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이미지 저장
cv2.imwrite('gray_image.jpg', gray_image)

# 이미지 표시
cv2.imshow('gray Image', gray_image)
cv2.waitKey(0)  # 키보드 입력 대기 : 매개변수 0은 무한정 대기한다는 의미로, 사용자가 아무 키나 누를 때까지 프로그램이 계속 실행되지 않음
cv2.destroyAllWindows() # 생성된 모든 창 닫는 함수 : 프로그램이 종료되기 전에 메모리를 정리하고 열려있는 모든 이미지 창을 닫는다.