
public class Array05_최대최소합평균2 {
	public static void main(String[] args) {
		int[] nums = { 64, 53, 123, 23, 444, 98, 12 };
		
		// 최대, 최소, 합, 평균
		// 최댓값 구하기
		// 1. 최댓값을 담을 임시 변수를 아주 작은 값으로 설정 | 배열의 첫번째 값을 임시 변수 값으로 설정
		// 2. 반복문을 돌면서 비교한다.
		
		// 최대
		// 1. 첫번째 값을 최대로 가정한다.
		int max = nums[0];
		// 2. 배열의 두번째 값부터 비교하면서 더 큰 값이 있다면 업데이트한다.
		for(int i = 1; i < nums.length; i++) {
			if(max < nums[i])
				max = nums[i];
		}
		System.out.println(max);
		
		// 최소
		// 1. 첫번째 값을 최소값으로 가정.
		int min = nums[0];
		// 2. 두번째 값부터 비교해 나간다.
		for(int i = 1;i < nums.length; i++) {
			if (min > nums[i])
				min = nums[i];
		}
		System.out.println(min);
		
		// 합
		int sum = 0;
		for(int i = 0;i < nums.length; i++)	// 반복문 블록이 한 문장일 경우에는 중괄호 생략 가능
			sum += nums[i];
		
		System.out.println(sum);
		
		// 평균
		double avg = (double)sum / nums.length;
		System.out.printf("%.2f\n", avg);
	}
}
