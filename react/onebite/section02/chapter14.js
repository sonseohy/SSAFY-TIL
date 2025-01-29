// 비동기 작업 처리하기 3. async/await
// promise를 더 직관적이고 편하게 사용할 수 있도록 도와주는 async와 await

// async
// 함수 앞에 붙이는 키워드
// 어떤 함수를 비동기 함수로 만들어주는 키워드
// 함수가 프로미스를 반환하도록 변환해주는 그런 키워드

// 예시. 서버로부터 유저의 데이터를 받아오는 함수 
async function getData() {
  return {
    name: "이정환",
    id: "winterlood",
  };  // 이 함수는 async에 의해 비동기 함수로 바뀜 -> 객체를 그대로 반환하는 함수가 아니라 이 객체를 결과값으로 갖는 새로운 promise를 반환하는 함수로 변환됨
}
console.log(getData()); // promise 객체가 반환됨, promise state는 성공 (Fulfilled 상태),결과값은 반환값으로 설정한 객체가 들어있음
// async를 이용하면 간단하게 동기적으로 작동하는 함수를 비동기 작업을 하는 promise를 반환하는 함수로 바꿔줄 수 있음

// async가 붙어있는 함수가 일반적인 객체값을 반환하는게 아닌 return new Promise()같이 애초에 promise를 반환하는 함수였다면?
// 이때는 async 키워드가 별다른 기능을 하지 않고 그냥 promise 객체 자체를 반환하도록 내버려 둠 
async function getData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve({
        name: "이정환",
        id: "winterlood",
      });
    }, 1500);
  });
}
// 결론 : async는 promise를 반환하지 않는 함수에 붙여서 자동으로 해당 함수를 비동기로 작동하도록 변환하는 기능읋 함
// async는 await와 함께 사용했을 때 위력이 제대로 발휘됨

// await
// async 함수(async 키워드가 붙은 함수) 내부에서만 사용이 가능한 키워드
// 비동기 함수가 다 처리되기를 기다리는 역할

async function printData() {
  // 원래 getData 함수가 반환하는, promise에 담긴 결과 값을 사용해야 된다면 getData().then((result) => { console.log(Result); }); then 메서드를 붙여 결과값을 매개변수로 받아왔어야 함
  // async와 await를 이용하면 더 이상 then 메서드를 복잡하게 쓸 필요없음
  // Why? 함수 앞에 async를 붙이고 함수 호출 앞에 await를 붙여주면 then 메서드를 쓰지 않아도 알아서 getData 함수가 반환하는 promise가 종료되기를 (이 라인에서) 기다림
  // 아래와 같이 일반적인 함수를 호출하듯 작성해주면 data 변수에 getData 함수가 반환하는 prmoise의 비동기 작업이 종료되기까지 기다렸다가 종료가 되면 결과값을 변수에 넣어줌
  const data = await getData();
  console.log(data);
}

printData();

// await 함수는 async가 붙지 않은 함수에서 사용하면 오류 발생
// -> async 키워드가 붙은 함수 안에서만 쓸 수 있다.
