function solution(n, times) {
    let min = 1;
    let max = Math.max(...times) * n
    
    let ans = max;
    
    while (min <= max) {
        let mid = Math.floor((min + max) / 2)
        let people = 0
        for (const time of times) {
            people += Math.floor(mid / time);
        }
        
        if (people >= n) {
            ans = Math.min(ans, mid)
            max = mid - 1
        } else {
            min = mid + 1
        }
    }
    
    return ans;
}