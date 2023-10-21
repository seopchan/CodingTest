function solution(citations) {
    citations.sort((a, b) => b-a)
    
    console.log(citations)
    // n h번 이상 h편
    h = citations.length + 1;
    hover = 0;
    
    while (hover < h && h != 0) {
        h--;
        hover = 0;
        for (const c of citations) {
            if (c >= h) {
                hover++
            } else {
                break;
            }
        }
    }
    
    return h
}