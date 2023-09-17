import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> list = new ArrayList<>();
        
        int tmp = arr[0];
        list.add(arr[0]);
        
        for (int i = 0; i < arr.length; i++) {
            if (tmp != arr[i]) {
                list.add(arr[i]);
                tmp = arr[i];    
            }
        }
        
        int[] answer = list.stream().mapToInt(Integer::intValue).toArray();

        return answer;
    }
}