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

Most mazes showcased here were generated using [Daedalus](https://www.astrolog.org/labyrnth/daedalus.htm), but the tool will work on any maze that adheres the assumptions below.

## Input
The program is designed to operate under the following assumptions:

- Walls are represented in black, while the path is in white.
- The width of the path is 1 pixel.
- There is one entrance and one exit — one at the top row and another at the bottom, each occupying a single pixel.
- Apart from the entrance and the exit, the maze is entirely surrounded by a continuous black wall.


The tool is capable of solving mazes of [any rectangular shape](https://github.com/OmriLeviGit/Maze-Solver/blob/main/examples/Uneven%20Maze%20-%20Dfs.jpg), and is not limited to squares.

Additionally, it has the added functionality of processing and solving mazes from [images found on the internet](https://github.com/OmriLeviGit/Maze-Solver/blob/main/examples/Maze1%20From%20The%20Internet%20-%20Dijkstra.jpg), and not just those generated using Daedalus.
However, note that while it might work, some of the algorithms may resort to an inefficient 'flood-fill' approach, as shown in this [example](https://github.com/OmriLeviGit/Maze-Solver/blob/main/examples/Maze2%20From%20The%20Internet%20-%20Dfs.jpg).

## How It Works
The program follows these key steps:

1. **Preprocessing (if from the internet)**: If the input image is from the internet, the program applies a custom smoothing filter and performs cropping before proceeding to the maze initialization phase.
2. **Maze Initializing Phase:** The program scans the image from the top-left to the bottom-right, identifying junctions and entrances.
3. **Solving Phase:** For node-based algorithms, junctions serve as nodes, and the chosen algorithm is executed. For the LHT algorithm, the program iterates through each step, regardless of junctions, until it reaches the end.
4. **Drawing Phase:** The program takes the traversed path from the start to the end, applies coloring, and enlarges the image if necessary for a clearer visualization.

The duration of each step is measured individually, and the corresponding timings are displayed at the conclusion of the process.

In addition, the image of the solved maze will be saved to a generated 'output' folder.


### [Examples](https://github.com/OmriLeviGit/Maze-Solver/tree/main/examples)
Each example offers a visual representation of the software's capabilities, showcasing how it navigates through mazes using various algorithms.
The algorithm determines the selected colors.







