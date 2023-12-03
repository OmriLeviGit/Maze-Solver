def create_solver(algorithm_name):
    if algorithm_name == "breadth first search":
        from algorithms import BFS
        return BFS.solve
    elif algorithm_name == "depth first search":
        from algorithms import DFS
        return DFS.solve
    elif algorithm_name == "left hand turn":
        from algorithms import LHT
        return LHT.solve
    else:
        print(f"Unsupported algorithm: {algorithm_name}, used BFS instead")
        from algorithms import BFS
        return BFS.solve
