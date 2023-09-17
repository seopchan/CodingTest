import java.util.*;

public class Solution {
    public static boolean isConvertible(String a, String b) {
        int diff = 0;
        for (int i = 0; i < a.length(); ++i) {
            if (a.charAt(i) != b.charAt(i)) {
                diff++;
            }
        }
        return diff == 1;
    }

    public static int solution(String begin, String target, String[] words) {
        Queue<String> queue = new LinkedList<>();
        Map<String, Integer> visited = new HashMap<>();

        queue.add(begin);
        visited.put(begin, 0);

        for (String word : words) {
            if (isConvertible(begin, word)) {
                queue.add(word);
                visited.put(word, 1);
            }
        }

        while (!queue.isEmpty()) {
            String current = queue.poll();
            int step = visited.get(current);

            if (current.equals(target)) {
                return step;
            }

            for (String word : words) {
                if (!visited.containsKey(word) && isConvertible(current, word)) {
                    queue.add(word);
                    visited.put(word, step + 1);
                }
            }
        }

        return 0;
    }
}