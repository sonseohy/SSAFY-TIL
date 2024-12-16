package modifier01_private;

public class Person {
	
	// private : 자기 자신만 접근 가능하다.
	// - 이 클래스 안에서는 접근 가능
	private String name;
	private int age;
	
	// 멤버 메서드 : 자기 자신..
	// - 멤버 메서드는 자기 자신이므로 private 접근이 가능함
	public void info() {
		name = "kim"; // 자기 자신의 것 
		System.out.printf("이름: %s, 나이: %d\n", name, age);
	}
}
