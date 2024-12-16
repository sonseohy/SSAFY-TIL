package test05_overriding;

// 상속을 할 때는 extends 키워드를 사용
public class Student extends Person {
	String major;
	
	// 아무런 생성자도 정의하지 않은 상태
	// = 컴파일러가 기본 생성자 Student(){}를 만듦
	// -> 생성자는 내부에 기본적으로 super();가 생략되어 있음
	// -> 기본적으로 부모 클래스의 기본 생성자를 호출한다는 뜻
	// -> 에러 발생
	
	// 빈 공간에서 ctrl + spacebar
	public Student() {
		// super(); // 생성자 내부에는 기본적으로 super();가 생략되어 있다.
		// 내부적으로 Person()을 호출하고 있다.
		// 1. 프로그래머가 명시적으로 super()를 호출하지 않아도 기본적으로 super();를 호출
		// 2. 프로그래머가 명시적으로 super()를 호출하면?
		// -> super()를 넣어주지 않는다.
	}

	
	
	void study() {
		super.eat();
		System.out.println("공부를 합니다.");
	}
	
	// 오버로딩
	// - 매개변수만 다르고 이름이 같은 메서드를 여러개 정의할 수 있다.
	// 
	
	// 오버로딩과 오버 라이딩의 가장 큰 차이점
	// - 상속 관계 유무
	// - 오버로딩은 하나의 클래스에서 하고, 오버 라이딩은 상속 받은 클래스에서 진행
	// - 오버로딩은 이름과 매개변수가 동일해야 하지만, 오버라이딩은 반환형까지 동일해야함
	
	
	// 부모에 eat()이라는 메서드가 있지만, 그대로 쓰고 싶지 않고 조금 바꾸고 싶다.
	// 자식 클래스에서 메서드를 재정의할 수 있다.
	// 오버라이딩 (재정의)
	// - 반드시 상속 관계에 있을 때
	// - 부모 클래스에 정의되어 있는 메서드를 자식 클래스에서 재정의한다.
	// - 메서드의 이름, 반환형, 매개변수가 동일해야 한다.
	// - @Override라는 어노테이션으로 좀 더 명확하게 나타낼 수 있다.
	@Override	// 태그와 같은 기능 <- 컴파일러한테 오버라이드 한 것이라고 알려주는 역할 (작성해주는 것이 좋음)
	void eat() {
		System.out.println("지식을 먹는다.");
	}
	
	// 오버로딩 : 오버로딩이므로 @Override 붙이면 에러 발생
	@Override
	void eat(int a) {
		System.out.println(a+"만큼 먹는다.");
	}
	// 컴파일 에러 분석
	// 오버라이드라고 어노테이션 했는데 부모클래스에 올라가보니 그런 메서드가 없다.
	// 오버라이드가 아니라고 에러로 알려줌

	public Student(String major) {
		super();	// 자동으로 생략되어 있는 super()를 넣어준다.
		this.major = major;
	}
	
	public Student(String name, int age, String major) {
		super(name, age);	// 부모의 생성자를 이용해 초기화
		this.major = major;
	}
}
