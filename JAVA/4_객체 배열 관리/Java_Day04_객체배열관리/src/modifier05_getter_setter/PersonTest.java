package modifier05_getter_setter;

public class PersonTest {
	public static void main(String[] args) {
		Person p = new Person();
		
		p.setAge(30);
		System.out.println(p.getAge());
		
		// p.age를 하면 사전에 막을 수 없이 age에 -10 값이 들어가는데 setAge를 하면 사전에 음수값을 막을 수 있음
//		p.age = -10;
		p.setAge(-10);
		System.out.println(p.getAge());
	}
}
