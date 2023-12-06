# Left Hand Turn

def solve(maze):
    y_start, x_start = maze.start.coordinates
    start_direction = ''
    if y_start == 0:  # starting at the top, heading down
        start_direction = 'S'
    if x_start == 0:  # starting at the left, heading right
        start_direction = 'E'
    if y_start == maze.array.shape[0]:  # starting at the bottom, heading up
        start_direction = 'N'
    if x_start == maze.array.shape[1]:  # starting at the right, heading left
        start_direction = 'W'

    facing = start_direction
    position = maze.start.coordinates
    array = maze.array
    is_completed = False
    path = [position]

    while not is_completed:
        if left_is_clear(facing, position, array):
            facing = turn_left(facing)
        if front_is_clear(facing, position, array):
            position = move_forward(facing, position)
            path.append(position)
        else:
            facing = turn_right(facing)  # Turn right or make a U-turn

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
