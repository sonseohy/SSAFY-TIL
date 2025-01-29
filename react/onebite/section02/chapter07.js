// 6가지의 요소 조작 메서드

// 1. push
// 배열의 맨 뒤에 새로운 요소를 추가하는 메서드
let arr1 = [1, 2, 3];
// arr1.push(4, 5);
// push 메서드는 요소들을 추가하고 난 다음 변환된 배열의 길이를 반환함
const newLength = arr1.push(4, 5, 6, 7);
console.log(newLength); // 7

// 2. pop
// 배열의 맨 뒤에 있는 요소를 제거하고, 반환
let arr2 = [1, 2, 3];
const poppedItem = arr2.pop();
console.log(poppedItem); // 3

// 3. shift
// 배열의 맨 앞에 있는 요소를 제거, 반환
let arr3 = [1, 2, 3];
const shiftedItem = arr3.shift();
console.log(shiftedItem); // 1

// 4. unshift
// 배열의 맨 앞에 새로운 요소를 추가하는 메서드
let arr4 = [1, 2, 3];
const newLength2 = arr4.unshift(0);
console.log(arr4); // [0, 1, 2, 3]
// push 메서드와 동일하게 값을 추가하고 난 이후에 변경된 배열의 길이를 동시에 반환함
console.log(newLength2); // 4

// 주의 : shift와 unshift는 push나 pop보다는 느리게 동작하게 된다.
// why? 맨 앞에 요소를 제거하거나 추가하는 메서드는 인덱스를 미뤄야 하거나 당기는 등의 작업이 필요하기 때문 -> 비효율적인 작업이 발생하므로 push나 pop에 비해 비교적 느리게 동작
// 되도록 push나 pop을 통해서 해결하는 것이 좋다.

// 5. slice
// 마치 가위처럼, 배열의 특정 범위를 잘라내서 새로운 배열로 반환
// 배열명.slice(자르기 시작할 인덱스, 잘라낼 범위의 끝 인덱스 + 1);
// slice로 원본 배열을 잘라냈다고 하더라도 원본 배열 값이 바뀌진 않음
let arr5 = [1, 2, 3, 4, 5];
let sliced = arr5.slice(2, 5);
console.log(sliced); // [3, 4, 5]
// 배열의 끝까지 잘라달라는 방식으로 슬라이드 메서드를 쓸 거면 두 번째 인수는 생략해도 됨
// 슬라이스 메서드의 두 번째 인수를 생략하면 자르기 시작할 부분부터 배열 끝까지 잘라냄
let sliced2 = arr5.slice(2);
console.log(sliced2); // [3, 4, 5]
// 배열의 뒤에서부터 잘라내고 싶으면 음수값 사용
let sliced3 = arr5.slice(-3); // 뒤에서부터 3개 잘라라
console.log(sliced3); // [3, 4, 5]

// 6. concat
// 두개의 서로 다른 배열을 이어 붙여서 새로운 배열을 반환
let arr6 = [1, 2];
let arr7 = [3, 4];

let concatedArr = arr6.concat(arr7); // arr6 배열의 뒤에 arr7 배열의 값들이 붙어서 새로운 배열로 반환됨
console.log(concatedArr); // [1, 2, 3, 4]
