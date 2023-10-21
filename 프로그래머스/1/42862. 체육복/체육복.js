function solution(n, lost, reserve) {
    let ans = n;
    lost.sort((a, b) => a - b);
    reserve.sort((a, b) => a - b);
    
    for (const l of lost) {
        for (const r of reserve) {
            if (l == r) {
                reserve.splice(reserve.indexOf(r), 1)
                lost.splice(lost.indexOf(l), 1)
            }
        }    
    }
    
    for (let i=1; i<=n; i++) {
        if (lost.find(l => l==i)) {
            if (reserve.find(r => r == i)) {
                reserve.splice(reserve.indexOf(i), 1)
            } else if (reserve.find(r => r == i - 1)) {
                reserve.splice(reserve.indexOf(i - 1), 1)
            } else if (reserve.find(r => r == i + 1)) {
                reserve.splice(reserve.indexOf(i + 1), 1)
            } else {
                ans--
            }
        }
    }
    
    return ans;
}