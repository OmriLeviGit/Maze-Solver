def create_solver(algorithm_name):
    if algorithm_name == "breadth first search" or algorithm_name == "bfs":
        from algorithms import BFS
        return BFS.solve
    elif algorithm_name == "depth first search" or algorithm_name == "dfs":
        from algorithms import DFS
        return DFS.solve
    elif algorithm_name == "left hand turn" or algorithm_name == "lht":
        from algorithms import LHT
        return LHT.solve
    elif algorithm_name == "dijkstra":
        from algorithms import dijkstra
        return dijkstra.solve
    elif algorithm_name == "a star":
        from algorithms import a_star
        return a_star.solve
    else:
        print(f"Unsupported algorithm: {algorithm_name}, used BFS instead")
        from algorithms import BFS
        return BFS.solve
