import java.util.stream.*;

class Solution {
    public int solution(int n) {
        return IntStream.rangeClosed(0,n)
            .filter(e->e%2==0)
            .sum();
    }
}