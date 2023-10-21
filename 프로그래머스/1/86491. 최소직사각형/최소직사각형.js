function solution(sizes) {
    let l = 0, s = 0;
    for (const size of sizes) {
        a = size[0];
        b = size[1];
        if (a > b) {
            if (a > l) {
                l = a
            }
            if (b > s) {
                s = b
            }
        } else {
            if (b > l) {
                l = b
            }
            if (a > s) {
                s = a
            }
        }   
    }
    
    return l * s;
}