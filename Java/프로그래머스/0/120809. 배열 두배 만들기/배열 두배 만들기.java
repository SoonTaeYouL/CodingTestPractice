import java.util.Arrays;
class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = Arrays.stream(numbers)
            .map(e-> e*2)
            .toArray(); // 다시 배열로 변환
        
        return answer;
    }
}