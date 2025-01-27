// 1. 콜백함수
// 자신이 아닌 다른 함수에, 인수로써 전달된 함수를 의미
// 어떠한 함수를 다른 함수의 인수로 전달해서 나중에 호출시키도록(해당 함수에서 알아서 호출하도록) 설정한 함수를 콜백함수라고 부름
// 콜백 : 프로그래밍에서 뒷전에 또는 나중에 실행되는 이라는 뜻으로 쓰임
function main(value) {  // 콜백 함수는 main 함수가 언제든지 원하는 타이밍에 실행시킬 수 있음
  value();
}
                                                                                                                                                                                                                              
// 2. 콜백함수의 활용
function repeat(count, callback) {  // 매개변수에 callback 함수를 추가해 
  for (let idx = 1; idx <= count; idx++) {
    callback(idx);  // 매 반복마다 콜백 함수를 호출하면서 idx 값 전달
  }
}

// 프로그래밍을 하다보면 아래 repeat과 같이 구조가 거의 흡사한 함수들을 만들게 될 일이 굉장히 많음
// 구조가 흡사한 함수들이 필요할 때 마다 함수명을 다르게 해서 생성하면 계속 중복코드를 발생시켜 좋지 않음 (ex. idx*2를 출력하는 함수, idx*3을 출력하는 함수..)
// 콜백 함수를 이용하면 중복 코드를 발생시키지 않으면서 코드개선 가능
repeat(5, function (idx) {  // 함수 표현식 사용
  console.log(idx);
});

repeat(5, (idx) => {  // 화살표 함수 사용
  console.log(idx * 2);
});

repeat(5, (idx) => {
  console.log(idx * 3); 
});


// 콜백함수 사용
// 1. sub 함수를 선언해서 사용
function sub() {
  console.log("I am sub");
}
main(sub);

// 2. 선언문 자체를 안에 넣어서 함수 표현식처럼 쓰는 것도 가능
main(function sub() {
  console.log("I am sub");
});
// 함수 표현식에서는 익명 함수로 써도 전혀 문제되지 않음
main(function () {
  console.log("I am sub");
});
// 화살표 함수로 만들어 쓰기도 가능
main(() => {
  console.log("I am sub");
});