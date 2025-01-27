// 단락 평가 (Short-circuit Evaluation)
// AND나 OR 같은 논리 연산식에서 첫번째 피연산자의 값만으로도 해당 연산의 결과를 확정할 수 있다면 두 번째 피연산자의 값에는 아예 접근하지 않는 자바스크립트의 특징
// 단락평가를 이용하면 조건문을 이용하지 않고도 특정 상황에서 어떠한 함수를 호출하지 않도록 방지해 주거나 어떠한 값들을 굳이 계산하지 않도록 제한하는 등 다양한 기능 개발이 가능
// 단락평가는 boolean형 값 뿐만 아니라 이전에 살펴본 Truthy한 값이나 falsy한 값에도 적용됨
// -> truthly나 falsy한 값이 사용되었을 경우에는 연산의 결과가 true, false가 아닌 truthy 하거나 falsy한 값 그자체가 출력됨
let varA = false;
let varB = true;
// AND 연산자
console.log(varA && varB); // varA가 false이므로 varB값이 true든 false든 상관없이 논리 연산의 결과는 무조건 false -> 따라서 두 번째 피연산자의 값은 아예 접근조차 하지 않게 됨
// OR 연산자
console.log(varA || varB);  // varB가 true이므로 varA 값과 관계없이 무조건 true만 나옴 -> 두번째 피연산자인 varA의 값에는 접근조차 하지 않음

// 단락 평가 예시
function returnFalse() {
  console.log("False 함수");
  return false; // return undefined;도 가능, 같은 의미 -> 이 경우에는 false가 아닌 falsy한 값 자체인 undefined가 콘솔에 출력됨
}

function returnTrue() {
  console.log("True 함수");
  return true;  // return 10;도 가능, 같은 의미
}

console.log(returnFalse() && returnTrue());
// 출력 결과
// False 함수
// false

// returnTrue라는 함수 호출 자체가 안됨 -> 단락 평가가 작동했기 때문


// 단락 평가 활용 사례

function printName(person) {
  const name = person && person.name;
  console.log(name || "person의 값이 없음");
}

printName();  // person에 매개변수를 넘겨주지 않아 undefined가 넘어가 name에 undefined가 저장되고 "person의 값이 없음"이 출력됨
printName({ name: "이정환" });

// printName();의 경우
// person이 undefined이기 때문에 name 변수의 && 연산에서 단락평가에 의해 두번째 피연산자인 person.name에 접근하지 않고 name에 undefined가 저장됨
// console.log의 || 연산에서 name이 undefined로 false이고 두번째 피연산자의 값은 Truthy한 문자열이므로 결과 값으로 Truthy한 문자열이 반환되어 "person의 값이 없음"이 출력됨

// print({ name: "이정환" });의 경우
// person이 객체이므로 Truthy한 값이기 때문에 true로 판단되어 두번째 피연산자인 person.name의 값 "이정환"이 name에 저장됨
// console.log에서 name이 "이정환"으로 두 피연산자 모두 truthy한 값이 되어 첫 번째 truthy한 값만 단락평가에 의해 반환되어 "이정환"이 출력됨

// 참고 : true || true인 경우 첫번째 값이 반환되고, true && true인 경우 두번째(뒤)에 있는 값이 반환됨
