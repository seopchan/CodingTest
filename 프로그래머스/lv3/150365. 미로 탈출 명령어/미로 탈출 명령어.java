import static java.lang.Math.abs;
import static java.lang.Math.max;

class Solution {
    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        int distance = abs(r - x) + abs(c - y);
        
        if (distance > k) {
            return "impossible";
        }
        
        if ((k - distance) % 2 == 1) {
            return "impossible";
        }
        
        String result = "";
        
        // dlru
        int down = max(r - x, 0);
        int left = max(y - c, 0); 
        int right = max(c - y, 0);
        int up = max(x - r, 0);
        int pair = (k - distance) / 2;
        
        String answer = "";
        
        //k만큼 이동
        for (int i = 0; i < k; i++) {
            if ((down > 0 || pair > 0) && x < n) {
                answer += "d";
                if (down > 0) {
                    down -= 1;
                } else {
                    pair -= 1;
                    up += 1;
                }
                x += 1;
                continue;
            }
            
            if ((left > 0 || pair > 0) && 1 < y) {
                answer += "l";
                if (left > 0) {
                    left -= 1;
                } else {
                    pair -= 1;
                    right += 1;
                }
                y -= 1;
                continue;
            }
            
            if ((right > 0 || pair > 0) && y < m) {
                answer += "r";
                if (right > 0) {
                    right -= 1;
                } else {
                    pair -= 1;
                    left += 1;
                }
                y += 1;
                continue;
            }
            
            if ((up > 0 || pair > 0) && 1 < x) {
                answer += "u";
                if (up > 0) {
                    up -= 1;
                } else {
                    pair -= 1;
                    down += 1;
                }
                x -= 1;
                continue;
            }
        }
        
        return answer;
    }
}