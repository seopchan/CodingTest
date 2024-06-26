function solution(arr) {
    const isSameArray = (arr1, arr2) => {
        if (arr1.length !== arr2.length) return false;
        for (let i = 0; i < arr1.length; i++) {
            if (arr1[i] !== arr2[i]) return false;
        }
        return true;
    };
    
    const transform = (arr) => {
        return arr.map(x => {
            if (x >= 50 && x % 2 === 0) {
                return x / 2;
            } else if (x < 50 && x % 2 === 1) {
                return x * 2 + 1;
            } else {
                return x;
            }
        });
    };
    
    let answer = 0;
    while (true) {
        let newArr = transform(arr);
        if (isSameArray(arr, newArr)) {
            return answer;
        }
        arr = newArr;
        answer++;
    }
}