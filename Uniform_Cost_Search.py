import heapq


def uniform_cost_search(graph, start, goal):
    """
    균일 비용 탐색 (Uniform Cost Search)

    graph: {노드: [(이웃노드, 비용), ...]} 형태
    start: 시작 노드
    goal: 목표 노드
    """
    # 우선순위 큐: (누적 비용, 현재 노드, 경로)
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)  # 누적 비용이 가장 작은 노드 선택

        if node == goal:
            return path, cost  # 목표에 도달하면 경로와 비용 반환

        if node in visited:
            continue
        visited.add(node)

        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + edge_cost, neighbor, path + [neighbor]))

    return None, float('inf')  # 목표에 도달할 수 없는 경우

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('D', 2), ('E', 5)],
        'C': [('A', 4), ('F', 1)],
        'D': [('B', 2)],
        'E': [('B', 5), ('F', 3)],
        'F': [('C', 1), ('E', 3)]
    }

    start = 'A'
    goal = 'F'

    path, cost = uniform_cost_search(graph, start, goal)
    print(f"최단 경로: {path}, 총 비용: {cost}")
