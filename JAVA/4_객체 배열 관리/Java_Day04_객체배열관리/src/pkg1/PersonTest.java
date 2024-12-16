package pkg1;

// pkg1.pkg2의 Person을 사용하고 싶으면 import 해서 사용
//import pkg1.pkg2.Person;

public class PersonTest {
	public static void main(String[] args) {
		
		Person p = new Person();
		System.out.println(p.pkg);
		
		// pkg1의 Person과 pkg1.pkg2의 Person 모두 사용하고 싶다면 풀 패키지명(전체 패키지 이름)을 써주면 됨
		pkg1.pkg2.Person p2 = new pkg1.pkg2.Person();
		System.out.println(p2.pkg);
	}
}