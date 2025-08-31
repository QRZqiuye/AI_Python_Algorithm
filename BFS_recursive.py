from collections import deque

def bfs(graph, start):
    """
    너비 우선 탐색
    graph: {노드: [인접 노드 리스트]} 형태의 딕셔너리
    start: 시작 노드
    """
    visited = set()         # 방문한 노드 집합
    queue = deque([start])  # 큐에 시작 노드 추가

    while queue:
        node = queue.popleft()  # 큐에서 가장 앞 노드 꺼내기
        if node not in visited:
            visited.add(node)
            print(node, end=" ")  # 방문 출력
            # 아직 방문하지 않은 인접 노드들 큐에 추가
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited  # 선택 사항: 방문한 노드 집합 반환

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("BFS 탐색 결과:")
    bfs(graph, 'A')
