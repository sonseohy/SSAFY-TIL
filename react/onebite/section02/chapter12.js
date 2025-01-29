// 비동기 작업 처리하기 1. 콜백 함수
// 비동기 작업의 결과를 콜백 함수로 처리하는 방법
// 응용 : 어떤 비동기 작업의 결과를 또 다른 비동기 작업의 인수로 활용 (예제 2)

// 예제 1.
function add(a, b) {
  setTimeout(() => {
    const sum = a + b;
    console.log(sum);
  }, 3000);
}

add(1, 2);  // 3초 뒤에 3 출력

// 비동기 처리의 결과값인 sum이라는 변수를 add 함수 바깥에서도 사용할 수 있도록 만드려면?
// 이 때는 add 함수를 호출할 때 인수로 비동기 처리의 결과 값을 사용하고자 하는 콜백 함수를 함께 전달해주면 됨
function add(a, b, callback) {  // add 함수에서는 세번째 인수로 전달한 callback 함수를 매개변수로 다시 받아서
  setTimeout(() => {
    const sum = a + b;
    // console.log(sum);
    callback(sum);  // setTimeout 함수 안에 콘솔을 대체해서 호출하고 인수로는 결과값인 sum을 넣어줌
  }, 3000);
}

add(1, 2, (value) => {  // 콜백 함수를 하나 추가해 value라는 매개변수를 받아 콘솔에 그대로 출력하도록 만들기
  console.log(value);
});

// 동작 방식
// 1. add 함수가 호출되면서 setTimeout 함수가 호출됨
// 2. setTImeout 함수는 콜백 함수를 3초 뒤에 실행
// 3. 3초 뒤에 실행된 콜백 함수에서 sum이라는 값을 계산한 다음 매개변수로 받은 callback 함수를 다시 호출하면서 sum 값을 전달해줌
// 4. setTimeout 함수가 끝났을 때 add의 3번째 인수인 콜백 함수가 한번 더 실행되어 배개변수로 3이라는 값이 들어오게 되고 출력됨
// 정리 : 비동기 작업을 하는 함수의 결과 값을 함수 외부에서 이용하고 싶다면 콜백 함수를 사용해 비동기 함수 안에서 콜백 함수를 호출하도록 설정해주면 된다.


// 예제 2. 음식을 주문하는 상황
function orderFood(callback) {  // food 변수를 orderFood 함수 바깥에서도 이용할 수 있도록 매개변수로 callback 함수를 받아 이 함수를 setTimeout 함수 안에서 호출하고 인수로 비동기 작업의 결과 값을 전달해주면 됨
  setTimeout(() => {
    const food = "떡볶이";
    callback(food);
  }, 3000);
}

// 음식을 식히는 함수 (추가적인 비동기 작업)
function cooldownFood(food, callback) { // 식힐 음식을 매개변수로 받아오고, 식힌 음식을 인수로 바깥에 다시 전달해주기 위해 콜백함수를 매개변수에 추가
  setTimeout(() => {
    const cooldownedFood = `식은 ${food}`;
    callback(cooldownedFood);
  }, 2000);
}

// 식어버린 음식을 아예 냉동해버리는 함수
function freezeFood(food, callback) { // 얼릴 음식과 해당 결과 값을 함수 외부에 전달하기 위핸 callback 함수를 받아올 callback 매개변수 추가
  setTimeout(() => {
    const freezedFood = `냉동된 ${food}`;
    callback(freezedFood);  // 매개변수에 담긴 함수(callback)를 setTimeout 함수 안에서 호출하고 인수로 freezeFood 전달
  }, 1500);
}

orderFood((food) => { // orderFood 함수 호출한 뒤 이 함수에 callback 함수를 넣고 매개변수로 food를 받아 콘솔에 출력하도록 작성
  console.log(food);  // 3초 뒤에 '떡볶이'가 출력됨

  cooldownFood(food, (cooldownedFood) => {  // 비동기 작업의 결과(food)를 또 다른 비동기 작업의 인수로 전달하는 것도 가능
    console.log(cooldownedFood);  // 위에서 콜백 함수의 인수로 cooldownedFood가 전달 되므로 똑같이 cooldownedFood라는 매개변수를 받아 콘솔에 출력

    freezeFood(cooldownedFood, (freezedFood) => {
      console.log(freezedFood);
    });
  });
});

// 콜백 함수를 이용해 받아온 비동기 작업의 결과를 또 다른 비동기 작업의 인수로 넣어주는 이러한 코드가 계속 반복이 되다보면 콜백 함수 안에서 계속 함수를 호출하는 문법으로 코드가 계속 작성됨
// -> 인덴트(indent, 들여쓰기)가 점점 깊어지는 형태로 코드가 진화
// -> 코드가 깊어지는 방식으로 계속 작성하면 기능이 늘어날수록 가독성이 점점 안좋아짐
// -> 이런 문제를 자바스크립트 프로그래머들이 콜백 지옥이라고 부르는데, 콜백 지옥을 피하려면 다음 내용인 Promise라는 비동기 작업을 도와주는 객체를 이용하면 됨
