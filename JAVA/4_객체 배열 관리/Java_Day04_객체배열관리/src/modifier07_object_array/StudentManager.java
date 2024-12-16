package modifier07_object_array;

public class StudentManager {
	// Student의 배열을 가지고 있는 객체
	// -> 1개의 객체만 생성하면 됨 -> 싱글턴으로 만든다.
	
	Student[] arr = new Student[100]; // 빈 배열을 만들어 놓음, null로 초기화 되어있는 상태
	int size = 0; // 실제 들어있는 개수
	
	private static StudentManager instance = new StudentManager();
	
	private StudentManager() {}
	
	public static StudentManager getInstance() {
		return instance;
	}
	
	public void addStudent(Student st) {
		if(size < 100) {
			arr[size] = st;
			size++;
		} else {
			System.out.println("더 이상의 학생을 추가할 수 없습니다.");
		}
	}
	
    public Student getStudent(String name) {
        for(int i = 0; i < size; i++) {
            if(arr[i].getName().equals(name)) {
                return arr[i];
            }
        }
        return null;
    }
    
    public void changeMajor(String name, String newMajor) {
        Student st = getStudent(name);
        if(st != null) {
            st.setMajor(newMajor);
            System.out.println(name + "의 전공이 " + newMajor + "로 변경되었습니다.");
        } else {
            System.out.println("해당 이름의 학생을 찾을 수 없습니다.");
        }
    }

}
