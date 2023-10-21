function solution(numbers) {
    numbers.sort((a, b) => {
        return (b.toString() + a.toString()) - (a.toString() + b.toString())
    })
    
    str = numbers.toString()
    if (parseInt(str) == 0) {
        return "0"
    }
    return str.replaceAll(",", "")
}