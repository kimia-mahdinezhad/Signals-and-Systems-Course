import sys


class PathFinder:
    def __init__(self, m_array, m_path, m_n, m_k):
        self.array = m_array
        self.path = m_path
        self.n = m_n
        self.k = m_k

    def check_possible_fruits(self, r, c):
        item = self.array[r][c][self.k]

        if item != -1:
            return item
        if r < self.n:
            right_down = down = left_down = -1
            r += 1

            if c + 1 < self.n:
                right_down = self.check_possible_fruits(r, c + 1)
            if self.k > 0:
                down = self.check_possible_fruits(r, c)
            if 0 < c - 1:
                left_down = self.check_possible_fruits(r, c - 1)

            chosen_path = max(right_down, down)
            chosen_path = max(chosen_path, left_down)

            self.array[r - 1][c][self.k] = chosen_path + self.path[r - 1][c]

            return self.array[r - 1][c][self.k]


temp = input().split(' ')
n = int(temp[0])
k = int(temp[1])

path = []
array = []

for i in range(n):
    row = [int(i) for i in input().strip().split(' ')]
    path.append(row)

for i in range(n):
    temp_2d = []
    for j in range(n):
        temp = []
        for t in range(k + 1):
            temp.append(-1)
        temp_2d.append(temp)
    array.append(temp_2d)

max_fruit = - sys.maxsize - 1

pf = PathFinder(array, path, n, k)

for i in range(n):
    fruit = pf.check_possible_fruits(0, i)
    max_fruit = max(fruit, max_fruit)

print(max_fruit)
