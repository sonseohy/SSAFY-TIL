package modifier04_public;

public class PersonTest {
	public static void main(String[] args) {
		Person p = new Person();
		p.age = 10;	// 같은 패키지에 있는 다른 클래스 접근 가능
	}
}
