package class08;

public class Dog {
	String name;
	int age;
	
	// 생성자에도 매개변수가 올 수 있다.
	// 생성자 : 멤버 필드를 초기화하는데 사용
	// 객체가 생성될 때 바로 name, age 변수가 초기화 되서(값이 들어간 채로) 메모리에 올라감
	// 프로그래머가 생성자를 하나라도 만든다면, 컴파일러는 기본 생성자를 추가하지 않는다.
	// -> 그래서 DogTest에서 Dog d2 = new Dog(); 코드가 오류가 발생함 (기본 생성자가 Dog()가 없으므로)
	// 기본 생성자는 웬만하면 만드는게 좋다 (상속)
	Dog() {
		
	}
	
	Dog(String name, int age) {
		// name = name, age = age와 같이 매개변수를 변수명과 통일시켜주는 것이 좋음
		// 그렇다면 변수와 매개변수 구분은 어떻게?
		// -> this.를 통해 구별한다.
		// this. : 내(생성된 인스턴스)가 가지고 있는
		// this는 this. 으로 멤버 변수에 접근할 때 사용 가능
		// this : 객체(인스턴스) 나 자신을 가리키는 참조값 != 설계도(클래스) 아님 -> 실제로 생성된 인스턴스
		this.name = name;
		this.age = age;
	}	// 생성자 오버로딩
	
	Dog(String name) {
//		this.name = name;
//		this.age = 5;
		// this 뒤에 괄호()가 바로 와버리면 내가 가지고 있는 다른 생성자를 호출한다는 뜻
		// 제약사항 : 반드시 생성자 본문에서 첫줄에 위치!
		this(name, 5);	// 내가 이미 가지고 있는 생성자를 호출
	}
	
	Dog(int age) {
//		this.name = "무명..";		// this() 구문은 반드시 첫 줄에 위치해야 함
		this("무명", age);
	}
	
	// 메서드 체이닝
	Dog eat() {
		System.out.println("사료를 먹고...");
		return this;	// 자기자신을 반환한다
	}
	
	void drink() {
		System.out.println("물을 마십니다.");
	}
}
