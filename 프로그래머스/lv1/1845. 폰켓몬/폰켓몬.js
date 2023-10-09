

function solution(nums) {
    n = nums.length / 2;
    
    keys = [];
    
    for(const num of nums) {
        if (!keys.find(key => key == num)) {
            keys.push(num);
            if (keys.length >= n) {
                return n;
            }
        };
    }
    return keys.length;
}