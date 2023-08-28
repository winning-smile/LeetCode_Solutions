class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l_moves = 0
        r_moves = 0
        free_moves = 0
        for move in moves:
            if move == "L":
                l_moves += 1
            elif move == "R":
                r_moves += 1
            else:
                free_moves += 1

        if l_moves > r_moves:
            return l_moves - r_moves + free_moves

        elif l_moves < r_moves:
            return r_moves - l_moves + free_moves

        else:
            return free_moves
