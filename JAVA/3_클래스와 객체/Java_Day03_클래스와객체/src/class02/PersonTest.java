package class02;

public class PersonTest {
	public static void main(String[] args) {
		
		// 클래스를 가지고 객체를 생성
		// - 객체도 참조형 변수 -> 주소를 저장
		// 클래스이름 객체의변수이름 = new 클래스이름();
		Person yang = new Person();
		
		// . (이 객체가 가지고 있는)
		yang.name = "Yang";
		yang.age = 45;
		yang.hobby = "YouTube";
		
		Person hong = new Person();
		hong.name = "Hong";
		hong.age = 25;
		hong.hobby = "Golf";
	}
}
