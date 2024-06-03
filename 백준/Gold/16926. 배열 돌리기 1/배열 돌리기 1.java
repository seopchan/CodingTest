import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    /*
    * q로 넣어서 돌리면 안되나?
    * 라인 마다 넣으면 0부터 넣지 말고 2부터 넣으면 좋을 것 같은데
    *
    * 가로 넣고 오른쪽 아래 왼쪽
    * 메소드 따로 만드는게 편해보임
    *
    * 짝수임
    *
    * 49524        1588
    *
    * */

    static int n,m,r;
    static int[][] map;
    static List<Deque<Integer>> nums = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] str = reader.readLine().split(" ");
        n = Integer.parseInt(str[0]);
        m = Integer.parseInt(str[1]);
        r = Integer.parseInt(str[2]);

        map = new int[n][m];
        for(int i=0; i<n; i++) {
            map[i] = Arrays.stream(reader.readLine().split(" "))
                    .mapToInt(Integer::parseInt).toArray();
        }

        int roundNum = Math.min(n,m) /2; // 회전 개수
        for(int i = 0 ; i < roundNum ; i++){
            nums.add(new LinkedList<>());
        }

        for(int i = 0 ; i< roundNum; i++){
            addRow(i, i, 0);
            addCol(m-1 - i, i, 0);
            addRow(n-1 - i, i, 1);
            addCol(i, i,1);
        }

        for(int i = 0 ; i< r ; i++){
            for(int j = 0 ; j < roundNum ; j++){
                int a = nums.get(j).poll();
                nums.get(j).add(a);
            }
        }


        for(int i = 0 ; i< roundNum; i++){
            saveRow(i, i, 0);
            saveCol(m-1 - i, i, 0);
            saveRow(n-1 - i, i, 1);
            saveCol(i, i,1);
        }

        for(int i = 0 ; i< n ; i++){
            for(int j = 0 ; j < m ; j++){
                System.out.print(map[i][j] + " ");
            }
            System.out.println();
        }

    }

    static void addRow(int idx, int roundIdx, int dir){
        if(dir == 0) {
            for (int j = 1 + roundIdx; j < m - 1 - roundIdx; j++) {
                nums.get(roundIdx).add(map[idx][j]);
            }
        }else if(dir == 1){
            for (int j = 1 + roundIdx; j < m - 1 - roundIdx; j++) {
                nums.get(roundIdx).add(map[idx][m-1 -j]);
            }
        }
    }
    static void addCol(int idx, int roundIdx, int dir){
        if(dir == 0) {
            for (int i = roundIdx; i < n - roundIdx; i++) {
                nums.get(roundIdx).add(map[i][idx]);
            }
        }else if(dir == 1){
            for (int  i = roundIdx; i < n - roundIdx; i++) {
                nums.get(roundIdx).add(map[n -1 -i][idx]);
            }
        }
    }

    static void saveRow(int idx, int roundIdx, int dir){
        if(dir == 0) {
            for (int j = 1 + roundIdx; j < m - 1 - roundIdx; j++) {
                int a = nums.get(roundIdx).poll();
                map[idx][j] = a;
            }
        }else if(dir == 1){
            for (int j = 1 + roundIdx; j < m - 1 - roundIdx; j++) {
                int a = nums.get(roundIdx).poll();
                map[idx][m-1 -j] = a;
            }
        }
    }
    static void saveCol(int idx, int roundIdx, int dir){
        if(dir == 0) {
            for (int i = roundIdx; i < n - roundIdx; i++) {
                int a = nums.get(roundIdx).poll();
                map[i][idx] = a;
            }
        }else if(dir == 1){
            for (int  i = roundIdx; i < n - roundIdx; i++) {
                int a = nums.get(roundIdx).poll();
                map[n -1 -i][idx] = a;
            }
        }
    }

}