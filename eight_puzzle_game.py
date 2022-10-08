"""
This module is a program that simulates the solution to the solve the
8 puzzle game using A* algorithm.
"""
import copy
import math
import time

# start state of the puzzle.
start_board = []
# expected end state of the puzzle.
GOAL_BOARD = []
# size of the puzzle.
BOARD_SIZE = 3


class Node:
    """
    The Node class has the attribute value, x-position, y-position and
    position. This Node represents a cell in the 8 puzzle game.
    """

    def __init__(self, value, x, y, position):
        """
        This constructor assigns the values from the parameters to the
        class attributes.

        :param value:           number representation of the Node object
        :param x:               x position of the Node object
        :param y:               y position of the Node object
        :param position:        position of the Node object
        """
        self.value = value
        self.x = x
        self.y = y
        self.position = position

    def __eq__(self, other):
        """
        This method checks the object values are the same.

        :param other:           Node object
        :return:                boolean
        """
        return self.value == other.value

    def __str__(self):
        """
        This method assigns the Node object value as a string object.

        :return:                string object
        """
        return str(self.value)

    def __hash__(self):
        """
        Method to get the hash value of the Node.

        :return:                integer
        """
        # generating a unique hash value for the current node.
        return int(
            hash((self.value, self.x, self.y, self.position))
            / (hash(self.position) + 1)
        )


def display_board(board):
    """
    This method prints the board in the command line.

    :param board:               array of Node objects
    :return:                    void
    """
    temp_board = ""
    for index in range(len(board)):
        # to display as a matrix of BOARD_SIZE x BOARD_SIZE.
        if (index + 1) % BOARD_SIZE == 0:
            temp_board = temp_board + " " + str(board[index].value)
            print(temp_board)
            temp_board = ""
        else:
            temp_board = temp_board + " " + str(board[index].value)


def load_data(board):
    """
    Method to a board of Node objects.

    :param board:               2D array
    :return:                    array of Node objects
    """
    temp_board = []
    position = 0
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            # creating Node objects
            temp_board.append(Node(board[y][x], x, y, position))
            position += 1
    return temp_board


def get_empty_tile(board):
    """
    This gets the Node object in of the array of Node object that in
    empty.

    :param board:               array of Node objects
    :return:                    Node objects
    """
    for index in range(len(board)):
        # checks if the tile is empty.
        if board[index].value == 0:
            return board[index]
    return -1


def get_node_tile(board, value):
    """
    Method to search the Node object that matches the value.

    :param board:               array of Node objects
    :param value:               integer
    :return:                    Node objects
    """
    for index in range(len(board)):
        # checks if the tile is the value in the parameter.
        if board[index].value == value:
            return board[index]
    return -1


def calculate_euclidean_cost(current_board, goal_board):
    """
    This method calculates the estimate cost for euclidean approach.

    :param current_board:       array of Node objects
    :param goal_board:          array of Node objects
    :return:                    integer
    """
    h = 0
    for index in range(len(current_board)):
        new_node = current_board[index]
        if new_node.value != 0:
            goal_node = get_node_tile(goal_board, new_node.value)
            # calculating heuristic functions cost for Euclidean method.
            h += math.sqrt(
                (new_node.x - goal_node.x) ** 2 + (new_node.y - goal_node.y) ** 2
            )
    return h


def calculate_manhattan_cost(current_board, goal_board):
    """
    This method calculates the estimate cost for manhattan approach.

    :param current_board:       array of Node objects
    :param goal_board:          array of Node objects
    :return:                    integer
    """
    h = 0
    for index in range(len(current_board)):
        new_node = current_board[index]
        if new_node.value != 0:
            goal_node = get_node_tile(goal_board, new_node.value)
            # calculating heuristic functions cost for Manhattan method.
            h += abs(new_node.x - goal_node.x) + abs(new_node.y - goal_node.y)
    return h


def is_visited(visited, current_board):
    """

    :param visited:
    :param current_board:
    :return:
    """
    return visited.count(current_board) > 0


def find_successor(current_board):
    """
    Method to find the next successor.

    :param current_board:       array of Node objects
    :return:                    array of Node objects
    """
    successors_board = []
    pos_node = get_empty_tile(current_board)

    # Left move
    if pos_node.x > 0:
        temp_board = copy.deepcopy(current_board)
        empty = temp_board[pos_node.position].value
        temp_board[pos_node.position].value = temp_board[pos_node.position - 1].value
        temp_board[pos_node.position - 1].value = empty
        successors_board.append(temp_board)

    # Right move
    if pos_node.x < BOARD_SIZE - 1:
        temp_board = copy.deepcopy(current_board)
        empty = temp_board[pos_node.position].value
        temp_board[pos_node.position].value = temp_board[pos_node.position + 1].value
        temp_board[pos_node.position + 1].value = empty
        successors_board.append(temp_board)

    # Up move
    if pos_node.y > 0:
        temp_board = copy.deepcopy(current_board)
        empty = temp_board[pos_node.position].value
        temp_board[pos_node.position].value = temp_board[
            pos_node.position - BOARD_SIZE
        ].value
        temp_board[pos_node.position - BOARD_SIZE].value = empty
        successors_board.append(temp_board)

    # Down move
    if pos_node.y < BOARD_SIZE - 1:
        temp_board = copy.deepcopy(current_board)
        empty = temp_board[pos_node.position].value
        temp_board[pos_node.position].value = temp_board[
            pos_node.position + BOARD_SIZE
        ].value
        temp_board[pos_node.position + BOARD_SIZE].value = empty
        successors_board.append(temp_board)

    return successors_board


def apply_successor_to_manhattan(successor_board, current_g, goal):
    """
    This function apply successor board to the manhattan method.

    :param successor_board:     array of Node objects
    :param current_g:           integer
    :param goal:                array of Node objects
    :return:                    array
    """
    new_g = current_g + 1
    new_h = calculate_manhattan_cost(successor_board, goal)
    new_f = new_g + new_h
    return [successor_board, new_g, new_f]


def sort_by_f(element):
    """
    Function to priorities the lowest cost.

    :param element:             list of cost
    :return:                    Node object
    """
    return element[0]


def hash_value(current_boad):
    """
    Function to calculate the sum of all the hash values of the Node
    object.

    :param current_boad:        array of Node objects
    :return:                    integer
    """
    value = 1
    for node in current_boad:
        # cumulate the hash value in the board.
        value += hash(node)
    return abs(value)


def calculate_h(start, goal, is_manhattan):
    """
    Method to calculate the h cost for the A* algorithm.

    :param start:               array of Node objects
    :param goal:                array of Node objects
    :param is_manhattan:        boolean
    :return:                    integer
    """
    if is_manhattan:
        return calculate_manhattan_cost(start, goal)
    return calculate_euclidean_cost(start, goal)


def a_star_algorithm(start_state, goal_state, is_manhattan):
    """
    This method performs the A* algorithm for the 8 puzzle game.

    :param start_state:         array of Node objects
    :param goal_state:          array of Node objects
    :param is_manhattan:        boolean
    :return:                    list of board path
    """
    global start_board, GOAL_BOARD
    start_board = load_data(start_state)
    GOAL_BOARD = load_data(goal_state)

    open_set = []
    open_queue = list()
    closed_set = []
    came_from = dict()

    # calculating the algorithm cost.
    g = 0
    h = calculate_h(start_board, GOAL_BOARD, is_manhattan)
    f = g + h

    open_set.append(start_board)
    open_queue.append((f, g, start_board))

    while len(open_set) > 0:
        open_queue.sort(key=sort_by_f)
        curr_f, curr_g, point = open_queue.pop(0)

        open_set.remove(point)  # Remove the point in the open_set

        if point == GOAL_BOARD:
            # reached goal, unwind path.
            path = [point]
            while point != start_board:
                point = came_from[hash_value(point)]
                path.append(point)

            path.reverse()
            return path  # Return the current path of the movement

        closed_set.append(point)

        # Generate successors
        successors = find_successor(point)
        for successor in successors:
            # If the path is not visited, then updating the g value.
            if not is_visited(closed_set, successor):
                tentative_g_score = curr_g + 1

                if not is_visited(open_set, successor):
                    # New territory to explore.
                    came_from[hash_value(successor)] = point

                    # calculating the algorithm cost.
                    g = tentative_g_score
                    h = calculate_h(successor, GOAL_BOARD, is_manhattan)
                    f = g + h

                    open_set.append(successor)
                    open_queue.append((f, g, successor))
                else:
                    # Reconnected to previously explored area using the open_queue.
                    g_score = 0
                    for oq in open_queue:
                        if oq[2] == successor:
                            g_score = oq[1]
                            break

                    if tentative_g_score < g_score:
                        came_from[hash_value(successor)] = point

                        # calculating the algorithm cost.
                        g = tentative_g_score
                        h = calculate_manhattan_cost(successor, GOAL_BOARD)
                        f = g + h

                        for oq in open_queue:
                            if oq[2] == successor:
                                open_queue.remove(oq)
                                open_queue.append((f, g, successor))
                                break

    if len(came_from) == 0:
        print("Can't found any move")


def get_user_inputs(message, start_board=None):
    """
    Method gets the user input for the 8 puzzle game board.

    :param message:             string
    :param start_board:         2D array of integer
    :return:                    2D array of integer
    """
    print(message, "\n")

    temp_board = []
    for x in range(BOARD_SIZE):
        temp_board.append(([]))
        for y in range(BOARD_SIZE):
            temp_board[x].append(-1)
            while True:
                # Error checking on user input
                try:
                    print("Enter the values and 0 value as an empty tile.")
                    msg = "[" + str(x + 1) + "," + str(y + 1) + "]: "
                    value = int(input(msg))

                    if validate_board(temp_board, x + 1, y + 1, value):
                        print("The value is already exist: ", value)
                    elif start_board and not validate_board(
                        start_board, BOARD_SIZE, BOARD_SIZE, value
                    ):
                        print(
                            "Must enter the same range of values "
                            "as the start state,"
                            "\n"
                        )
                    else:
                        break
                except:  # catch *all* exceptions
                    print("Invalid input\n")

            temp_board[x][y] = value

    return temp_board


def validate_board(board, row, column, user_input):
    """
    Function to validate the board entered by the user.

    :param board:               2D array of integer
    :param row:                 list of integer
    :param column:              list of integer
    :param user_input:          integer
    :return:
    """
    for x in range(row):
        for y in range(column):
            if board[x][y] == user_input:
                return True
    return False


def main():
    # Get start board
    start = get_user_inputs("Enter your start state")
    if not validate_board(start, BOARD_SIZE, BOARD_SIZE, 0):
        print("Must enter 0 value to represent a blank tile")
        return

    print("Start Board: ", start, "\n")

    # Get goal board
    goal = get_user_inputs("Enter your goal state", start)
    if not validate_board(goal, BOARD_SIZE, BOARD_SIZE, 0):
        print("Must enter 0 value to represent a blank tile")
        return
    print("Goal Board: ", goal, "\n")

    # start = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
    # goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    # Getting the user input
    user_input = input(
        "Enter one of heuristic functions from the "
        "following: E - Euclidean or M - Manhattan: "
    )
    # checks if the user has selected a valid heuristic functions.
    while True:
        if user_input == "E":
            print("A* Search - Euclidean")
            time_start = time.time()
            paths = a_star_algorithm(start, goal, False)
            break
        elif user_input == "M":
            print("A* Search - Manhattan")
            time_start = time.time()
            paths = a_star_algorithm(start, goal, True)
            break
        else:
            print("Incorrect heuristic functions")
            user_input = input(
                "Enter one of heuristic functions from the "
                "following: E - Euclidean or M - Manhattan: "
            )

    time_end = time.time()
    # Counting the number of moves to reach the goal state.
    count = -1
    for path in paths:
        display_board(path)
        count += 1
        print("Move ", count)

    print("No Of Move : ", count)
    # timer to calculate how long the heuristic functions took.
    print("Time: ", time_end - time_start, " seconds")


if __name__ == "__main__":
    main()
