function solution(n, results) {
    let win = {}, lose = {};
    for(let i=1; i<=n; i++) {
        win[i] = new Set();
        lose[i] = new Set();
    }
    
    for(let [winner, loser] of results) {
        win[winner].add(loser);
        lose[loser].add(winner);
    }

    for(let i=1; i<=n; i++) {
        // i가 이긴 사람 -> win[i] -> loser
        for(let loser of win[i]) {
            // loser는 i의 진 사람(lose)한테 짐 -> lose[loser] add lose[i]
            lose[i].forEach(item => {
                lose[loser].add(item);
            });
        }
        for(let winner of lose[i]) {
            win[i].forEach(item => {
                win[winner].add(item);
            });
        }
    }

    let count = 0;
    for(let i=1; i<=n; i++) {
        if(win[i].size + lose[i].size === n-1) count++;
    }
    return count;
}