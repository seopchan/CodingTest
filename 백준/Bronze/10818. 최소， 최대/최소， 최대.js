let array = require("fs").readFileSync("/dev/stdin").toString().split("\n")[1].split(" ");
let max = Number(array[0]);
let min = max;
for(let val of array) {
    val = Number(val);
    if(val>max) max = val;
    if(val<min) min =val;
}
console.log(min, max);