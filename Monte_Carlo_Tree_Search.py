import math
import random

class Node:
    def __init__(self, state, parent=None):
        self.state = state          # 게임 상태 (보드 등)
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0

    def is_fully_expanded(self):
        return len(self.children) == len(self.state.get_legal_moves())

    def best_child(self, c_param=1.4):
        """UCB1 기반으로 최적 자식 선택"""
        choices = []
        for child in self.children:
            if child.visits == 0:
                score = float("inf")
            else:
                score = (child.wins / child.visits) + c_param * math.sqrt(
                    math.log(self.visits) / child.visits
                )
            choices.append((score, child))
        return max(choices, key=lambda x: x[0])[1]


class TicTacToe:
    def __init__(self, board=None, player=1):
        self.board = board or [0] * 9  # 0=빈칸, 1=X, -1=O
        self.player = player

    def get_legal_moves(self):
        return [i for i in range(9) if self.board[i] == 0]

    def move(self, index):
        new_board = self.board[:]
        new_board[index] = self.player
        return TicTacToe(new_board, -self.player)

    def is_terminal(self):
        # 승리 조건
        wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for a,b,c in wins:
            s = self.board[a] + self.board[b] + self.board[c]
            if s == 3: return True, 1   # X 승리
            if s == -3: return True, -1 # O 승리
        if 0 not in self.board:
            return True, 0  # 무승부
        return False, None


def mcts(root, iter_max=1000):
    for _ in range(iter_max):
        node = root

        # 1. Selection
        while node.children and node.is_fully_expanded():
            node = node.best_child()

        # 2. Expansion
        if not node.state.is_terminal()[0]:
            untried_moves = [m for m in node.state.get_legal_moves()
                             if all(c.state.board != node.state.move(m).board for c in node.children)]
            if untried_moves:
                m = random.choice(untried_moves)
                child = Node(node.state.move(m), parent=node)
                node.children.append(child)
                node = child

        # 3. Simulation
        sim_state = node.state
        while not sim_state.is_terminal()[0]:
            m = random.choice(sim_state.get_legal_moves())
            sim_state = sim_state.move(m)
        terminal, winner = sim_state.is_terminal()

        # 4. Backpropagation
        while node:
            node.visits += 1
            if winner == 1:   # X 승리
                if node.state.player == -1:  # 직전에 X가 둠
                    node.wins += 1
            elif winner == -1: # O 승리
                if node.state.player == 1:  # 직전에 O가 둠
                    node.wins += 1
            node = node.parent

    return root.best_child(c_param=0)  # 탐색 후 가장 좋은 자식 반환


# 사용 예시
if __name__ == "__main__":
    state = TicTacToe()
    root = Node(state)

    # X의 최적 수 찾기
    best = mcts(root, iter_max=500)
    print("추천 수 (보드 인덱스):", [i for i in range(9) if best.state.board[i] != state.board[i]][0])
