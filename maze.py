import random


class Maze:
    # width and height are in cells while cell_size is in pixel.
    def __init__(self):
        self.cells = []
        self.nb_line = 15
        self.nb_col = 15
        self.wall = '1'
        self.maze = '0'
        self.visited = '0'

        for line in range(0, self.nb_line):
            line_tab = []
            for col in range(0, self.nb_col):
                line_tab.append(self.wall)
            self.cells.append(line_tab)

        self.depth_first_search()
        self.write()

    def change_cell(self, cell, value):
        x = cell[0]
        y = cell[1]
        self.cells[y][x] = value

    def print_maze(self):
        for line_ in self.cells:
            print(line_)

    def write(self):
        with open('level_', "w") as f:
            for line in self.cells:
                if self.cells.index(line) == 0:
                    line[0] = "s"
                    for col in line:
                        f.write(str(col))
                    f.write("\n")
                elif self.cells.index(line) == self.nb_line - 2:
                    line[self.nb_col - 2] = "0"
                    for col in line:
                        f.write(str(col))
                    f.write("\n")
                elif self.cells.index(line) == self.nb_line - 1:
                    line[self.nb_col - 1] = "f"
                    for col in line:
                        f.write(str(col))
                else:
                    for col in line:
                        f.write(str(col))
                    f.write("\n")

    def unvisited_cell_neighbors(self, cell):
        x = cell[0]
        y = cell[1]
        neighbors = []
        left = []
        up = []
        right = []
        down = []

        if x > 1 and self.cells[y][x-2] == self.wall:
            left.extend([(x-1, y), (x-2, y)])
        if y > 1 and self.cells[y-2][x] == self.wall:
            up.extend([(x, y-1), (x, y-2)])
        if x < self.nb_col-2 and self.cells[y][x+2] == self.wall:
            right.extend([(x+1, y), (x+2, y)])
        if y < self.nb_line - 2 and self.cells[y+2][x] == self.wall:
            down.extend([(x, y+1), (x, y+2)])

        neighbors.extend([left, up, right, down])
        neighbors = [x for x in neighbors if x != []]
        return neighbors

    def depth_first_search(self):
        visited = []
        current_cell = (0, 0)
        visited.append(current_cell)
        # commented to keep S in first
        # self.change_cell(current_cell, self.maze)

        while visited:

            neighbors = self.unvisited_cell_neighbors(current_cell)
            if neighbors:
                next_cell = random.choice(neighbors)
                self.change_cell(next_cell[0], self.maze)
                self.change_cell(next_cell[1], self.maze)
                visited.extend([next_cell[0], next_cell[1]])
                current_cell = next_cell[1]
            else:
                if len(visited) > 1:
                    self.change_cell(visited[-1], self.visited)
                    del visited[-1]
                    self.change_cell(visited[-1], self.visited)
                    del visited[-1]
                    current_cell = visited[-1]
                else:
                    self.change_cell(visited[-1], self.visited)
                    current_cell = visited[-1]
                    del visited[-1]
