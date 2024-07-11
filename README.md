# TIL
# 제목 1
## 제목 1-1
1. 순서
    1. 1-1
    2. 1-2

2. 있는
3. 리스트

## 제목 1-2
- 순서
  - 없는
- 리스트

# 제목 2
## 제목 2-1
**굵게**

*기울게*

~~취소선~~

----
- 3개 이상이면 줄 긋기

## 제목 2-2
``` python
print("Hello World!")
```
파이썬은 `print` 함수를 사용해 텍스트를 출력

[google로 이동](https://google.co.kr)

![주소를 못찾았을 때 나오는 문장](https://www.google.co.kr/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)

### 상대경로
현재 작업하고 있는 위치로부터 경로를 작성해주는 방식

![이미지](../실습/img/google.png)

### 절대경로
상위 경로부터 모든 경로를 작성해주는 방식

![이미지](C:\Users\SSAFY\실습\img)

프로그램에 따라 해석되지 않는 경우 존재

## CLI
- ls : 현재 폴더에 있는 파일과 폴더를 보여줌
- cd : 폴더 간 이동
- touch : 파일 생성 (ex.touch 폴더명/파일명 : 폴더 안에 파일 생성 가능)
- mkdir : 새 디렉토리(폴더) 형성
- rm : 파일 삭제 (디렉토리 삭제는 뒤에 -r 붙이기)
- code . : 현재 폴더에 코드 파일 생성
- . : 현재 디렉토리
- .. : 부모(상위) 디렉토리
- 폴더 이동 : cd cli/test_folder, cd ../../(이전 이전 폴더로 이동), cd ../test_folder (이전 폴더로 이동해 test_folder로 이동)

## git
- git의 영역 3가지 :  working directory, staging area(working directory에서 변경된 파일 중 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역), repository (버전 이력과 파일들이 영구적으로 저장되는 구역)
- 파일 생성하면 파일이 working directory에 존재, git add를 통해 파일을 staging area에 올릴 수 있고 staging area에 있는 파일은 commit하면 commit 뒤 파일명 쓰지 않고도 commit 가능 
- git init : 폴더가 git이 관리하는 working directory(실제 작업중인 파일들이 있는 구역)가 됨, 로컬 저장소 설정(초기화), git 버전관리를 시작할 디렉토리에서 실행
- 프로젝트를 새로운 폴더에서 다시 시작하려고 할 때는 소스 코드를 git으로 관리하기 위해 git init 먼저 작성하여 저장소를 초기화 해줘야 함
- git init 주의사항 : git 로컬 저장소 내에 또 다른 git 로컬 저장소를 만들지 말 것 (이미 git 로컬 저장소인 디렉토리 내부 하단에서 git init 명령어를 다시 입력하지 말 것, 숨겨진 git 폴더 안에 또 만들기 X, init 된 폴더에 두 번 금지)
- git 관리 받기 시작하면 숨겨진 폴더에 .git 폴더 생성
- git status : git 상태확인
- git commit -m "메세지" : 버전(변경 이력)이 기록됨, 
- commit = 버전 : 변경된 파일을 저장 후 기록으로 남김
- git config --global user.email(or name) "이메일 or 이름"
- global : 모든 프로젝트 commit에 use.email과 name을 붙여줌
- git config --global -l : user.email, user.name 설정 되었는지 확인(알파벳 엘L, list 의미), git global 설정 정보 보기
- git add . : 모든 변경사항 파일 추가
- git log --oneline : 로그를 한 줄로 짧게 확인 가능 (commit 메세지만 짧게 확인 가능)
- 단계별 git status 메세지 : 1. working directory : Untracked > 2. staging area : New file > 3. repository : nothing to commit
- remote : git repository와 local repository를 연결
- git repository 생성시 Add a README file는 이전에 로컬 폴더에 commit 내용이 있으면 체크 X, README file이 생성되므로 충돌이 일어남, 연결하려는 폴더에 아무 파일 없을때(커밋내역 없을때) Add a README file 체크, 로컬에서 폴더 생성해서 이미 작업을 했으면 체크하지 X
- git branch -M master : branch가 아예 없으므로 master로 branch를 잡는 명령
- git remote add origin (git repository 주소) : 로컬과 git repository 연결
- git remote -v : 현재 remote 상태 확인
- git push -u origin master : 로컬 commit 내용을 git repository로 올림
- -u의 의미 : -u 옵션은 --set-upstream의 줄임말, 로컬 레포지토리의 master 브랜치가 리모트 레포지토리의 master 브랜치를 항상 추적하도록(tracking) 하도록 설정, 이런 관계를 tracking connection이라고 함
- git push origin master과의 차이점 : [참고](https://blog.naver.com/codeitofficial/221946628621)
- git remote rm origin : remote 된 origin 삭제
- git clone (원격 repository 주소) : 원격 repository에서 로컬 repository로 가져오는 명령
- git clone 후 바로 git remote -v 하면 안됨, cd로 불러온 폴더로 들어간 후 remote
- remote 한 후 내용 수정했으면 add, commit 후 git push
- 원격에서 로컬로 수정사항 받는 명령 : git pull
- push 후 pull 받지 않은 상태에서 다시 push 하면 충돌이 일어남
- 원격 repository에서 수정을 하면 add와 commit이 다 되어 자동으로 저장됨, 따라서 local에서 pull 해줘야 함
- 만약 pull 하지 않은 상태에서 로컬 repository에서 push를 하게되면 충돌 : 대처법? 로컬 파일을 임시로 다른 곳에 저장한 후 로컬 repository를 아예 삭제하고 원격에서 pull 해서 원격 파일을 받은 후 임시 저장된 곳에서 파일 보고 수정
- staging area에 올라간 파일 unstage 하기 : git rm --cached(working directory에서 commit이 한번도 발생하지 않은 경우), git restore --staged(working directory에서 commit이 발생한 경우) (add 후 commit 하고 싶지 않을 때)
- 바로 직전 생성한 commit 수정하기(바로 직전만 가능) : git commend --amend (명령창에서 수정창 여는 코드, commit 메세지가 상단에 뜨고 해당 명령창에서 수정, INSERT 키 누르면 수정 가능(=편집모드), 빔(VIM)에디터 명령 검색해서 해당 명령창에서 수정할때 쓰는 기능 확인 가능, esc키 누르면 빠져나옴, :wq)