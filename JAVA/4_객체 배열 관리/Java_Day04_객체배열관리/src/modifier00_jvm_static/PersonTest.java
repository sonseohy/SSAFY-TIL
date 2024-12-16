package modifier00_jvm_static;

public class PersonTest {
	public static void main(String[] args) {
		// static 변수는 클래스 이름으로 바로 접근 가능
		System.out.println(Person.pCount);	// 100이 아닌 1000 출력 (초기화 블록으로 초기화 할 수 있는 수단을 하나 더 만들었다고 생각하면 쉬움)
		
		Person p = new Person();
		p.pCount = 200; // static 변수는 모든 인스턴스가 공유한다.
		// 참고) p.pCount는 Person 클래스의 pCount에 접근해 값을 직접 바꾼것 -> 해당 설계도를 공유하는 많은 인스턴스의 pCount 값이 바뀐 것
		System.out.println(p.pCount); // 노란줄이 뜬다.(경고)
		// 인스턴스를 통해서도 접근은 되지만, 클래스 이름으로 접근하는 것을 권장.
	}

}
