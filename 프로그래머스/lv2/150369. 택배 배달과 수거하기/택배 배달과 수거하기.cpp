#include <string>
#include <vector>
#include <iostream>

using namespace std;

long long solution(int cap, int n, vector<int> deliveries, vector<int> pickups) {
    int d = 0, p = 0;
    long long ans = 0;
    
    // 1. 끝집부터 모든 배달을 끝낸다.
    // -> 2/0 -> 전 집에 2개 배달 / 4개 회수 가능 (끝집 거리 * 2)
    // -> (2/4) -> (1/0) -> 전 집에 1개 배달 / 0개 회수 가능
    // -> (1/0) -> (-2)
    // 2. 끝집의 배달 잉여분은 그 전집에서 처리 -> count X
    // 3. 왕복
    for (int i=(n-1); i >= 0; i--) {
        int cnt = 0;
        // 배달
        d -= deliveries[i];
        p -= pickups[i];
        
        // 최대치만큼 왔다갔다 해야 함
        // 여분은 이전 집에서 처리
        while (d <0 || p <0) {
            d += cap;
            p += cap;
            cnt++;            
        }
        
        // n번 집에 배달/최대치 왕복
        ans += (i + 1) * 2 * cnt;
    }
    
    return ans;
}