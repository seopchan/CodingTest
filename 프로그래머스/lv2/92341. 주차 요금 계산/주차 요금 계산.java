import java.util.*;
import java.io.*;
import java.math.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        System.out.println(Arrays.toString(fees));
        System.out.println(Arrays.toString(records));
        
        HashMap<String, String> in = new HashMap<>();
        HashMap<String, Integer> result = new HashMap<>();
        
        for (String val : records) {
            String time = val.substring(0,5);
            String carNumber = val.substring(6,10);
            String inOut = val.substring(11);
            System.out.println("time: " + time + " cn: " + carNumber + " inOut : " + inOut);
            
            int h = Integer.parseInt(time.split(":")[0]);
            int m = Integer.parseInt(time.split(":")[1]);
            int totalMin = h * 60 + m;
            
            
            if ("IN".equals(inOut)) {
                in.put(carNumber, time);
            } else {
                String inTime = in.remove(carNumber);
                int inH = Integer.parseInt(inTime.split(":")[0]);
                int inM = Integer.parseInt(inTime.split(":")[1]);
                int inTotalMin = inH * 60 + inM;
                
                int parkedMin = totalMin - inTotalMin;
                result.put(carNumber, result.getOrDefault(carNumber, 0) + parkedMin);
            }
        }
        
        for (String carNumber: in.keySet()) {
            String inTime = in.get(carNumber);
            int inH = Integer.parseInt(inTime.split(":")[0]);
            int inM = Integer.parseInt(inTime.split(":")[1]);
            int inTotalMin = inH * 60 + inM;

            int parkedMin = 23 * 60 + 59 - inTotalMin;
            result.put(carNumber, result.getOrDefault(carNumber, 0) + parkedMin);
        }
        
        List<String> sortedCars = new ArrayList<>(result.keySet());
        Collections.sort(sortedCars);
        
        int[] answer = new int[sortedCars.size()];
        
        for(int i=0; i < sortedCars.size(); i++) {
            String car = sortedCars.get(i);
            int time = result.get(car);
            
            if (time <= fees[0]) {
                answer[i] = fees[1];
            } else {
                int extraTime = time - fees[0];
                answer[i] = fees[1] + (int)Math.ceil((double)extraTime / fees[2]) * fees[3];
            }
        }
        
        return answer;
    }
}