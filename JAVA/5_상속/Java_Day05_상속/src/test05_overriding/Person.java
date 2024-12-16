package test05_overriding;

// extends 키워드를 명시하지 않으면 사실은 Object 클래스를 상속 받고 있는 것임.
public class Person {
	String name;
	int age;
	
	// 권장 : 기본 생성자는 만들어 주는 것이 좋다.
	public Person() {
		// super();가 생략되어 있다
		// -> Object 클래스의 생성자를 호출하고 있다.
	} // 기본 생성자 만들지 않으면 Student.java, Test.java에서 에러 발생
	
	// 클래스의 접근제한자(public)와 생성자의 접근제한자를 맞춰주는 것이 좋음
	// 부모 클래스에서 매개변수가 있는 생성자를 만들었더니 경고 발생
	public Person(String name, int age){
		// 말하지 않아도 super();가 생략되어 있다.
		super();	// object 생성자 호출
		this.name = name;
		this.age = age;		
	}
	
	void eat() {
		System.out.println("음식을 먹습니다.");
	}
}
