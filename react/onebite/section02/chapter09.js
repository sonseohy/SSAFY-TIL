// 5가지 배열 변형 메서드
// 참고 링크 : https://reactjs.winterlood.com/fc0a951e-41cd-4cc5-8f47-7507965bbe41#8f2d70d5e8334377bb56f0a3f9101de2
// 1. filter
// 기존 배열에서 조건을 만족하는 요소들만 필터링하여 새로운 배열로 반환
// 참고 : filter 메서드는 웹 서비스를 개발할 때 특정 조건에 의해서 검색시키는 기능이나 카테고리별 필터 같은 기능을 만드는데 거의 필수적으로 사용됨

let arr1 = [
  { name: "이정환", hobby: "테니스" },
  { name: "김효빈", hobby: "테니스" },
  { name: "홍길동", hobby: "독서" },
];

// filter 메서드는 콜백 함수를 이용해 배열의 모든 요소들을 순회하면서 조건을 만족하는 값들만 새로운 배열로 반환해주는 역할을 함 (Find, FindIndex 메서드처럼)
// const tennisPeople = arr1.filter((item) => {
//   if (item.hobby === "테니스") return true;
// });
// console.log(tennisPeople); // [{ name: "이정환", hobby: "테니스" }, { name: "김효빈", hobby: "테니스" },]

const tennisPeople = arr1.filter((item) => item.hobby === "테니스"); // 조건문만 떼어와서 조건식만 반환하는 걸로 단축해서 사용 가능

// 2. map
// 자주 활용되는 메서드
// 배열의 모든 요소를 순회하면서, 각각 콜백함수를 실행하고 그 결과값들을 모아서 새로운 배열로 반환
// map 메서드는 특별히 callback 함수 안에서 return item * 2 이런 식으로 반환값을 설정해 줄 수도 있음
// -> 이렇게 해주면 map 메서드가 콜백 함수가 반환한 값들을 모두 모아서 새로운 배열로 반환시켜줌
let arr2 = [1, 2, 3];
const mapResult1 = arr2.map((item, idx, arr) => {
  // 매개변수로 forEach와 동일하게 현재 요소, 반복 카운트, 원본 배열을 전달 받음 (filter도 동일)
  return item * 2;
});
console.log(mapResult1); // [2, 4, 6]

// 결론 : map 메서드를 사용하면 원본 배열의 값들을 변형한 새로운 배열을 생성할 수 있음

// 실용적 사례 : arr1 배열에 있는 객체 값들에서 name 프로퍼티에 있는 이름 값들만 따로 뽑아서 새로운 배열로 추출
let names = arr1.map((item) => item.name);
console.log(names); // ["이정환", "김효빈", "홍길동"]

// 3. sort
// 배열을 사전순으로 정렬하는 메서드
// sort 메서드는 호출만 해도 배열의 요소들을 자동으로 정렬 해줌
// let arr3 = ["b", "a", "c"];
// arr3.sort();
// console.log(arr3);  // ['a', 'b', 'c']
// 주의! 배열의 값이 문자열로 이루어져 있는 것이 아닌 숫자 값으로 이루어진 배열이었다라고 하면 sort 메서드가 정상적으로 동작하지 않음
let arr3 = [10, 3, 5];
arr3.sort();
console.log(arr3); // [10, 3, 5], 정렬이 정상적으로 이루어지지 않고 그대로 출력됨
// why? sort 메서드는 배열을 사전순으로 정렬하기 때문 -> 숫자의 대소비교를 통해 정렬한 게 아니라 사전 순으로 정렬함
// 숫자의 대소관계를 기준으로 정렬하고 싶다면 sort 메서드를 호출하면서 비교 기준을 설정하는 콜백 함수도 함께 넘겨주어야 함
// 콜백 함수에서는 두 개의 배열 요소 a, b를 받아서 두 배열 요소를 비교할 때 뭐가 더 크고 작은 값이라고 판단할 것인지 함수 안에 다 설정해주어야 함
arr3.sort((a, b) => {
  // 오름차순 숫자 정렬 (내림차순 정렬은 조건을 반대로)
  if (a > b) {
    // b가 a 앞에 와라
    return 1; // sort 메서드에서 양수를 반환하게 되면 b를 a 앞에 오도록 배치함 -> b, a 배치
  } else if (a < b) {
    // a가 b 앞에 와라
    return -1; // 음수를 반환하게 되면 반대로 a가 b 앞에 오도록 배치됨 -> a, b 배치
  } else {
    // 두 값의 자리를 바꾸지 마라
    return 0; // 0을 반환하게 되면 A와 B의 자리를 그대로 유지함 -> a, b 자리를 그대로 유지
  }
});

// 4. toSorted (가장 최근에 추가된 최신 함수)
// 정렬된 새로운 배열을 반환하는 메서드
// sort와 차이점? sort는 원본 배열 자체를 정렬시키는 메서드, toSorted 메서드는 원본 배열은 두고 새로운 배열을 반환하는 메서드
// toSorted는 sort와 동일하게 배열을 사전 순으로 정렬하지만, 원본 배열을 정렬하는게 아닌 정렬된 배열을 새롭게 반환하는 함수
let arr5 = ["c", "a", "b"];
const sorted = arr5.toSorted();

console.log(arr5); // ['c', 'a', 'b']
console.log(sorted); // ['a', 'b', 'c']

// 5. join
// 배열의 모든 요소를 하나의 문자열로 합쳐서 반환하는 그런 메서드
let arr6 = ["hi", "im", "winterlood"];
// const joined = arr6.join();
// console.log(joined); // hi,im,winterlood -> 여기서 ,(콤마)는 separator, 즉 구분자라고 해서 이 배열의 요소와 요소 사이에 들어가는 문자를 말함
// 구분자를 바꿔주고 싶다면 join 메서드의 인수로 바꾸고 싶은 구분자를 넣어주면 됨 (ex.-(dash), |(bar), 공백 등)
const joined = arr6.join(" ");
console.log(joined);
