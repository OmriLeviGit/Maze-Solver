# Left Hand Turn

def solve(maze):
    is_completed = False

    y_start, x_start = maze.start.coordinates
    start_direction = ''
    if y_start == 0:                    # Starting at the top, heading down
        start_direction = 'S'
    if x_start == 0:                    # Starting at the left, heading right
        start_direction = 'E'
    if y_start == maze.array.shape[0]:  # Starting at the bottom, heading up
        start_direction = 'N'
    if x_start == maze.array.shape[1]:  # Starting at the right, heading left
        start_direction = 'W'

    facing = start_direction
    position = maze.start.coordinates
    path = [position]
    times_visited_start = 0

    while not is_completed:
        if position == maze.start.coordinates:  # Looping to the start means the maze cannot be completed
            times_visited_start += 1

            if times_visited_start > 1:
                break

        if left_is_clear(facing, position, maze.array):
            facing = turn_left(facing)
        if front_is_clear(facing, position, maze.array):
            position = move_forward(facing, position)
            path.append(position)
        else:
            facing = turn_right(facing)     # Turn right or make a U-turn

        if position == maze.end.coordinates:
            is_completed = True

    return path, is_completed


def move_forward(facing, position):
    if facing == "N":
        return position[0] - 1, position[1]
    elif facing == "E":
        return position[0], position[1] + 1
    elif facing == "S":
        return position[0] + 1, position[1]
    elif facing == "W":
        return position[0], position[1] - 1


def turn_left(facing):
    if facing == "N":
        return "W"
    elif facing == "E":
        return "N"
    elif facing == "S":
        return "E"
    elif facing == "W":
        return "S"


def turn_right(facing):
    if facing == "N":
        return "E"
    elif facing == "E":
        return "S"
    elif facing == "S":
        return "W"
    elif facing == "W":
        return "N"


def left_is_clear(facing, position, array):
    if facing == "N":
        left = (position[0], position[1] - 1)
    elif facing == "E":
        left = (position[0] - 1, position[1])
    elif facing == "S":
        left = (position[0], position[1] + 1)
    else:
        left = (position[0] + 1, position[1])

    return array[left] != 0


def front_is_clear(facing, position, array):
    if facing == "N":
        front = (position[0] - 1, position[1])
    elif facing == "E":
        front = (position[0], position[1] + 1)
    elif facing == "S":
        front = (position[0] + 1, position[1])
    else:
        front = (position[0], position[1] - 1)

    return array[front] != 0
