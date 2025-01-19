// 1. Number Type (숫자)
let num1 = 27;
let num2 = 1.5;
let num3 = -20;

console.log(num1 % 3);  // 나머지를 구하는 연산을 프로그래밍에서 모듈러 연산이라고 함

let inf = Infinity;     // 양의 무한대
let mInf = -Infinity;   // 음의 무한대

let nan = NaN;      // not a number라는 뜻으로, 수치 연산이 실패했을 때의 결과 값으로 보통 사용
console.log(1 * "hello");   // NaN이 나오는 경우 예시

// NaN이라는 값이 있기 때문에 불가능한 수치 연산을 시키더라도 프로그램이 완전히 종료되어 버리거나 하지 않음
// -> 따라서 다른 언어에 비해서 JS가 수학 연산에서 안전하다고 표현할 수 있음


// 2. String Type (문자열)
// JS에서 문자열 값은 무조건 쌍따옴표 또는 작은따옴표로 감싸주어야 함
// 쌍따옴표(작은 따옴표)를 쓰지 않게 되면 값을 문자열이 아닌 변수명으로 취급하기 때문에 오류 발생
let myName = "이정환";
let myLocation = "목동";
let introduce = myName + myLocation;    // 자바스크립트의 문자열은 독특하게 덧셈 연산을 지원
console.log(introduce); // 이정환목동

// 문자열을 `(backtick)을 이요해 만들 수도 있음
// 백틱으로 문자열을 만들면 기본적으로는 쌍따옴표로 만든 문자열과 동일하지만 달러와 중괄호를 이용해 문자열 안에 변수의 값을 동적으로 집어넣을 수 있음
// 이러한 문법을 템플릿 리터럴 문법이라고 부름
let introduceText = `${myName}은 ${myLocation}에 거주합니다`;


// 3. Boolean Type
// true, false, 즉 참이거나 거짓만을 젖아하는 타입
// 상태를 의미하는데 주로 사용되는 타입
let isSwitchOn = true;
let isEmpty = false;


// 4. Null Type (아무것도 없다)
let empty = null;   // empty라는 변수에 어떠한 값도 들어있지 않다라는 의미


// 5. Undefined Type
// Undefined라는 단 하나의 값만 포함하는 특수한 타입
// undefined라는 값은 변수를 선언하고 진짜 그 변수에 대한 어떠한 값도 집어넣지 않았을 때 자동으로 할당이 되는 값
let none;    // 변수를 만들고 초기화 값 없이 선언해주면
console.log(none);  // 출력해보면 undefined가 출력됨

// null과 undefined의 차이?
// - undefined 값은 변수를 선언하고 아무런 값도 할당하지 않았을 때 자동으로 들어가는 값
// - 반면 null 값은 직접 명시적으로 변수에 할당을 해줘야 되는 값
// null 값은 개발자들이 현재 이 변수에 어떠한 값도 없다를 표현할 때 사용하는 값이고, undefined는 변수를 초기화하지 못했거나 존재하지 않는 어떤 값을 불러오려고 할 때 발생할 수 있는 값