package modifier06_singleton;

// 점수를 관리하는 객체
// 점수는 1개만 존재함
// -> 객체도 1개만 만든다.
public class ScoreManager {
	private int score;
	
	// 2. 인스턴스는 1개만 만들어서 가지고 있자.
	private static ScoreManager manager = new ScoreManager();
	
	// 싱글턴으로 만들어보자.
	// 1. 오로지 1개만 생성되도록 -> 외부에서 생성자를 호출할 수 없도록 막아야 함
	// - 생성자를 private로 만든다.
	private ScoreManager() {}
	
	// 3. 인스턴스를 외부에서 가져다 쓸 수 있도록 public으로 getter를 추가
	// - getter는 반환형이 필요한데 나 자신을 반환할 것이므로 public 다음에 ScoreManager 작성
	// 4. 객체 생성 없이 클래스 이름으로 바로 접근할 수 있도록 static을 추가
	public static ScoreManager getInstance() {
		return manager;
	}
}
