// 순회
// 배열, 객체에 저장된 여러개의 값에 순서대로 하나씩 접근하는 것

// 1. 배열 순회
let arr = [1, 2, 3];

// 1.1 배열 인덱스
// length 프로퍼티는 모든 배열이 다 가지고 있는 기본적인 프로퍼티로서 배열의 길이를 저장하고 있는 프로퍼티
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]); // 인덱스를 통해 순회할 수 있다.
}

let arr2 = [4, 5, 6, 7, 8];
for (let i = 0; i < arr2.length; i++) {
  console.log(arr2[i]);
}

// 1.2 for of 반복문
// for of 반복문은 오직 배열을 순회하기 위해서만 존재하는 특수한 반복문
// 기본적인 문법은 for문과 비슷, for문을 사용하듯이 똑같이 만들어준 후 소괄호 안에 let item of (순회하고자하는 배열) 작성
// of 뒤에 있는 배열의 값을 하나씩 순서대로 꺼내서 변수 item에 저장 -> 첫번째 반복에서는 item에 1이 들어가고 두번째 반복에서는 item에 2가 들어가는 방식
for (let item of arr) {
  console.log(item);
}

// 인덱스를 사용하는 방법과 FOR-OF를 사용하는 방식에 성능 차이는 없으나 한 가지 차이점은
// 인덱스를 이용하는 방식은 카운터 변수에 인덱스가 저장되기 때문에 for문 안에서 인덱스를 통한 활동을 할 수 있는 반면,
// for-of를 이용하는 방식은 인덱스를 저장하지 않고 배열 안의 값들을 순서대로 순회만 해줌

// 2. 객체 순회
let person = {
  name: "이정환",
  age: 27,
  hobby: "테니스",
};

// 2.1 Object.keys 사용 (내장함수)
// -> 객체에서 key 값들만 뽑아서 새로운 배열로 반환
let keys = Object.keys(person); // person 객체로부터 키 값들만 모아서 새로운 배열로 반환
console.log(keys); // ['name', 'age', 'hobby']

for (let key of keys) {
  const value = person[key];
  console.log(key, value);
}

// 2.2 Object.values (내장함수)
// -> 객체에서 value 값들만 뽑아서 새로운 배열로 반환
let values = Object.values(person);
console.log(values); // ['이정환', 27, '테니스']

for (let value of values) {
  console.log(value);
}

// 2.3 for in
// 객체만을 위해 존재하는 특수한 반복문 (for of와 비슷)
// in 뒤에 있는 Person 객체의 Property의 key를 순서대로 key라는 변수에 할당해줌
for (let key in person) {
  const value = person[key];
  console.log(key, value);
}

// 주의! for of는 배열에서만 사용가능, for in은 객체에서만 사용가능
