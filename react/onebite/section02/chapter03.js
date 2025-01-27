// 구조 분해 할당
// 배열이나 객체에 저장된 여러 개의 값을 분해해서 각각 다른 변수에 할당하는 문법

// 1. 배열의 구조 분해 할당
// 배열에 들어있는 원소들을 각각의 변수에 일일이 다 할당을 해줘야 된다라고 하면 배열을 표현하듯 대괄호 안에 할당할 변수명을 차례로 작성
// 그 다음 초기 값으로 arr 배열을 넣어줌 -> arr 배열에 있는 원소들이 순서대로 변수에 각각 할당됨
let arr = [1, 2, 3];

// let [one, two] = arr;   // 배열의 일부 원소만 변수에 할당하는 것도 가능
// let [one, two, three, four] = arr;   // 배열 원소의 개수를 넘어서서 추가로 선언해도 오류 발생 X -> four에 초기화가 되지 않은 변수처럼 undefined가 저장됨
let [one, two, three, four = 4] = arr;  // 값이 모자랄 상황을 대비해 four = 4처럼 기본값을 설정할 수 있음
console.log(one, two, three, four); // 1 2 3 4


// 2. 객체의 구조 분해 할당
// 객체의 경우에도 배열처럼 존재하지 않는 프로퍼티를 구조분해 할당으로 받으려고 하면 undefined가 저장됨, 기본값 설정도 가능
let person = {
  name: "이정환",
  age: 27,
  hobby: "테니스",
};

// let { name, age, hobby } = person;  // 중괄호를 이용해 각각 객체의 프로퍼티를 키 값을 기준으로 변수에 저장할 수 있음 -> name 변수에는 이정환, age 변수에는 27, hobby 변수에는 테니스가 저장됨
// 객체 구조 분해 할당에서는 특별하게 할당받는 변수의 이름을 변경할 수도 있음
// -> age: myAge처럼 콜론을 이용해 변경할 이름을 작성하면 age가 아니라 myAge라는 변수에 age 프로퍼티의 값이 저장됨
let {
  age: myAge,
  hobby,
  name,
  extra = "hello",
} = person;

// 3. 객체 구조 분해 할당을 이용해서 함수의 매개변수를 받는 방법
// 객체의 구조 분해 할당은 함수에 여러 개의 인수를 전달할 때 자주 사용됨
// 주의! 객체를 넘겼을 때만 중괄호와 함게 구조분해 할당을 받을 수 있음 (person이라는 객체를 넘겼기 때문에 구조분해 할당이 가능한 것)
const func = ({ name, age, hobby, extra }) => {
  console.log(name, age, hobby, extra);
};

func(person);

// 원래는 이런식으로 객체를 받아와 함수에서 사용용
// const func = (person) => {
//   person.name;
//   person.age;
// }