function solution(n, lost, reserve) {
    lost.sort((a, b) => a - b);
    reserve.sort((a, b) => a - b);
    
    let realLost = lost.filter(l => !reserve.includes(l));
    let realReserve = reserve.filter(r => !lost.includes(r));
    
    for (let i = 0; i < realLost.length; i++) {
        if (realReserve.includes(realLost[i] - 1)) {
            realReserve.splice(realReserve.indexOf(realLost[i] - 1), 1);
        } else if (realReserve.includes(realLost[i] + 1)) {
            realReserve.splice(realReserve.indexOf(realLost[i] + 1), 1);
        } else {
            n--;
        }
    }
    return n;
}
