import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        
        Integer[] integerTruckWeights = Arrays.stream(truck_weights).boxed().toArray(Integer[]::new);
        Queue<Integer> wait = new LinkedList<>(Arrays.asList(integerTruckWeights));
        Queue<int[]> onBridge = new LinkedList<>();
        
        int total_weight = 0;
        
        int time = 0;
        
        while (!wait.isEmpty() || !onBridge.isEmpty()) {
            time++;
            
            if (!onBridge.isEmpty()) {
                int[] front = onBridge.peek();
                if (time - front[1] == bridge_length) {
                    total_weight -= front[0];
                    onBridge.poll();
                }
            }
            
            if (!wait.isEmpty()) {
                int next_truck = wait.peek();
                if (total_weight + next_truck <= weight) {
                    wait.poll();
                    onBridge.add(new int[]{next_truck, time});
                    total_weight += next_truck;
                }
            }
        }
        
        return time;
    }
}