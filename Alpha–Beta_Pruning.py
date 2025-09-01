import math

def minimax(node, depth, alpha, beta, maximizing_player, values):
    """
    알파-베타 가지치기를 적용한 미니맥스 탐색
    node   : 현재 노드 인덱스
    depth  : 현재 깊이
    alpha  : 최대화 플레이어의 최적(최대)값
    beta   : 최소화 플레이어의 최적(최소)값
    maximizing_player : True → MAX, False → MIN
    values : 리프 노드 값 배열
    """
    # 리프 노드 도달
    if depth == 0 or node >= len(values):
        return values[node]

    if maximizing_player:
        max_eval = -math.inf
        # MAX 플레이어: 두 자식 노드 탐색 (왼쪽, 오른쪽)
        for child in [2 * node + 1, 2 * node + 2]:
            if child < len(values):  # 자식이 존재할 때만
                eval_val = minimax(child, depth - 1, alpha, beta, False, values)
                max_eval = max(max_eval, eval_val)
                alpha = max(alpha, eval_val)
                if beta <= alpha:
                    break  # β 컷
        return max_eval
    else:
        min_eval = math.inf
        # MIN 플레이어
        for child in [2 * node + 1, 2 * node + 2]:
            if child < len(values):
                eval_val = minimax(child, depth - 1, alpha, beta, True, values)
                min_eval = min(min_eval, eval_val)
                beta = min(beta, eval_val)
                if beta <= alpha:
                    break  # α 컷
        return min_eval


# 사용 예시
if __name__ == "__main__":
    # 리프 노드 값들 (게임 종료 상태 점수라고 가정)
    values = [3, 5, 6, 9, 1, 2, 0, -1]

    # 깊이는 log2(len(values)) 정도
    depth = int(math.log2(len(values)))

    best_value = minimax(0, depth, -math.inf, math.inf, True, values)
    print("최적 값:", best_value)
