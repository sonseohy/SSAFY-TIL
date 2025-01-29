# 3.1 Node.js 소개
### 갑자기 왜 Node.js를 배워야 하는지?
- React.js 기술은 Node.js를 기반으로 동작하는 기술이기 때문
- React뿐만 아니라 나중에 학습하게될 Next.js, Vue.js 또는 Svelte까지 모두 Node.js를 기반으로 동작하는 기술들

### Node.js
- 웹 브라우저가 아닌 환경에서도 자바스크립트 코드를 실행시켜주는 JavaScript 실행 환경 (Run Time)
- 실행 환경 === 구동기 : 무언가를 동작시키는 프로그램 의미
- Node.js도 JavaScript 코드를 실행시켜주는 구동기라고 이해 -> 프로그래밍에서는 언어를 구동하는 구동기를 실행 환경이라고 해서 '런타임'이라고 표현함

### Node.js가 필요한 이유?
- JavaScript는 태생 자체가 웹 페이지 내부에 필요한 아주 단순한 기능만을 개발하기 위해 만들어진 간단한 스크립트 언어
- ex. 사용자가 웹에서 버튼을 클리가현 경고창을 띄워주거나 요소의 색상을 변경시킨다던가 등 아주 단순한 인터랙션을 개발하기 위한 목적으로 오직 웹브라우저 내에서만 동작할 수 있도록 개발됨
- C, JAVA와 다르게 문법 자체가 매우 유연하고 작성하기 편리하도록 설계됨 -> 생산성에만 중심을 두고 언어가 설계되어 생산성이 매우 높았음
- 이러한 자바스크립트의 문법 체계, 설계 철학에 많은 사람들이 큰 매력을 느껴 자바스크립트로 웹페이지 내부의 기능을 만드는 것을 넘어서 웹 브라우저 바깥에서도 자바스크립트를 이용해서 프로그램을 만들고 싶어함
- 2009년에 Node.js가 등장하면서 JavaScript는 어디서든 동작할 수 있는 범용적인 언어가 됨
- Node.js는 JavaScript가 가진 태생적인 한계를 넘어설 수 있게 해주었고, 그 결과 Node.js를 이용해 JavaScript로 굉장히 많은 것들을 만들어내기 시작함
- 기존에 자바, C, C# 같은 언어로 만들던 웹 서버는 이제는 자바스크립트로 구축되는 일이 많아졌고, 더 나아가 모바일 어플리케이션을 만들고 데스크탑 어플리케이션까지 만들기 시작
- 자바스크립트의 전성기를 Node.js가 이끌었다고 볼 수 있음
- 현재까지 인기가 이어져오고 있음 -> 2023 Stack overflow 설문조사에 따르면 자바스크립트는 프로그래밍 언어 중 현재 가장 많은 개발자가 사용하는 언어

### 결론
- Node.js는 아주 단순한 상호작용만 개발할 수 있었던 언어인 JavaScript를 범용적으로 사용할 수 있도록 도와주는 JavaScript의 실행 환경, 즉 런타임이며, React 또한 Node.js를 기반으로 동작하는 기술임

# 3.2 Node.js 설치하기
- Node.js는 라이브러리나 언어가 아니고 컴퓨터에 직접 설치해서 사용하는 프로그램
- LTS : 대부분의 유저들에게 추천하는 현재 가장 안정적인 버전
- LTS는 Long Term Support의 약자로, 장기적으로 지원되는 버전이라는 뜻 -> 오랜기간 동안 안정적으로 지원되기 때문에 현재 거의 대다수의 기업에서도 LTS 버전을 이용하고 있음
- NPM(Node Package Manager) : Node.js의 프로젝트 단위인 패키지를 관리하는 도구로, 새로운 패키지를 생성하거나 외부 라이브러리를 설치하거나 또는 삭제하는 유용한 기능들을 제공함

# 3.3 Node.js 사용하기
- Node.js 환경에서는 여러 개의 JavaScript 파일로 어떠한 목적을 갖는 프로그램을 만들 대 모두 다 Package라는 단위로 프로그램을 만들게 됨 -> 앞으로 만들 모든 JavaScript 앱, 모든 React 앱들도 다 Package라는 단위로 만들어지게 되며, 앞으로 사용할 모든 라이브러리들도 모두 Package 단위로 만들어져 있음
- 패키지 : Node.js에서 사용하는 프로그램의 단위
### Node.js 패키지 생성 방법
1. 패키지의 루트 폴더, 즉 패키지의 뿌리가 될 폴더를 하나 만들어줘야 함 -> 새로운 폴더 만들기
2. vscode에서 파일 - 폴더 열기 - 생성한 폴더 열기
3. 패키지 생성을 위해 terminal 이용 - vscode의 자체 터미널 이용 : ctrl(command) + J -> 자동으로 터미널 경로가 현재 폴더 내부로 설정됨
4. 터미널에 새로운 패키지를 생성해달라는 의미로 npm init 명령 작성
5. package name (enter 누르면 소괄호 안의 기본값으로 설정됨), package 버전, description(설명), entry point (메인으로 실행될 JS 파일), test command 설정, git repository, 키워드, 라이센스 설정 (enter 누르면 기본 값으로 설정됨)
6. 패키지 생성이 완료되면 폴더 아래 package.json이라는 설정 파일이 자동으로 생성됨
7. 새로운 자바스크립트 파일 생성 : index.js
8. index.js 파일을 Node.js를 이용해 실행시키려면 터미널에 'node (실행시키고 싶은 파일명)' 입력
- 경로도 함께 확인 : 만약 src 폴더 아래에 index.js가 있다면 'node src/index.js'

### 패키지 스크립트
- package.json 파일의 스크립트라는 항목 안에 들어있는 일종의 매크로들
- test라는 기존에 설정된 스크립트 아래 start라는 새로운 스크립트를 만들고, 콜론 큰 따옴표로 스크립트의 값을 node src/index.js라고 설정해주면 이제는 터미널에 경로를 다 명시해줄 필요없이 스크립트의 이름인 start로만 명령을 한 번에 수행할 수 있게됨
```json
  "scripts": {
    ...,
    "start": "node src/index.js"
  },
```
- 이 스크립트를 실행하기 위해 터미널에 'npm run'이라고 입력한 후 뒤에 방금 설정한 스크립트 이름인 start를 입력해주면 됨 : 'npm run start'
- 설정한대로 node src/index.js가 실행되고 그 결과가 출력됨
- 따라서 패키지 내부의 파일과 경로가 복잡하게 될 경우에는 scripts라는 패키지의 기능을 이용해 한 번에 복잡한 경로에 있는 파일도 노드로 실행하도록 명령할 수 있다.

# 3.4 Node.js 모듈 시스템 이해하기
- 모듈 시스템 : 모듈을 다룰 수 있는 어떠한 시스템
- 모듈(Module) : 기능별로 나뉘어진 각각의 자바스크립트 파일들
- 모듈 시스템 : 모듈을 생성하고, 불러오고, 사용하는 등의 모듈을 다루는 다양한 기능을 제공하는 시스템
- JavaScript의 모듈 시스템 : Common JS(CJS), ES Module(ESM), AMD, UMD ...
- 대표적으로 많이 사용되는 모듈 시스템 : Common JS, Es Module

### CJS (Common JS) 모듈 시스템
- module이라는 내장 객체에 exports라는 프로퍼티의 값으로 객체를 저장해 줄건데, 이 객체 안에 각각 프로퍼티로 내보내고 싶은 값들을 넣어주면 됨
```js
// math 모듈 (math.js)
function add(a, b) {
  return a + b;
}

function sub(a, b) {
  return a - b;
}

// math 모듈로부터 add와 sub라는 두 개의 함수를 내보낼 것이므로 먼저 add라는 프로퍼티의 value로 내보낼 값 add 함수, sub라는 프로퍼티의 value로 내보낼 값인 sub 함수를 내보내 줄 수 있음음
// 참고로 value 값으로 사용되는 변수의 이름과 키 값이 똑같을 경우에는 변수나 함수 이름만 명시해줘도 알아서 해당 키와 값이 저장됨
module.exports = {
  add,  // add : add, 와 동일, 키 값과 변수 이름이 같을 경우 변수명(함수명)만 명시해줘도 됨
  sub : sub
};  // CommonJS 모듈 시스템에 의해 두 값이 math 모듈(math.js)로부터 내보내지게 됨
```

- 내보내진 값들은 다른 인덱스 같은 모듈(index.js)에서 내장 함수인 require를 이용해 모듈의 경로를 인수로 전달하면서 불러와 사용가능
```js
// index.js
const moduleData = require("./math");  // require 함수가 현재 경로의 math 모듈로부터 객체 형태로 내보내진 값을 그대로 반환해줌 -> 반환된 객체 값을 변수에 담아준 다음
console.log(moduleData);  // { add, sub }, add와 sub 함수가 잘 출력됨

console.log(moduleData.add(1, 2));  // 3
console.log(moduleData.sub(1, 2));  // -1
```

- 객체의 구조분해 할당을 이용하면 굳이 위 코드처럼 moduleData라는 변수에 받아서 점 표기법으로 사용할 필요없이 아래 코드도 가능
```js
const {add, sub} = require("./math"); // 객체의 구조분해 할당으로 add와 sub 함수를 받아옴

console.log(add(1, 2));
console.log(sub(1, 2));
```

### Es Module
- CommonJS보다 훨씬 최신식으로 동작하는, 그렇기 때문에 React에서도 사용하게 되는 모듈 시스템
- ES 모듈 시스템을 사용하려면 먼저 이 패키지 내에서 앞으로는 ES 모듈 시스템을 쓰겠다라는 설정을 해줘야 함
- 패키지 설정 파일인 package.json에서 파일의 맨 아래에 콤마로 쉼표 찍고 타입은 모듈이라는 추가적인 옵션을 넣어줘야 함
```json
...
  // package.json 파일 맨 아래 부분 (license 밑에 콤마 찍고 작성)
  "type": "module"  // 앞으로 해당 폴더의 패키지는 ES 모듈 시스템을 사용하겠다라는 뜻
}
```
- 위 코드 작성 후 CommonJS 모듈 시스템을 활용하는 코드를 npm run start로 가동시켜 보면 오류 발생 (require is not defined in ES module scope ->  require 함수는 ES 모듈의 기능이 아니다, import를 대신 사용해라라는 오류 발생)
- Why? ES 모듈 시스템과 CommonJS 모듈 시스템은 기본적으로는 함께 이용할 수가 없기 때문

```js
// math 모듈 (math.js)
function add(a, b) {
  return a + b;
}

function sub(a, b) {
  return a - b;
}

// export 키워드를 쓴 후 중괄호를 열고 내보낼 함수를 작성
export { add, sub };
```
- ES 모듈 시스템에서는 모듈로부터 어떠한 값을 내보낼 때 그냥 export라는 키워드 뒤에 객체를 리터럴로 생성해서 그 안에 내보내고 싶은 값들을 담아주기나 하면 됨
- 모듈로부터 값을 가져오는 index 측에서도 require가 아닌, import와 중괄호로 가져오고자 하는 값을 작성해주고 from 뒤에 어떤 모듈로부터 가져올지 경로 작성
```js
// index.js
import {add, sub} from "./math.js";

console.log(moduleData.add(1, 2));  // 3
console.log(moduleData.sub(1, 2));  // -1
```
- 주의! ES 모듈 시스템을 사용할 때는 모듈의 확장자까지 꼭 명시를 해줘야함 (math.js의 .js까지 명시, .js를 안쓰고 ./math만 쓰면 못 찾음)

#### 추가기능
- export 뒤에 중괄호로 묶어서 함수를 내보내지 않고, 함수 선언문 앞에 export 키워드를 붙여줘도 똑같이 동작함
```js
// math 모듈 (math.js)
export function add(a, b) {
  return a + b;
}

export function sub(a, b) {
  return a - b;
}
```
- ES 모듈 시스템에서는 특별이 하나의 모듈을 대표하는 디폴트 값을 내보내는 방법도 있음
```js
// math 모듈 (math.js)
export function add(a, b) {
  return a + b;
}

export function sub(a, b) {
  return a - b;
}

// multiply 함수는 그냥 export로 내보내는게 아니라 default로써 내보내져서 math 모듈을 대표하는 단 하나의 기본값이 됨
export default function multiply(a, b) {
  return a * b;
}
```

```js
// index.js
// 그래서 기본 값으로써 내보내진 multiply 같은 함수는 다른 모듈에서 import로 불러올 때 중괄호 안에 작성해주는게 아니라
// 대신에 새로운 import문을 만들어서 중괄호 없이 불러오도록 설정해줘야 함
// 이때 특별히 기본값을 불러올 때 이름을 맘대로 정해서 불러올 수 있음 (multiply -> mul)

// import multiply from './math.js';
import mul from './math.js';  // 이름을 바꿔서 불러오는 것도 가능

console.log(mul(2, 3)); // 6
```

- 마지막으로 동일한 경로로부터 값을 불러오는 여러 개의 import문은 아래와 같이 합치는 것도 가능
```js
// index.js
import mul, {add, sub} from './math.js';

console.log(moduleData.add(1, 2));  // 3
console.log(moduleData.sub(1, 2));  // -1
console.log(mul(2, 3)); // 6
```
- 동일한 경로로부터 값을 가져오는 import문이 여러 개라면 위와 같이 합쳐서 사용하는게 훨씬 더 깔끔함

# 3.5 Node.js 라이브러리 사용하기
### 라이브러리
- 프로그램을 개발할 때 필요한 다양한 기능들을 미리 만들어 모듈화 해놓은 것
- 라이브러리를 이용하면 프로그램을 만들 때 복잡하거나 귀찮은 기능들을 일일이 직접 다 만들 필요가 없음
- 원하는 기능이 있으면 그 기능을 제공하는 라이브러리를 설치해서 모듈 시스템으로 불러와서 이용하면 됨
- 모듈 시스템의 import문만을 이용해서 간단하게 불러와 이용하는 것도 가능
- [npm js](https://www.npmjs.com/) : Node.js 라이브러리계의 백화점, 모든 라이브러리가 다 등록되어 있음
- 최상단 검색바에 찾고 싶은 기능을 검색해서 관련된 라이브러리를 찾아내면됨
- 실습 : randomcolor
- 라이브러리 설명을 보면 어떻게 라이브러리를 설치할 수 있는지 명령어, 어떻게 이용할 수 있는지 간단한 안내문도 작성되어 있음
- 상세페이지 우측에 install 탭이 존재 -> 아래에 명령어가 하나 나와있음 -> 해당 명령어가 라이브러리를 설치하기 위해서 이용해야 될 명령어
- vscode의 폴더로 가서 터미널에 해당 명령어 입력 -> added 1 package라는 메세지가 나오면서 라이브러리가 잘 설치되었다고 알려줌
- 라이브러리가 설치되면 몇가지 변화가 생김
1. package.json에 들어가보면 맨 아래에 dependencies라는 항목이 추가 되었고, 해당 항목 안에 방금 설치한 randomColor라는 라이브러리의 버전 정보가 들어있음
- dependency는 '의존'이라는 뜻으로, 쉽게 말해 이제부터 이 프로젝트는 랜덤 컬러라는 라이브러리를 이용하니까 여기에 의존하고 있다는 뜻 (해당 라이브러리가 있어야 동작 가능하다는 뜻)
- 새로운 라이브러리를 설치하면 package.json의 dependencies 항목에 어떠한 라이브러리를 설치했고 대략적인 설치된 버전이 무엇인지 의미하는 필드가 추가됨
2. 파일 탐색기를 보면 package-lock.json이라는 새로운 파일과 node_modules라는 새로운 폴더가 자동으로 생성됨
- node_modules 폴더는 우리가 설치한 라이브러리가 실제로 저장되는 곳
- node_modules 폴더를 열어보면 randomcolor 라이브러리를 설치했기 때문에 실제 랜덤컬러의 코드가 node_modules 안에 들어있음
- node_modules : 실제로 설치된 라이브러리의 저장소
- package-lock.json : 패키지가 사용하고 있는 라이브러리들의 버전이나 정보를 package.json보다 더 정확하고 엄밀하게 저장하는 파일
- package-lock.json 파일의 정보가 기존의 package.json과 다른점?
  - package-lock.json 파일은 정확한 버전 정보를 저장하고 있다는 것
- package.json 파일은 randomcolor라는 패키지의 버전 앞에 갈매기 표시(^)가 붙어있음 -> 이 표시는 Version Range(버전 범위)라고 해서 정확한 버전이 아니라 대략적인 버전이 표기되어 있는 것
- "^0.6.2" : ^ 표시는 0점대 버전부터 1점대 버전 이전까지의 버전 중 최신 버전으로 설치하겠다는 의미로 생각해주면 됨
- package.json에는 대략적인 버전이 명시가 되고 package-lock.json에는 실제로 설치된 버전의 정보가 명시된다.

### randomcolor 라이브러리 실습
- randomcolor 라이브러리를 모듈 시스템을 이용해 불러오기
```js
// index.js
// import문을 통해 randomColor라는 라이브러리가 내보낸 기본값을 불러오도록 import문을 작성해줌
// 참고로 라이브러리에서 어떠한 값을 가져올 대는 경로를 명시하는게 아니라 from 뒤에 라이브러리 이름만 명시하면 됨
import randomColor from 'randomcolor';

const color = randomColor();
console.log(color);
```
- 라이브러리를 이용하면 다양하고 신기한 기능들을 손쉽게 제공받을 수 있다는 장점 존재

### node_modules와 package-lock.json이 지워지게 되면
- 실제로 해당 라이브러리의 코드를 보관하는 node_modules 폴더가 사라졌기 때문에 다시 실행해보면 오류 발생
- 이때 package.json의 정보만 가지고 있어도 원래 설치되었던 것처럼 라이브러리를 다시 설치하도록 만들어줄 수 있음
- npm install 또는 npm i를 입력해주면 됨
- npm i를 입력하면 package.json의 dependencies의 정보를 기준으로 모든 패키지, 모든 라이브러리를 다시 다 설치해줌
- 만약 node_modules나 package-lock.json 파일이 없어지고나 삭제가 되었다 하더라도 npm i만 입력해주면 한 번 설치되어서 package.json에 기록된 라이브러리들을 다시 한 번 설치해주기 때문에 크게 걱정하지 않아도 됨
- 보통 Node.js 패키지를 압축해서 누군가한테 공유하거나 또는 Github 같은 곳에 업로드 할 때 node_modules 폴더는 굳이 함께 포함하지 않음
- Why? package.json만 있으면 언제든지 npm i를 통해 필요한 라이브러리들을 다시 설치할 수 있기 때문에 굳이 용량이 크고 무거운 node_modules 폴더까지 함께 공유할 필요가 없음
- 만약 Node.js 패키지 파일을 남들과 공유해야 될 일이 있다면 node_modules 폴더는 과감하게제외하고 다른 파일들만 보내줘도 괜찮음
