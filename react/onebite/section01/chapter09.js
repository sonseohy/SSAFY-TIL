// 1. if 조건문 (if문)
// else if문은 개수의 제한이 없음
let num = 4;

if (num >= 10) {
  //   console.log("num은 10 이상입니다");
  //   console.log("조건이 참 입니다!");
} else if (num >= 5) {
  //   console.log("num은 5 이상입니다");
} else if (num >= 3) {
  //   console.log("num은 3 이상입니다");
} else {
  //   console.log("조건이 거짓입니다!");
}

// 2. Switch 문
// -> if문과 기능 자체는 동일
// -> 다수의 조건을 처리할 때 if보다 더 직관적이다.

let animal = "cat";

// switch문의 소괄호 안에는 변수가 들어감
// switch 이후 소괄호에 조건식이 아닌 비교하고 싶은 변수를 하나 넣어주면 됨
// 중괄호 안에서 case문을 통해 animal 변수의 값이 될 수 있는 후보들을 다 적어주면 됨
switch (animal) {
  case "cat": {
    console.log("고양이");
    break;
  }
  case "dog": {
    console.log("강아지");
    break;
  }
  case "bear": {
    console.log("곰");
    break;
  }
  case "snake": {
    console.log("뱀");
    break;
  }
  case "tiger": {
    console.log("호랑이");
    break;
  }
  default: {
    console.log("그런 동물은 전 모릅니다");
  }
}
// switch - case문은 기본적으로 소괄호 안에 있는 변수의 값과 일치하는 케이스를 위에서부터 차례로 탐색하다가
// 일치하는 case를 만나게 되면 그 아래에 있는 모든 코드를 다 수행시켜줌
// -> 일치하는 case 안에 있는 코드만 실행 시키고 싶다면 case문 끝에 break 키워드를 적어주면 break가 걸려 switch문이 종료됨
// switch문은 기본적으로 거의 모든 케이스에 break를 필수적으로 달아줘야 된다는 특징 존재
// 어떠한 case에도 해당되지 않았을 때 실행할 코드는 default: {}에 작성

// 결론
// 어떠한 변수의 값을 기준으로 각각 다른 코드를 실행시키고 싶다면 switch문
// 복잡한 여러 개의 조건을 이용하고 싶다면 if문