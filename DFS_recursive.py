def dfs_recursive(graph, start, visited=None):
    """
    재귀를 사용한 깊이 우선 탐색
    graph: {노드: [인접 노드 리스트]} 형태의 딕셔너리
    start: 시작 노드
    visited: 방문한 노드 집합 (재귀 호출 시 사용)
    """
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")  # 방문 출력

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited  # 선택 사항: 나중에 방문한 노드 집합 반환

def dfs_stack(graph, start):
    """
    스택을 사용한 반복문 DFS
    """
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            # 인접 노드 역순으로 스택에 추가하면 재귀와 동일한 순서
            stack.extend(reversed(graph[node]))

    return visited

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("재귀 DFS:")
    dfs_recursive(graph, 'A')

    print("\n스택 DFS:")
    dfs_stack(graph, 'A')
