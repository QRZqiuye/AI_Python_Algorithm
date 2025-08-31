import heapq


def a_star_search(graph, start, goal, heuristic_fn):
    """
    A* 알고리즘

    graph: {노드: [(이웃노드, 비용), ...]} 형태
    start: 시작 노드
    goal: 목표 노드
    heuristic_fn: 노드의 휴리스틱 값 함수
    """
    # 우선순위 큐: (f = g+h, g, 현재 노드, 경로)
    queue = [(heuristic_fn(start), 0, start, [start])]
    visited = set()

    while queue:
        f, g, node, path = heapq.heappop(queue)

        if node == goal:
            return path, g  # 경로와 총 비용 반환

        if node in visited:
            continue
        visited.add(node)

        for neighbor, cost in graph.get(node, []):
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristic_fn(neighbor)
                heapq.heappush(queue, (f_new, g_new, neighbor, path + [neighbor]))

    return None, float('inf')  # 목표에 도달할 수 없는 경우

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 2), ('E', 5)],
        'C': [('F', 1)],
        'D': [],
        'E': [('F', 3)],
        'F': []
    }

    # 목표까지 추정 거리 (휴리스틱)
    heuristic = {
        'A': 6,
        'B': 4,
        'C': 2,
        'D': 4,
        'E': 2,
        'F': 0
    }

    def h(node):
        return heuristic[node]

    path, cost = a_star_search(graph, 'A', 'F', h)
    print("A* 최적 경로:", path)
    print("총 비용:", cost)
