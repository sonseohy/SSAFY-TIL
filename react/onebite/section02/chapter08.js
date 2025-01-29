// 5가지 요소 순회 및 탐색 메서드
// 1. forEach
// 모든 요소를 순회하면서, 각각의 요소에 특정 동작을 수행시키는 메서드
// 배열의 모든 요소를 한 번씩 순회하면서 콜백 함수로 해당 요소를 이용해 무언가 동작을 수행시키도록 만들어 줄 수 있음
let arr1 = [1, 2, 3];

// forEach 메서드를 호출한 후 메서드에 인수로 콜백함수를 넣어줌
// forEach 메서드가 배열의 요소들을 반복문처럼 순회하면서 매 반복마다 콜백 함수를 호출하고 매개변수로 현재 요소의 값과 현재 반복 카운트와 전체 배열의 값을 전달해줌
arr1.forEach(function (item, idx, arr) {
  // item은 배열의 요소(처리할 현재 요소), idx는 반복 카운트(처리할 현재 요소의 인덱스), arr에는 forEach 메서드를 호출한 배열
  console.log(idx, item * 2);
});

let doubledArr = [];

arr1.forEach((item) => {
  doubledArr.push(item * 2);
});

console.log(doubledArr); // [2, 4, 6]

// 2. includes
// 배열에 특정 요소가 있는지 확인하는 그런 메서드
let arr2 = [1, 2, 3];
let isInclude = arr2.includes(10); // includes 메서드를 호출하고 인수로 해당 배열에서 찾으려는 값을 넣어줌

console.log(isInclude); // false

// 3. indexOf
// 특정 요소의 인덱스(위치)를 찾아서 반환하는 메서드
let arr3 = [2, 2, 2];
let index = arr3.indexOf(2); // 0, 배열에 찾으려는 값이 여러 개 존재한다면 indexOf는 배열의 맨 앞에서부터 탐색을 시작하기 때문에 가장 첫 번째로 찾아낸 요소의 인덱스를 반환
let index2 = arr3.indexOf(20); // -1, 현재 배열에 존재하지 않는 값의 인덱스를 찾아달라고 하면 존재하지 않는다는 의미로 -1을 반환해줌

// 4. findIndex
// 모든 요소를 순회하면서, 콜백함수를 만족하는 그런
// 특정 요소의 인덱스(위치)를 반환하는 메서드
let arr4 = [1, 2, 3];
// findIndex 메서드 호출 후 인수로 콜백 함수를 전달 -> 이렇게 전달한 콜백 함수를 만족하는(참을 반환하는) 요소를 배열에서 찾아 그 인덱스 반환해줌
// 배열의 요소들을 순회하면서 가장 처음 이 조건문을 만족시키는 요소의 위치를 찾아서 그 인덱스 반환해줌
// const findedIndex = arr4.findIndex((item) => {
//   if (item % 2 !== 0) return true;
// });
// console.log(findedIndex); // 0

// 위 코드 간단 ver
// if문 안의 조건식을 따로 복사해 중괄호 내부를 다 지우고 조건식을 리턴하도록 만들어줌
// const findedIndex = arr4.findIndex((item) => item % 2 !== 0);
const findedIndex = arr4.findIndex((item) => item === 999); // 조건을 만족하는 요소가 배열에 존재하지 않는다면 -1 반환

console.log(findedIndex); // -1

// findIndex가 존재하는 이유?
// indexOf라는 메서드는 배열에 원시 타입의 값이 들어있을 때가 아니라 객체 타입의 값들이 저장된 배열에서는 정확한 요소의 위치를 찾아낼 수 없기 때문
// 예시
// let objectArr = [
//   { name: "이정환" },
//   { name: "홍길동" },
// ];

// console.log(
//   objectArr.indexOf({ name: "이정환" })
// ); // -1, 인수로 객체 값과 일치하는 요소의 인덱스를 반환하라고 했는데 못찾음
// Why? indexOf는 기본적으로 얕은 비교로 동작하기 때문
// - 얕은 비교는 동등 비교 연산자(===)를 이용해서 비교한다는 것
// -> 객체 값들은 이전 시간에 살펴봤던 것처럼 참조값을 기준으로 비교가 되기 때문에 프로퍼티를 기준으로는 비교가 이루어지지 않음
// -> 그렇기 때문에 indexOf로는 배열에서 특정 객체값이 존재하는지 찾아낼 수가 없음
// -> 이럴 때 findIndex 사용

// console.log(
//   // objectArr.findIndex()메서드를 호출하고 콜백함수를 이용해 item의 값 중 item.name이 이정환인 요소의 위치를 찾아서 반환하라고 설정해주고 콘솔 출력하면 0이라는 정확한 위치를 찾아냄
//   objectArr.findIndex(
//     (item) => item.name === "이정환"
//   )
// ); // 0, 정확한 위치를 찾아낼 수 있음

// 결론
// indexOf 메서드는 특정 값을 배열에서 찾을 때 무조건 얕은 비교로만 진행하기 때문에 객체 값은 찾지 못하는 반면
// FindIndex는 콜백 함수를 이용해 직접 특정 프로퍼티의 값을 기준으로 비교시킬 수 있기 때문에 복잡한 객체 값도 조건식을 잘 만들어주면 쉽게 찾아낼 수 있다는 장점 존재
// 따라서 단순한 원시 타입의 값을 찾을 때는 indexOf,복잡한 객체 타입의 값을 찾을 땐 FindIndex를 쓰면 좋다.

// 5. find
// 모든 요소를 순회하면서 콜백함수를 만족하는 요소를 찾는데, 요소를 그대로 반환

let arr5 = [{ name: "이정환" }, { name: "홍길동" }];

const finded = arr5.find((item) => item.name === "이정환");

console.log(finded); // { name: "이정환" }, 첫번째로 찾은 객체 자체가 반환됨
