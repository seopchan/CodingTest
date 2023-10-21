function solution(n, edge) {
    // n + 1(0~n)개의 그래프를 저장
    const graph = Array.from({ length: n + 1 }, () => []);
    for (const [a, b] of edge) {
        graph[a].push(b);
        graph[b].push(a);
    }

    // 큐, 방문여부, 노드별 최대 거리
    const queue = [[1, 0]]
    const visited = Array(n + 1).fill(false)
    const distance = Array(n + 1).fill(0)
    
    while(queue.length > 0) {
        // 큐의 첫 요소 제거
        const [current_node, dist] = queue.shift()
        // 방문하지 않았으면
        if (!visited[current_node]) {
            // 방문여부, 거리 저장
            visited[current_node] = true
            distance[current_node] = dist
            // 이웃된 노드로 이동
            for(let neighbor of graph[current_node]) {
                if(!visited[neighbor]) {
                    queue.push([neighbor, dist + 1]);
                }
            }
        }
    }
    
    const max = Math.max(...distance)
    
    return distance.filter(e => e == max).length
}