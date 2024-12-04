import java.util.Arrays;

public class Array04_배열의복사 {
	public static void main(String[] args) {
		int[] nums = { 1, 4, 6, 1, 4 };
		// 반복문을 통한 복사
		// 1. 먼저 빈 배열 만들기
		int[] tmp = new int[nums.length*2];
		for (int i = 0; i < nums.length; i++) {	// 반복문을 순회하면서,
			tmp[i] = nums[i];	// 각 원소의 값 옮기기
			// 위의 경우, 주소의 복사가 아닌 값의 복사가 이루어짐 (자료형에 따라 달라짐)
			// But. 배열이 기본형의 배열이 아닌 참조형의 배열이라면 참조값의 복사가 이루어짐
			// String[] fruits = { "pig", "date", "plum" };을 복사하면 참조값 복사가 이루어짐
		}
		System.out.println(Arrays.toString(tmp));
		
		// Arrays.copyOf(원본배열, 새로운 배열의 크기)
		// 시작점 조절이 불가능하고, 끝점 조절만 가능
		int[] tmp2 = Arrays.copyOf(nums, nums.length*2);
		System.out.println(Arrays.toString(tmp2));
		
		// Arrays.copyOfRange(원본배열, 시작점, 끝 인덱스(새로운 배열의 끝 인덱스))
		// 시작점 조절이 가능
		int[] tmp3 = Arrays.copyOfRange(nums, 0, nums.length*2);
		System.out.println(Arrays.toString(tmp3));
		
		// for문 보다는 메서드를 사용하는 방법이 더 빠름 (코딩테스트에서 유의미한 차이는 없음)
		// 두 메서드간 시간 차이는 없음 (두 메서드는 시간이 같음)
		
		// System.arraycopy(원본배열, 원본배열의 시작점, 복사배열, 복사배열의 시작점, 복사할 길이(갯수))
		int[] tmp4 = new int[nums.length*2];
		System.arraycopy(nums, 0, tmp4, 0, nums.length);
		// System.arraycopy(nums, 2, tmp4, 1, nums.length-2);
		System.out.println(Arrays.toString(tmp4));
	}
}
