// Truthy & Falsy란?
// - 참이나 거짓을 의미하지 않는 값도, 조건문 내에서 참이나 거짓으로 평가하는 특징
// - Truthy : 참은 아니지만 조건문 내에서 참으로 평가되는 값들, 참 같은 값이라고 말함
// - Falsy : 거짓은 아니지만 조건문 내에서는 거짓으로 평가되는 값들, 거짓 같은 값이라고 말함
// JavaScript에 존재하는 모든 값들은 Truthy하거나 또는 Falsy 함
// -> 이런 특징을 잘 이용하면 특정 상황에서 조건문을 매우 간결하고 강력하게 만들 수 있음

// 1. Falsy한 값
// 7가지 Falsy한 값이 존재
let f1 = undefined;
let f2 = null;
let f3 = 0;
let f4 = -0;
let f5 = NaN;
let f6 = "";
let f7 = 0n;  // Big Integer라는 특수한 자료형에 해당하는 값, 아주 큰 숫자를 저장하는 데에 사용되는 값 (웹 개발 중에는 잘 이용 X)


// 2. Truthy 한 값
// -> 7가지 Falsy 한 값들 제외한 나머지 모든 값
let t1 = "hello"; // 비어있지 않은 문자열
let t2 = 123; // 0이 아닌 숫자
let t3 = [];  // 빈 배열
let t4 = {};  // 객체
let t5 = () => {};  // 화살표 함수


// 3. 활용 사례
// 매개변수로 객체를 받을 것이라 생각했는데 실제로는 Undefined 값이 들어오는 경우
// 보통 객체의 특정 프로퍼티에 접근하는 기능들을 담고 있는 함수에서는 보통 조건문으로 person 매개변수 값이 null이거나 undefined가 아님을 먼저 확인해주어야 함
function printName(person) {
  if (!person) {  // 매개변수 값이 null이나 undefined로 들어왔을 때, 조건문에서 거짓으로 평가해 not 연산자가 붙어 true가 되어 아래 코드 실행
    console.log("person의 값이 없음");
    return;
  }
  console.log(person.name);
}

let person = { name: "이정환" };
// let person;
// let person = null;
printName(person);
