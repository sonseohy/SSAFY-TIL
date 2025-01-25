// 자바스크립트에서만 제공되거나 독특한 기능을 하는 특수한 연산자들

// 1. null 병합 연산자 : ??
// -> 존재하는 값을 추려내는 기능
// -> null, undefined가 아닌 값을 찾아내는 연산자
// 양쪽에 피연산자(연산에 참여하는 값)들 중에 Null이나 undefined가 아닌 값들을 찾아내는 기능을 하는 연산자
// 실무에서 요긴하게 사용됨
// ex) 회원 관리 시스템을 만들 때 displayame에 유저네임이 있으면 유저 네임을 저장하고 없으면(Undefined) 유저 닉네임으로 저장해라라
// let userName = "홍길동";
// let userNickName = "Hong";
// let displayName = userName ?? userNickName;

let var1;   // var1은 초기화해주지 않았으므로 undefined 값이 존재
let var2 = 10;
let var3 = 20;

let var4 = var1 ?? var2;    // undefined가 아닌 값인 10을 var4에 저장
console.loge(var4); // 10
let var5 = var1 ?? var3;
console.log(var5);  // 20
let var6 = var3 ?? var2;
console.log(var6);  // 10 : 두 개의 피연산자가 둘 다 null이나 undefined가 아니면 맨 처음에 적힌 값이 반환됨

let userName;
let userNickName = "Winterlood";

let displayName = userName ?? userNickName;


// 2. typeof 연산자
// -> 값의 타입을 문자열로 반환하는 기능을 하는 연산자

// 자바스크립트는 변수의 타입이 고정되어 있지 않음
// (var7처럼 변수를 선언하면서 숫자 값으로 변수를 처음에 초기화했다고 하더라도 해당 변수에 다른 타입의 값을 나중에 또 저장하는게 가능함)
let var7 = 1;
var7 = "hello";
var7 = true;

// 현재 변수에 저장된 값의 타입이 궁금할 때 typeof 연산자를 이용
let t1 = typeof var7;
console.log(t1);    // boolean
var7 = 20;
console.log(t1);    // number


// 3. 삼항 연산자
// -> 항을 3개 사용하는 연산자
// -> 조건식을 이용해서 참, 거짓일 때의 값을 다르게 반환
let var8 = 10;

// 요구사항 : 변수 res에 var8의 값이 짝수 -> "짝", 홀수 -> "홀"
// (조건식) ? (조건식이 참일 때 반환값) : (거짓일 때 반환값);
let res = var8 % 2 === 0 ? "짝수" : "홀수";
console.log(res);   // 짝수
