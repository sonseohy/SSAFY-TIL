package test01_class_diagram;

// 사실은 하나의 파일에 여러 개의 class를 만들 수는 있다.
// public은 하나여야 하고 public 클래스의 이름과 파일 이름이 일치해야함

class B {
	
}

class C {
	A a;
}

class D {
	
}

class E {
	
}

class F {
	void method() {
		System.out.println("f");
	}
}

public class A {
	B b;	// 멤버변수 선언, 멤버 변수로 가지고 있음 : A는 B와 연관된다.
	C c;	// 양방향 연관 : A와 C는 서로를 가지고 있다. 서로 연관된다.
	D[] d; 	// A가 D를 가지고 있는데 여러 개를 가지고 있을 수도 있음, 집합 or 구성
	D[] d2;	// 집합 : A는 D의 집합을 가지고 있다. A는 D 없이도 존재 가능하다.
	E[] e;	// 구성 : A는 E로 구성된다. A는 E가 없으면 존재 불가능하다.
	
	void method() {
		// A 클래스가 F를 가지고 있는 것은 아님.
		F f = new F();	// A는 F에 의존한다.
		f.method();
	}
}
