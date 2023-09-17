import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        Arrays.sort(jobs, (a,b) -> a[0] - b[0]);
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        
        int time = 0;
        int sum = 0;
        int index = 0;
        
        while(index < jobs.length || !pq.isEmpty()) {
            while (index < jobs.length && jobs[index][0] <= time) {
                pq.add(jobs[index++]);
            }
            
            if (!pq.isEmpty()) {
                int[] job = pq.poll();
                sum += (time + job[1] - job[0]);
                time += job[1];
            } else {
                time = jobs[index][0];
            }
        }
        
        return sum / jobs.length;
    }
}