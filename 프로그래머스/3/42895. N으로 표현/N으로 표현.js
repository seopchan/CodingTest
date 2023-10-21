function solution(N, number) {
    dp = Array(9).fill(0).map(() => new Set())
    
    for (let i = 1; i<= 8; i++) {
        dp[i].add(Number(String(N).repeat(i))) // N NN NNN
        for (let j = 1; j < i; j++) {
            for (const arg1 of dp[j]) {
                for (const arg2 of dp[i-j]) {
                    dp[i].add(arg1 + arg2);
                    dp[i].add(arg1 - arg2);
                    dp[i].add(arg1 * arg2);
                    if (arg2 !== 0) {
                        dp[i].add(Math.floor(arg1 / arg2));  // 나눗셈에서 나머지 무시
                    }
                }
            }
        }
        if (dp[i].has(number)) return i;
    }
    
    return -1
}