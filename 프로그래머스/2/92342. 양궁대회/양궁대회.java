import java.util.*;

class Solution {
    static int[] res = {-1};
    static int[] lion;
    static int max = Integer.MIN_VALUE;

    public void dfs(int[] apeach, int shootCount, int n) {
        if (shootCount == n+1) {
            int apeachScore = 0;
            int lionScore = 0;
            
            for (int scoreIdx = 0; scoreIdx <= 10; scoreIdx++) {
                if (apeach[scoreIdx] != 0 || lion[scoreIdx] != 0) {
                    if(apeach[scoreIdx] < lion[scoreIdx])
                        lionScore += 10 - scoreIdx;
                    else
                        apeachScore += 10 - scoreIdx;
                }
            }
            
            if (lionScore > apeachScore) {
                if (lionScore - apeachScore >= max) {
                    res = lion.clone();
                    max = lionScore - apeachScore;
                }
            }
            
            return;
        }
        
        for (int scoreIdx = 0; scoreIdx <= 10 && lion[scoreIdx] <= apeach[scoreIdx]; scoreIdx++) {
            lion[scoreIdx]++;
            dfs(apeach, shootCount + 1, n);
            lion[scoreIdx]--;
        }
    }
    
    public int[] solution(int n, int[] info) {
        lion = new int[11];
        dfs(info, 1, n);
        return res;
    }
}