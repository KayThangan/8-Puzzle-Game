# 8-Puzzle Game

The 8-puzzle game consists of a 3 x 3 board. There are 9 tiles in the
board are numbered from 1 to 8, and one tile is blank tile. I
created A* search algorithm to solve the 8 puzzle game using the
two heuristic functions(Euclidean and Manhattan).

To calculate the Euclidean distance is by:
sqrt((new_node.x - goal_node.x) ** 2 +
(new_node.y - goal_node.y) ** 2)

To calculate the Manhattan distance is by:
abs(new_node.x - goal_node.x) + abs(new_node.y - goal_node.y)

During the execution, user need to input the start board, goal board
and enter E for Euclidean or M for Manhattan.

In the user input of the board size, start and goal state. The user must enter
0 to represented as a blank tile. Also, when inputting the values for
the board, it will guide the user by telling what value they would like to input
for each position in the board.

### Prerequisites

What things you need to install the software and how to install
them

```
install python 3.6.0+
```

## Running the code

Running the main application
```
python eight_puzzle_game.py
```

## Built With
* Python

## License

This project is licensed under the MIT License - see the
[LICENSE.md](LICENSE.md) file for details
