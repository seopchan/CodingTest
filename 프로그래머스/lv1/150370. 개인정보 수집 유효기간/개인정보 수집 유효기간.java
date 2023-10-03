import java.util.*;

class Solution {
    private final HashMap<String, Integer> termsMap = new HashMap<>();

    public boolean isExpired(String type, int y, int m, int d, int curY, int curM, int curD) {
        int term = termsMap.get(type);
        
        int newYear = y + (m + term) / 12;
        int newMonth = (m + term) % 12;
        int newDay = d - 1;
        
        if (newMonth == 0) {
            newMonth = 12;
            newYear--;
        }

        if (newDay == 0) {
            newDay = 28;
            newMonth--;

            if (newMonth == 0) {
                newMonth = 12;
                newYear--;
            }
        }
        
        System.out.println(newYear + " " + newMonth + " " + newDay);

        return newYear < curY || (newYear == curY && (newMonth < curM || (newMonth == curM && newDay < curD)));
    }

    public int[] solution(String today, String[] terms, String[] privacies) {
        String[] todayArr = today.split("\\.");
        int curYear = Integer.parseInt(todayArr[0]);
        int curMonth = Integer.parseInt(todayArr[1]);
        int curDay = Integer.parseInt(todayArr[2]);
        
        System.out.println(today);

        for (String term : terms) {
            String[] parts = term.split(" ");
            termsMap.put(parts[0], Integer.parseInt(parts[1]));
        }

        List<Integer> expiredIndices = new ArrayList<>();

        for (int i = 0; i < privacies.length; i++) {
            String[] parts = privacies[i].split(" ");
            String date = parts[0];
            String type = parts[1];

            String[] dateArr = date.split("\\.");
            int year = Integer.parseInt(dateArr[0]);
            int month = Integer.parseInt(dateArr[1]);
            int day = Integer.parseInt(dateArr[2]);

            if (isExpired(type, year, month, day, curYear, curMonth, curDay)) {
                expiredIndices.add(i + 1);
            }
        }

        return expiredIndices.stream().mapToInt(Integer::intValue).toArray();
    }
}