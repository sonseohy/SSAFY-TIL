package modifier04_public2;

import modifier04_public.Person;

public class PersonTest {
	public static void main(String[] args) {
		Person p = new Person();
		// public은 모든 위치에서 접근 가능함
		p.age = 20;	// 다른 패키지에 있어도 무리없이 접근 가능
	}
}
