import pytest
from maze import Maze


@pytest.fixture
def maze():
    # Return a maze instance
    return Maze()


def test_maze(maze):
        assert maze.cells[0][0] == 's'


def test_change_cell(maze):
    maze.change_cell((0, 0), 'x')
    assert maze.cells[0][0] == 'x'


def test_write(maze):
    maze.write()
    with open('level_', "r") as f:
        level_list = []
        for line in f:
            line_list = []
            for char in line:
                if char != '\n':
                    line_list.append(char)
            level_list.append(line_list)
    assert level_list == maze.cells
