package class06;

public class PersonTest {
	public static void main(String[] args) {
		// 메서드의 호출: 1. 객체를 생성, 2. '.'연산자 사용
		Person p = new Person();
		
		// 묵시적 형변환 가능
		p.study((byte)2);
		p.study((short)10);
		p.study('A');	// 정수로 형변환이 됨
		p.study(10);
		
		// 아래 코드는 오류 발생 (아래 형이 다른 경우) -> 메서드 오버로딩 방법으로 해결 가능
		// 묵시적 형변환으로 안된다면?
		// -> 메서드 오버로딩으로 처리할 수 있다.
		p.study(10L);
		p.study(10.3f);	// float 값
		p.study(10.5);	// double 값
		p.study("10");	// 문자열 값
		
	}
	
}
