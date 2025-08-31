def hill_climbing(initial_state, neighbors_fn, heuristic_fn):
    """
    단순 언덕 오르기(Hill Climbing)

    initial_state: 시작 상태
    neighbors_fn: 현재 상태에서 가능한 이웃 상태들을 반환하는 함수
    heuristic_fn: 상태의 평가 점수(높을수록 좋음)를 반환하는 함수
    """
    current = initial_state
    current_value = heuristic_fn(current)

    while True:
        neighbors = neighbors_fn(current)
        if not neighbors:
            break  # 더 이상 이동할 곳이 없으면 종료

        # 이웃 중 평가값이 가장 높은 상태 선택
        next_state = max(neighbors, key=heuristic_fn)
        next_value = heuristic_fn(next_state)

        if next_value <= current_value:
            break  # 더 나은 상태가 없으면 종료

        current, current_value = next_state, next_value

    return current, current_value

import random

# 상태의 평가 함수
def heuristic_fn(x):
    return -(x-3)**2 + 10

# 현재 상태에서 이동 가능한 이웃 상태
def neighbors_fn(x):
    step = 0.1  # 한 번에 이동할 거리
    return [x - step, x + step]

if __name__ == "__main__":
    start = random.uniform(-10, 10)  # 임의 시작점
    solution, value = hill_climbing(start, neighbors_fn, heuristic_fn)
    print(f"최적해: x = {solution:.3f}, f(x) = {value:.3f}")
