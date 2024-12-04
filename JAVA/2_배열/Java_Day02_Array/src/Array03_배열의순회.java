import java.util.Arrays;

public class Array03_배열의순회 {
	public static void main(String[] args) {
		int[] nums = { 23, 7, 20, 11, 6 };
		
		// index를 활용할 일이 있다면
		for(int i = 0; i < nums.length; i++) {
			System.out.println(nums[i]);
			nums[i] *= 2;
		}
		
		// for-each문
		// for (type 변수명: iterate) {
		//     body-of-loop
		// }
		// iterate는 루프를 돌릴 객체이고 iterate 객체에서 한 개씩 순차적으로 변수명에 대입되어 for 문이 수행됨
		// - read only
		// - index를 활용할 일이 없다면
		for(int num : nums) {
			System.out.println(num);
		}
		
		// 간단하게 배열 출력하는 방법 (메서드 이용)
		System.out.println(Arrays.toString(nums));
	}
}
