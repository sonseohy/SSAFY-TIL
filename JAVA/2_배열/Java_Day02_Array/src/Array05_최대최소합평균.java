
public class Array05_최대최소합평균 {
	public static void main(String[] args) {
		int[] nums = { 64, 53, 123, 23, 444, 98, 12 };
		
		// 최대, 최소, 합, 평균
		// 최댓값 구하기
		// 1. 최댓값을 담을 임시 변수를 아주 작은 값으로 설정 | 배열의 첫번째 값을 임시 변수 값으로 설정
		// 2. 반복문을 돌면서 비교한다.
		
		// 최대, 최소, 합, 평균을 하나의 코드로 합치기
		int max = nums[0];
		int min = nums[0];
		int sum = nums[0];
		
		for(int i = 1; i < nums.length; i++) {
			if(max < nums[i])
				max = nums[i];
			if (min > nums[i])
				min = nums[i];
			sum += nums[i];
		}
		
		System.out.println(max);
		System.out.println(min);
		System.out.println(sum);
		
		// 평균
		double avg = (double)sum / nums.length;
		System.out.printf("%.2f\n", avg);
	}
}
