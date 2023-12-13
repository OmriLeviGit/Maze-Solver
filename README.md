# Maze-Solver

<table>
  <tr>
    <td><img src="examples/101X101, Medium - Depth First Search.jpg" alt="DFS" width="402" height="402"></td>
    <td><img src="examples/201X201, Very Large - Left Hand Turn.jpg" alt="LHT" width="402" height="402"></td>
  </tr>
</table>


## About
Maze-Solver is a software tool designed for solving mazes effectively using various algorithms.  
The generated paths are highlighted in green, with backtracked cells in a darker shade for algorithms employing backtracking, such as the Left-Hand turn (LHT) algorithm.  
Note that LHT solutions may contain white paths in island areas, where connections are not possible using left turns only.  

All mazes showcased here were generated using [Daedalus](https://www.astrolog.org/labyrnth/daedalus.htm), but the tool will work on any maze that adheres the assumptions below.

## Input
The program operates under these specific assumptions:

- Walls are represented in black, while the path is depicted in white.
- The width of each path is precisely 1 pixel.
- There are two entrances — one at the top row and another at the bottom, each occupying a single pixel.
- Apart from the entrances, the maze is entirely surrounded by a continuous black wall.

It is recommended that input images will be placed in the 'input' folder.

Note: The tool is capable of solving mazes of any rectangular shape, and not limited to squares.

## How It Works
The program follows these key steps:

1. **Maze Initializing Phase:** The program scans the BMP file from the top-left to the bottom-right, identifying junctions and entrances.

2. **Solving Phase:** For node-based algorithms, junctions serve as nodes, and the chosen algorithm is executed. For the LHT algorithm, the program iterates through each step, regardless of junctions, until it reaches the end.

3. **Drawing Phase:** The program takes the traversed path from the start to the end, applies coloring, and enlarges the image if necessary for a clearer visualization.

The duration of each step is measured individually, and the corresponding timings are displayed at the conclusion of the process.

In addition, the image of the solved maze will be saved to a generated 'output' folder.


### [Examples](https://github.com/OmriLeviGit/Maze-Solver/tree/main/examples)
Each example offers a visual representation of the software's capabilities, showcasing how it navigates through mazes using various algorithms.
