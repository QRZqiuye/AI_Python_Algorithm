import heapq


def best_first_search(graph, start, goal, heuristic_fn):
    """
    최적 우선 탐색 (Best-First Search)

    graph: {노드: [인접 노드]} 형태
    start: 시작 노드
    goal: 목표 노드
    heuristic_fn: 노드의 휴리스틱 값 (목표까지 추정 비용)
    """
    # 우선순위 큐: (휴리스틱 값, 현재 노드, 경로)
    queue = [(heuristic_fn(start), start, [start])]
    visited = set()

    while queue:
        _, node, path = heapq.heappop(queue)

        if node == goal:
            return path

        if node in visited:
            continue
        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (heuristic_fn(neighbor), neighbor, path + [neighbor]))

    return None  # 목표에 도달 불가

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    # 목표까지의 추정 거리(휴리스틱)
    heuristic = {
        'A': 5,
        'B': 4,
        'C': 2,
        'D': 3,
        'E': 2,
        'F': 0
    }

    def h(node):
        return heuristic[node]

    path = best_first_search(graph, 'A', 'F', h)
    print("최적 우선 탐색 경로:", path)
