## Branch Scenario

###
- Branch 장점
1. 독립된 개발 환경을 형성하기 때문에 원본(master)에 대해 안전
2. 하나의 작업은 하나의 브런치로 나누어 

### master(main) 브랜치의 의미와 역할
- 기본 브랜치 (Default Branch)
  - 저장소의 초기 상태를 나타내며, 일반적으로 프로젝트의 가장 최신 버전 또는 배포 가능한 안정적인 코드를 포함
- 기준점
  - 다른 브랜치가 파생되는 기준점으로 사용됨
- 변경사항 통합
  - 다른 브랜치에서 작업한 기능이나 버그 수정을 완료한 후, 코드 리뷰와 테스트를 거쳐 master(또는 main)로 병합하는 과정 거침

### git branch
- 브랜치 조회, 생성, 삭제 등 브랜치와 관련된 git 명령어
- git branch : 브랜치 목록 확인
- git branch -r : 원격 저장소의 브랜치 목록 확인
- git branch <브랜치 이름> : 새로운 브랜치 생성
- git branch -d <브랜치 이름> : 브랜치 삭제 (병합된 브랜치만 삭제 가능)
- git branch -D <브랜치 이름> : 브랜치 삭제 (강제 삭제)

### git switch
- 현재 브랜치에서 다른 브랜치로 HEAD를 이동시키는 명령어
- git switch <다른 브랜치 이름> : 다른 브랜치로 전환
- git switch -c <브랜치 이동> : 새 브랜치 생성 후 전환
- git switch -c <브랜치 이동> <existing-branch-name> : 특정 커밋(<existing-branch-name>)에서 현재의 커밋 기준으로 새 브랜치 생성하고 전환 
- 주의 사항 : 

### HEAD
- 현재 브랜치나 commit을 가리키는 포인터 (현재 내가 바라보는 위치)

### branch 생성 및 조회
1. 현재 위치(master 브랜치의 최신 commit)에서 login 브랜치를 생성
![alt text](image-2.png)
- git log --oneline으로도 확인 가능
![alt text](image-3.png)
- master4 생성 후 log 확인하면 HEAD가 이동한 것 볼 수 있음
![alt text](image-4.png)
- HEAD를 login으로 옮기면 login이후 commit은 보이지 않음
![alt text](image-5.png)
- 모든 commit을 보고 싶다면 --all 붙이기
![alt text](image-6.png)
2. master 브랜치에서 article.txt작성한 master4가 사라짐

### branch에서 commit 생성
1. login 브랜치에서 article.txt 파일 수정 (login1 작성)
2. 추가적으로 test_login.txt도 

### 사전준비 1
1. git-branch-practice 폴더 생성 : mkdir git-branch-practice
2. 생성한 폴더로 이동
3. VSCode 실행
4. Git 저장소 생성 : git init으로 git 저장소 생성
![alt text](image.png)

### 사전준비 2
1. article.txt 생성
2. 각각 master-1, master-2, master-3 라는 내용을 순서대로 입력하여 commit 3개를 작성
![alt text](image-1.png)
- git branch : 현재 만들어진 branch 목록을 보여줌
- master는 배포된 상태 저장하는데 주로 사용

### 사전준비 3
1. 