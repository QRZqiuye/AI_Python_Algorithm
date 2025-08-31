import math
import random


def simulated_annealing(initial_state, neighbors_fn, energy_fn,
                        temp=1000.0, cooling_rate=0.99, min_temp=1e-3):
    """
    모의 담금질 (Simulated Annealing)

    initial_state: 시작 상태
    neighbors_fn: 현재 상태에서 가능한 이웃 상태들을 반환하는 함수
    energy_fn: 상태의 에너지(낮을수록 좋은 상태)를 반환
    temp: 초기 온도
    cooling_rate: 온도 감소율 (0~1)
    min_temp: 최소 온도 (이하면 종료)
    """
    current = initial_state
    current_energy = energy_fn(current)

    while temp > min_temp:
        neighbor = random.choice(neighbors_fn(current))
        neighbor_energy = energy_fn(neighbor)

        # 에너지가 낮으면 무조건 채택, 높으면 확률적으로 채택
        delta_energy = neighbor_energy - current_energy
        if delta_energy < 0 or random.random() < math.exp(-delta_energy / temp):
            current, current_energy = neighbor, neighbor_energy

        temp *= cooling_rate  # 온도 감소

    return current, current_energy

# 상태의 에너지 함수 (낮을수록 좋음)
def energy_fn(x):
    return (x - 3)**2

# 현재 상태에서 이동 가능한 이웃 상태
def neighbors_fn(x):
    step = 0.5
    return [x - step, x + step]

if __name__ == "__main__":
    start = random.uniform(-10, 10)
    solution, value = simulated_annealing(start, neighbors_fn, energy_fn,
                                          temp=1000, cooling_rate=0.95)
    print(f"최적해: x = {solution:.3f}, f(x) = {value:.3f}")
