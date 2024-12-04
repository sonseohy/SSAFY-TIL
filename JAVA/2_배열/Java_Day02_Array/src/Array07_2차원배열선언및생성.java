import java.util.Arrays;

public class Array07_2차원배열선언및생성 {
	public static void main(String[] args) {
		int[][] arr1;	// 2차원 배열 선언만 한 것
		
		int[][] arr2 = new int[3][4];	// 3행 4열인 배열
		
		// 다차원 배열을 출력할 때는
		// Arrays.deepToString()
		System.out.println(Arrays.deepToString(arr2));
		
		// 2차원 배열은 1차원 배열의 참조값을 가지고 있는 배열이므로 아래 코드 가능
		// 2차원 배열을 생성할 때는 2차원 배열의 길이만 지정하면 된다.
		// 2차원 배열 : 1차원 배열의 참조값을 요소로 갖는 배열
		int[][] arr3 = new int[3][];	// 2차원 배열은 기본값으로 null을 가짐 -> arr3은 null로 채워진 상태
		
		System.out.println(Arrays.toString(arr3));
		
		// 1차원 배열의 길이는 각각 다르게 만들 수 있음
		arr3[0] = new int[10];
		arr3[1] = new int[4];
		arr3[2] = new int[9];
		System.out.println(Arrays.deepToString(arr3));
	}
}
