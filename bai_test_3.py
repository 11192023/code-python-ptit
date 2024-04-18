def min_steps_to_destination(N, M, matrix):
    dp = {}

    def helper(x, y):
        if x == N and y == M:
            return 0
        if x > N or y > M:
            return float('inf')
        if (x, y) in dp:
            return dp[(x, y)]

        down = helper(x + 1, y) - matrix[x][y] if x + 1 <= N else float('inf')
        right = helper(x, y + 1) - matrix[x][y] if y + 1 <= M else float('inf')
        diagonal = helper(x + 1, y + 1) - matrix[x][y] if x + 1 <= N and y + 1 <= M else float('inf')

        dp[(x, y)] = min(down, right, diagonal) + 1
        return dp[(x, y)]

    steps = helper(1, 1)
    return steps if steps != float('inf') else -1

# Hàm main để đọc dữ liệu và gọi hàm min_steps_to_destination
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        matrix = []
        for _ in range(N):
            row = list(map(int, input().split()))
            matrix.append(row)
        result = min_steps_to_destination(N, M, matrix)
        print(result)