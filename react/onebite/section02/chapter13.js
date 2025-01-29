// 비동기 작업 처리하기 2. Promise
// Promise
// - 비동기 작업을 효율적으로 처리할 수 있도록 도와주는 자바스크립트의 내장 객체
// - 날짜를 저장하는 Date 객체처럼 특수한 목적을 위해서 존재하는 내장 객체
// - Promise는 비동기 작업을 감싸는 객체
// - Promise의 효능 : 비동기 작업 실행, 비동기 작업 상태 관리, 비동기 작업 결과 저장, 비동기 작업 병렬 실행, 비동기 작업 다시 실행 등등.. -> 비동기 작업을 처리하는데 필요한 거의 모든 기능을 다 제공해주는 객체

// Promise는 비동기 작업을 진행 단계에 따라 세 가지의 상태로 나누어서 관리함
// 1. 대기 상태 (Pending 상태) : 아직 비동기 작업이 진행중인, 완료되지 않은 상태
// 2. 성공 상태 (Fulfilled 상태) : 비동기 작업이 별다른 오류 없이 성공적으로 마무리 된 상태를 의미
// 3. 실패 상태 (Rejected 상태) : 비동기 작업이 모종의 이유(네트워크 에러, 코드를 잘못 작성 등)로 실패된 상태를 의미
// 추가로 어떠한 비동기 작업이 대기 상태였다가 성공적으로 완료되어 성공 상태로 바뀌는 걸 해결되었다라는 의미에서 resolve 되었다라고 표현
// 반대로 어떠한 비동기 작업이 대기 상태였다가 모종의 이유로 실패해서 실패 상태로 바뀌는 건 거부되었다는 의미에서 Reject 되었다고 표현함

function add10(num) {
  const promise = new Promise((resolve, reject) => {  // 생성자를 이용, 생성자의 인수로는 비동기 작업을 실제로 진행할 콜백 함수를 넣어주면 됨
    // 콜백 함수 안에 비동기 작업을 진행하는 코드를 작성하면 Promise 객체가 생성됨과 동시에 자동으로 콜백 함수를 호출해서 안에 있는 비동기 작업들을 실행해줌
    // 이 콜백 함수를 특별히 실제로 비동기 작업을 실행하는 함수라고 해서 executor라고 부름
    
    // executor 함수 : 프로미스 객체를 생성하면서 인수로 전달되는 콜백 함수
    setTimeout(() => {
      if (typeof num === "number") {
        resolve(num + 10);
      } else {
        reject("num이 숫자가 아닙니다");
      }
    }, 2000);
  });

  return promise;
}

console.log(promise); // 프로미스 객체가 출력되고 2초 뒤 executor 함수의 실행 결과가 출력됨
                      // 출력된 객체를 자세히 보면 Promise 객체의 상태는 Pending이라고 해서 대기 상태에 있는 것을 볼 수 있고, promise result, 즉 결과 값은 아직 대기 상태이므로 일단 undefined로 저장되어 있는 것을 볼 수 있음

// executor 함수에는 두 가지의 매개변수가 전달됨 : resolve, reject
// - resolve : resolve라는 첫 번째 매개변수에는 promise의 작업, 즉 비동기 작업을 성공 상태로 바꾸는 함수가 들어있음
// - reject : reject라는 두 번째 매개변수에는 promise가 관리하는 비동기 작업을 실패 상태로 바꾸는 함수가 들어있음
// 만약 executor에서 실행하는 비동기 작업을 성공했다고 알리고 싶다면 resolve 함수를 호출해주면 됨 -> resolve 함수가 호출되면 promise 객체의 상태를 성공, 즉 Fulfilled 상태로 바꿔줌
// But. 상태는 fulfilled로 바뀌지만 결과값은 undefined로 저장되지 않은 것을 볼 수 있음
// -> 결과값은 execute 함수 내부에서 resolve 함수를 호출하면서 인수로 전달해줘야 함

// reject를 호출한 다음 인수로는 왜 실패했는지 이유를 인수로 넘겨줌 -> 실행하면 promise 객체가 실패했고 이유는 무엇이라는 오류가 발생
// 정리 : executor 함수에서 reject를 호출하게 되면 promise의 비동기 작업이 실패하게 되고, 반대로 resolve를 호출하게 되면 promise의 비동기 작업이 성공하게돰
// 각각 resolve와 reject 함수 모두 인수로 promise의 결과 값을 전달해줄 수 있다

const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    const num = 10;

    if (typeof num === "number") {
      resolve(num + 10);
    } else {
      reject("num이 숫자가 아닙니다");
    }
  }, 2000);
});
// then 메서드
// -> 그 후에
// promise의 결과값을 직접 이용하기 위해 promise 객체의 메서드인 then이라는 메서드를 호출해야됨
// promise.then으로 메서드를 호출하고 인수로 콜백 함수를 넣어주면 promise가 성공하게 되면, 즉 execute 함수에서 resolve를 호출하게 되면 그 후에 then 메서드에 전달한 콜백 함수를 실행시켜줌
// -> 동시에 resolve의 인수로 전달한 결과값을 매개변수로까지 제공해줌
promise.then((value) => { // value라는 매개변수로 resolve의 결과값을 받아서
  console.log(value); // value 값을 그대로 출력 -> 20
});
// then 메서드를 이용하면 promise로 관리하는 비동기 작업의 결과 값을 언제든지 자유롭게 불러다가 이용할 수 있다.

// 만약 reject가 호출되어 실패한다면 then 메서드는 실행되지 않음
// -> then 메서드는 promise의 비동기 작업이 성공했을때만 호출되는 메서드이기 때문
// 이때는 then이 아닌 promise의 catch라는 메서드를 사용하면 됨
// catch 메서드
// - 실패 버전의 then 메서드 같은 것으로, 똑같이 인수로 콜백 함수를 전달해주면 promise가 실패했을때 콜백 함수를 실행시켜주게 됨
// -> then 메서드와 마찬가지로 매개변수로 결과값까지 제공해줌
promise.catch((error) => {
  console.log(error); // reject의 결과값인 'num이 숫자가 아닙니다'가 콘솔에 출력됨
});

// then과 catch 메서드를 잘 활용하면 promise가 관리하는 비동기 작업이 성공하거나 실패했을 때 결과값을 이용할 수 있다.

// promise의 then 메서드는 promise를 한 번 다시 반환한다!
// then 메서드의 호출 결과가 promise를 반환한다는 의미
// 어떤 promise 객체를 반환하냐면 해당 promise 객체를 그대로 다시 반환함
// -> 그렇기 때문에 catch 메서드를 호출하고 있는 promise나 then 메서드가 호출하고 있는 promise나 똑같은 promise 객체라는 것
// -> 따로 catch 메서드를 호출하지 말고 뒤에 catch 메서드를 연결해서 사용하는 것도 가능
promise.then((value) => {
  console.log(value);
}).catch((error) => {
  console.log(error);
});
// 비동기 작업이 reject 되면 then 메서드가 아닌 연결된 catch 메서드가 실행되면서 error 값이 출력됨
// then과 catch를 연달아서 사용하는 문법을 마치 chaining 하는 것 같다라고 해서 특별히 Promise Chaining이라고 표현


// 비동기 작업을 고정된 값이 아닌 함수를 하나 만들어서 함수 안에서 promise 객체를 새롭게 생성하면서 동적으로 매개변수를 받아서 숫자 값을 바꿔가면서 사용할 수 있도록 개선
function add10(num) { // 매개변수로 num을 받아옴옴
  const promise = new Promise((resolve, reject) => {

    setTimeout(() => {
      if (typeof num === "number") {
        resolve(num + 10);
      } else {
        reject("num이 숫자가 아닙니다");
      }
    }, 2000);
  });

  return promise; // promise 객체를 그대로 반환하는 함수
}

// add10 함수를 호출하고 인수로 숫자값 0을 넘겨주면 함수 내부에서 새로운 promise 객체가 생성되면서 비동기 작업이 실행되고 해당하는 promise 객체 반환까지 이루어짐
// promise 객체를 이용해도 비동기 작업의 결과를 또 다른 비동기 작업의 인수로 전달할 수 있음
const p = add10(0);
p.then((result) => {
  console.log(result);

  // then 메서드의 콜백함수 안에서 한번 더 add10 함수를 호출하면서 인수로는 결과값인 result를 전달하게 되면 
  const newP = add10(result); // 호출한 add10 함수가 새로운 promise 객체를 또 반환
  newP.then((result) => {
    console.log(result);
  });
}); // 10, 20이 출력됨
// 위 코드는 chapter12와 같이 콜백 지옥이 발생할 것 같음
// -> promise는 콜백 지옥을 방지하기 위한 엄청난 기능을 제공함
// - then 메서드 안에서 retunrn newP라고 해서 새로운 promise 객체를 반환해주면 반환된 promise 객체가 then 메서드 호출의 결과값이 됨
const p2 = add10(0);
p.then((result) => {
  console.log(result);

  const newP = add10(result);
  newP.then((result) => {
    console.log(result);
  });
  return newP;  // 원래는 아무것도 반환하지 않았다면 원본 promise 객체(p2)를 반환했지만 새로운 프로미스 객체를 반환하도록 해주면 이제는 then 메서드의 결과값이 새로운 promise 객체가 된다는 것
});
// 그렇기 때문에 then 메서드를 연달아 붙여 작성 가능
const p3 = add10(0);
p.then((result) => {
  console.log(result);

  const newP = add10(result);
  return newP;
}).then((result) => {
  console.log(result);  // newP라는 promise에 저장된 then 메서드는 여기서 실행됨
});

// 간결 version
add10(0)
  .then((result) => {
    console.log(result);
    return add10(result);
  })
  .then((result) => {
    console.log(result);
    return add10(undefined);
  })
  .then((result) => {
    console.log(result);
  })
  .catch((error) => { // 비동기 작업이 실패할 수 있는 상황 생각해 작성
    console.log(error);
  });