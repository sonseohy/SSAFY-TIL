
public class Array02_다양한타입의배열 {
	public static void main(String[] args) {
		int[] intArray = new int[5];
		double[] doubleArray = new double[5];
		char[] charArray = new char[5];
		boolean[] boolArray = new boolean[5];
		String[] strArray = new String[5];
		
		System.out.println(intArray[0]);	// 0
		System.out.println(doubleArray[0]);	// 0.0
		System.out.println(charArray[0]);	// 공백문자 \u0000 -> 대응되는 정수 값은 0
		System.out.println(boolArray[0]);	// false
		System.out.println(strArray[0]);	// null (참조 자료형은 null로 초기화 -> 아무것도 참조하고 있지 않은 상태)
	}
}
