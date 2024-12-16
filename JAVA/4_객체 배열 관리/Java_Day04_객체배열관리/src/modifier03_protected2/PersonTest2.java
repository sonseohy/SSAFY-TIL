package modifier03_protected2;

import modifier03_protected.Person;

// 다른 패키지에 있는 다른 클래스
// 상속을 받은 것은 : PersonTest2 가 상속을 받은 것
public class PersonTest2 extends Person{
	public static void main(String[] args) {
		Person p = new Person();
		// 다른 클래스에 있으면 기본적으로는 안됨
		
		// 상속을 받은 다음 그 상속을 받은 클래스를 통해서만 접근 가능
		// 즉 Person을 상속받은 PersonTest2에서는 접근 가능하다는 뜻
		PersonTest2 p2 = new PersonTest2();
		p2.age = 10;
	}
}
