function solution(array, commands) {
    var answer = [];
    for (const command of commands) {
        const na = array.slice(command[0] - 1, command[1]).sort((a, b) => a - b)
        answer.push(na[command[2] - 1])
    }
    return answer;
}