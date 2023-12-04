# Maze-Solver

![Maze Solver](https://github.com/OmriLeviGit/Maze-Solver/blob/main/examples/151x151%2C%20Large%20-%20breadth%20first%20search.jpg?raw=true)

## About
Maze-Solver is a software tool designed for solving mazes effectively using various algorithms.
The generated paths are highlighted in green, with backtracked cells in a darker shade for algorithms employing backtracking, such as the Left-Hand turn (LHT) algorithm.
Note that LHT solutions may contain white paths in island areas, where connections are not possible using left turns only.

All mazes showcased here were generated using [Daedalus](https://www.astrolog.org/labyrnth/daedalus.htm), but the tool will work on any maze that adheres the assumptions below.

## Input
The program operates under these specific assumptions:

- Walls are represented in black, while the path is depicted in white.
- The width of each path is precisely 1 pixel.
- There are two entrances — one at the top row and another at the bottom—each occupying a single pixel.
- Apart from the entrances, the maze is entirely surrounded by a continuous black wall.

Input images should be placed in the 'input' folder, and the corresponding solutions will be saved to the 'output' folder.

The tool is able to solve any rectangle maze, not only squares.


## How It Works
The program follows these key steps:

1. **Maze Building Phase:** The program scans the BMP file from the top-left to the bottom-right, identifying junctions, including the entrances.

2. **Solving Phase:** For node-based algorithms, junctions serve as nodes, and the chosen algorithm is executed. For the LHT algorithm, the program iterates through each step, regardless of junctions, until it reaches the end.

3. **Drawing:** The program takes the traversed path from the start to the end, applies coloring, and enlarges the image if necessary for a clearer visualization.

### [Examples](https://github.com/OmriLeviGit/Maze-Solver/tree/main/examples)
Each example offers a visual representation of the software's capabilities, showcasing how it navigates through mazes using various algorithms.
