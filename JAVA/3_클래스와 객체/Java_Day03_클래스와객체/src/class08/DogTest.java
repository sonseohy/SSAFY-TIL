package class08;

public class DogTest {
	public static void main(String[] args) {
		Dog d = new Dog("메리", 4);
		System.out.println(d.name);
		System.out.println(d.age);
		
		Dog d2 = new Dog(); // 오류가 발생하는 이유? 컴파일러가 기본 생성자를 안 만들어줘서
	
		// 메서드 체이닝 사용
		d2.eat().drink(); // 연결해서 쓸 수 있다는 것
	}
}
