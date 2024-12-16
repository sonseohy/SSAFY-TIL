package modifier00_import;

// 하나씩 import 해 와도 되지만
//import java.util.Arrays;
//import java.util.Date;
//import java.util.Scanner;

// '*'을 사용해 java.util의 모든 패키지 불러올 수 있음
import java.util.*;
// 단, 하위 패키지까지 가져오지는 않는다.
// 하나씩 가져오는 것과 *로 가져오는 것의 속도 차이는 유의미한 차이는 없음

// * 그 패키지에 있는 클래스만, 하위 패키지는 x
import java.util.logging.Logger;

public class ImportTest {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		Date d;
//		Arrays
		
		Logger l; // 하위 패키지는 *로 가져올 수 없음
	}
}
