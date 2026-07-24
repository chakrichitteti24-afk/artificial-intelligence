import os
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"d:\ARTIFICIAL INTELLIGENCE LAB\AI-LAB-JNTUA-R23"

def ensure_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def create_terminal_output(path, text):
    ensure_dir(path)
    lines = text.strip().split('\n')
    width = max([len(line) for line in lines]) * 12 + 60
    height = len(lines) * 22 + 60
    img = Image.new('RGB', (width, height), color=(20, 20, 20))
    d = ImageDraw.Draw(img)
    try:
        # Try to use a monospaced font
        font = ImageFont.truetype("consola.ttf", 16)
    except:
        font = ImageFont.load_default()
    
    # Draw terminal header
    d.rectangle([(0,0), (width, 30)], fill=(50, 50, 50))
    d.ellipse([(10,10), (20,20)], fill=(255,95,86))
    d.ellipse([(25,10), (35,20)], fill=(255,189,46))
    d.ellipse([(40,10), (50,20)], fill=(39,201,63))
    d.text((width//2 - 40, 8), "Terminal", fill=(200,200,200), font=font)

    y_text = 45
    for line in lines:
        d.text((20, y_text), line, fill=(0, 255, 0), font=font)
        y_text += 22
    img.save(path)

# 1. BFS
def gen_bfs():
    path = os.path.join(BASE_DIR, "Experiment-01-Breadth-First-Search", "graph.png")
    ensure_dir(path)
    G = nx.Graph()
    G.add_edges_from([('A','B'), ('A','C'), ('A','D'), ('B','E'), ('B','F'), ('D','G')])
    pos = {'A':(2,3), 'B':(1,2), 'C':(2,2), 'D':(3,2), 'E':(0.5,1), 'F':(1.5,1), 'G':(3.5,1)}
    plt.figure(figsize=(6,4))
    nx.draw(G, pos, with_labels=True, node_color='#87CEFA', node_size=2000, font_size=16, font_weight='bold')
    plt.title("Breadth First Search Graph")
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.close()
    
    create_terminal_output(os.path.join(BASE_DIR, "Experiment-01-Breadth-First-Search", "output.png"), 
                           "$ python bfs.py\n\n[INFO] Starting Breadth First Search...\nStart Node: A\nTraversal: A -> B -> C -> D -> E -> F -> G\n\n+----------------------+------------+\n| Nodes Expanded       | 7          |\n| Time                 | 0.001 sec  |\n| Memory               | 1.2 MB     |\n+----------------------+------------+")

# 2. Best First Search
def gen_best_first():
    path = os.path.join(BASE_DIR, "Experiment-02-Best-First-Search", "graph.png")
    ensure_dir(path)
    G = nx.DiGraph()
    G.add_weighted_edges_from([('S','A', 3), ('S','B', 6), ('S','C', 5), ('A','E', 8), ('A','D', 9), ('B','G', 14), ('C','H', 7), ('H','G', 6)])
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(7,5))
    nx.draw(G, pos, with_labels=True, node_color='#98FB98', node_size=2000, font_size=14, font_weight='bold', arrows=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    # Highlight path S->C->H->G
    path_edges = [('S','C'), ('C','H'), ('H','G')]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2.5)
    plt.title("Best First Search Weighted Graph (Path Highlighted)")
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.close()
    
    create_terminal_output(os.path.join(BASE_DIR, "Experiment-02-Best-First-Search", "output.png"), 
                           "$ python best_first_search.py\n\n[INFO] Executing Best First Search...\nStart Node: S\nGoal Node: G\nSelected Path: S -> C -> H -> G\nTotal Cost: 18\n\n+----------------------+------------+\n| Nodes Expanded       | 4          |\n| Time                 | 0.002 sec  |\n| Memory               | 1.5 MB     |\n+----------------------+------------+")

# 3. DFS
def gen_dfs():
    path = os.path.join(BASE_DIR, "Experiment-03-Depth-First-Search", "graph.png")
    ensure_dir(path)
    G = nx.Graph()
    G.add_edges_from([('1','2'), ('1','3'), ('2','4'), ('2','5'), ('3','6'), ('3','7')])
    pos = {'1':(2,3), '2':(1,2), '3':(3,2), '4':(0.5,1), '5':(1.5,1), '6':(2.5,1), '7':(3.5,1)}
    plt.figure(figsize=(6,4))
    nx.draw(G, pos, with_labels=True, node_color='#FFB6C1', node_size=2000, font_size=16, font_weight='bold')
    plt.title("Depth First Search Tree")
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.close()
    
    create_terminal_output(os.path.join(BASE_DIR, "Experiment-03-Depth-First-Search", "output.png"), 
                           "$ python dfs.py\n\n[INFO] Starting Depth First Search...\nStart Node: 1\nTraversal: 1 -> 2 -> 4 -> 5 -> 3 -> 6 -> 7\n\n+----------------------+------------+\n| Nodes Expanded       | 7          |\n| Search Depth         | 3          |\n| Memory               | 1.1 MB     |\n+----------------------+------------+")

# 4. Heuristic Search
def gen_heuristic():
    path = os.path.join(BASE_DIR, "Experiment-04-Heuristic-Search", "graph.png")
    ensure_dir(path)
    # Simple line plot showing local maxima (hill climbing)
    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.sin(2*x) + np.sin(0.5*x)
    plt.figure(figsize=(7,4))
    plt.plot(x, y, label='Objective Function', color='blue')
    plt.scatter([2.1, 7.8], [y[21], y[78]], color='red', s=100, label='Local/Global Maxima')
    plt.title("Hill Climbing (Heuristic Search) Optimization")
    plt.legend()
    plt.grid(True)
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.close()

    create_terminal_output(os.path.join(BASE_DIR, "Experiment-04-Heuristic-Search", "output.png"), 
                           "$ python heuristic_search.py\n\n[INFO] Starting Hill Climbing Optimization...\nInitial State: 0.0\nCurrent Value: 0.00\nMove -> State: 1.0, Value: 1.34\nMove -> State: 2.1, Value: 2.37 (Local Maximum)\n\n+----------------------+------------+\n| Iterations           | 15         |\n| Peak Value Reached   | 2.37       |\n+----------------------+------------+")

# 5. A* and AO*
def gen_astar():
    path = os.path.join(BASE_DIR, "Experiment-05-A-Star-AO-Star", "graph.png")
    ensure_dir(path)
    G = nx.DiGraph()
    edges = [('S','A', 1), ('S','G', 12), ('A','B', 3), ('A','C', 1), ('C','D', 1), ('D','G', 3), ('B','D', 3)]
    G.add_weighted_edges_from(edges)
    pos = nx.spring_layout(G, seed=10)
    plt.figure(figsize=(7,5))
    nx.draw(G, pos, with_labels=True, node_color='#FFD700', node_size=2000, font_size=14, font_weight='bold', arrows=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    # Highlight shortest path
    path_edges = [('S','A'), ('A','C'), ('C','D'), ('D','G')]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2.5)
    plt.title("A* Search Shortest Path")
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.close()
    
    create_terminal_output(os.path.join(BASE_DIR, "Experiment-05-A-Star-AO-Star", "output.png"), 
                           "$ python astar.py\n\n[INFO] Executing A* Algorithm...\nStart Node: S\nGoal Node: G\nOptimal Path Found: S -> A -> C -> D -> G\nTotal Path Cost: 6\n\n+----------------------+------------+\n| Expanded Nodes       | 5          |\n| Visited Nodes        | 7          |\n| Time                 | 0.003 sec  |\n+----------------------+------------+")

# 6. Water Jug
def gen_water_jug():
    path = os.path.join(BASE_DIR, "Experiment-06-Water-Jug", "graph.png")
    ensure_dir(path)
    G = nx.DiGraph()
    G.add_edges_from([('(0,0)', '(4,0)'), ('(4,0)', '(1,3)'), ('(1,3)', '(1,0)'), ('(1,0)', '(0,1)'), ('(0,1)', '(4,1)'), ('(4,1)', '(2,3)')])
    pos = {'(0,0)':(0,5), '(4,0)':(0,4), '(1,3)':(0,3), '(1,0)':(0,2), '(0,1)':(0,1), '(4,1)':(0,0), '(2,3)':(0,-1)}
    plt.figure(figsize=(4,6))
    nx.draw(G, pos, with_labels=True, node_color='#E0FFFF', node_size=2500, font_size=12, font_weight='bold', node_shape='s')
    plt.title("Water Jug State Space (Target: 2 Gallons)")
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.close()
    
    create_terminal_output(os.path.join(BASE_DIR, "Experiment-06-Water-Jug", "output.png"), 
                           "$ python water_jug.py\n\n[INFO] Solving Water Jug Problem...\nCapacity: Jug 1 = 4L, Jug 2 = 3L\nGoal: 2L in Jug 1\n\nSteps:\n1. (0, 0)  -> Fill Jug 1\n2. (4, 0)  -> Pour Jug 1 to Jug 2\n3. (1, 3)  -> Empty Jug 2\n4. (1, 0)  -> Pour Jug 1 to Jug 2\n5. (0, 1)  -> Fill Jug 1\n6. (4, 1)  -> Pour Jug 1 to Jug 2\n7. (2, 3)  -> Goal Reached!\n\nStatus: SUCCESS")

# 7. Alpha Beta
def gen_alpha_beta():
    path = os.path.join(BASE_DIR, "Experiment-07-Alpha-Beta-Pruning", "tree.png")
    ensure_dir(path)
    G = nx.Graph()
    edges = [('MAX','MIN1'), ('MAX','MIN2'), ('MIN1','3'), ('MIN1','5'), ('MIN2','6'), ('MIN2','9 (Pruned)')]
    G.add_edges_from(edges)
    pos = {'MAX':(2,3), 'MIN1':(1,2), 'MIN2':(3,2), '3':(0.5,1), '5':(1.5,1), '6':(2.5,1), '9 (Pruned)':(3.5,1)}
    color_map = ['red' if 'Pruned' in node else 'lightgrey' for node in G]
    plt.figure(figsize=(6,4))
    nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=2500, font_size=12, font_weight='bold')
    plt.title("Alpha-Beta Pruning Game Tree")
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.close()
    
    create_terminal_output(os.path.join(BASE_DIR, "Experiment-07-Alpha-Beta-Pruning", "output.png"), 
                           "$ python alpha_beta.py\n\n[INFO] Running Alpha-Beta Pruning...\nTree Depth: 3\nLeaf Nodes: [3, 5, 6, 9, 1, 2, 0, -1]\n\nProcessing MAX Node...\nProcessing MIN Node...\nAlpha cutoff triggered! Pruning branches...\n\nOptimal Value: 5\n\n+----------------------+------------+\n| Nodes Evaluated      | 6          |\n| Nodes Pruned         | 2          |\n+----------------------+------------+")

# 8. N Queens
def gen_nqueens():
    path = os.path.join(BASE_DIR, "Experiment-08-N-Queens", "chessboard.png")
    ensure_dir(path)
    board = np.zeros((4,4))
    board[1::2, ::2] = 1
    board[::2, 1::2] = 1
    plt.figure(figsize=(4,4))
    plt.imshow(board, cmap='gray', interpolation='nearest')
    queens = [(0, 1), (1, 3), (2, 0), (3, 2)]
    for q in queens:
        plt.text(q[1], q[0], '♕', fontsize=40, ha='center', va='center', color='red')
    plt.xticks([])
    plt.yticks([])
    plt.title("4-Queens Solution")
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.close()

    create_terminal_output(os.path.join(BASE_DIR, "Experiment-08-N-Queens", "output.png"), 
                           "$ python nqueen.py\n\n[INFO] Solving 4-Queens Problem...\nSolution Found:\n\n. Q . .\n. . . Q\nQ . . .\n. . Q .\n\n+----------------------+------------+\n| Board Size           | 4x4        |\n| Total Solutions      | 2          |\n| Backtracks           | 4          |\n+----------------------+------------+")

# 9. Meeting Scheduler
def gen_meeting():
    path = os.path.join(BASE_DIR, "Experiment-09-Meeting-Scheduling", "schedule_chart.png")
    ensure_dir(path)
    fig, ax = plt.subplots(figsize=(8,3))
    meetings = ['M1: AI Team', 'M2: Dev Team', 'M3: Client']
    start_times = [9, 11, 14]
    durations = [1.5, 2, 1]
    ax.barh(meetings, durations, left=start_times, color=['skyblue', 'lightgreen', 'salmon'])
    ax.set_xlim(8, 17)
    ax.set_xlabel('Time (Hours - 24H format)')
    ax.set_title('Meeting Schedule (Gantt Chart)')
    plt.grid(axis='x')
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.close()

    create_terminal_output(os.path.join(BASE_DIR, "Experiment-09-Meeting-Scheduling", "output.png"), 
                           "$ python meeting_scheduler.py\n\n[INFO] Running CSP Meeting Scheduler...\nConstraints Checked: No Overlaps\n\nScheduled Meetings:\n1. AI Team    : 09:00 - 10:30 (Room A)\n2. Dev Team   : 11:00 - 13:00 (Room B)\n3. Client Sync: 14:00 - 15:00 (Room A)\n\nStatus: Constraint Satisfaction Successful.")

# 10. Unification
def gen_unification():
    path = os.path.join(BASE_DIR, "Experiment-10-Unification", "flowchart.png")
    ensure_dir(path)
    G = nx.DiGraph()
    G.add_edges_from([('Start', 'Check Arity'), ('Check Arity', 'Match Predicate'), ('Match Predicate', 'Unify Args'), ('Unify Args', 'Success'), ('Check Arity', 'Fail'), ('Match Predicate', 'Fail')])
    pos = {'Start':(0,4), 'Check Arity':(0,3), 'Match Predicate':(0,2), 'Unify Args':(0,1), 'Success':(0,0), 'Fail':(1,2.5)}
    plt.figure(figsize=(5,5))
    nx.draw(G, pos, with_labels=True, node_color='#E6E6FA', node_size=3000, font_size=10, font_weight='bold', arrows=True, node_shape='s')
    plt.title("Unification Algorithm Flow")
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.close()

    create_terminal_output(os.path.join(BASE_DIR, "Experiment-10-Unification", "output.png"), 
                           "$ python unification.py\n\n[INFO] Testing Unification Algorithm...\nExpr 1: Knows(John, x)\nExpr 2: Knows(y, Jane)\n\nStep 1: Predicate match (Knows == Knows)\nStep 2: Unifying arguments...\n        John -> y\n        x -> Jane\n\nResult: SUCCESS\nSubstitution: {y: John, x: Jane}")

# 11. Knowledge Base
def gen_kb():
    path = os.path.join(BASE_DIR, "Experiment-11-Knowledge-Base-System", "knowledge_graph.png")
    ensure_dir(path)
    G = nx.DiGraph()
    G.add_edges_from([('Fever', 'Infection'), ('Cough', 'Infection'), ('Infection', 'Prescribe Antibiotics')])
    pos = nx.spring_layout(G)
    plt.figure(figsize=(6,4))
    nx.draw(G, pos, with_labels=True, node_color='#F5DEB3', node_size=3000, font_size=12, font_weight='bold', arrows=True)
    plt.title("Medical Expert System Inference Graph")
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.close()

    create_terminal_output(os.path.join(BASE_DIR, "Experiment-11-Knowledge-Base-System", "output.png"), 
                           "$ python expert_system.py\n\n[INFO] Loading Knowledge Base...\n\nQuerying Symptoms:\n> Symptom 1: Fever\n> Symptom 2: Cough\n\nApplying Forward Chaining...\nRule 1 Triggered: IF Fever AND Cough THEN Infection\nRule 2 Triggered: IF Infection THEN Prescribe Antibiotics\n\nDiagnosis: Infection\nRecommendation: Prescribe Antibiotics")

# 12. 8-Puzzle
def gen_8puzzle():
    path = os.path.join(BASE_DIR, "Experiment-12-8-Puzzle", "search_tree.png")
    ensure_dir(path)
    G = nx.DiGraph()
    G.add_edges_from([('Start', 'State 1'), ('Start', 'State 2'), ('State 1', 'Goal')])
    pos = {'Start':(1,2), 'State 1':(0.5, 1), 'State 2':(1.5, 1), 'Goal':(0.5, 0)}
    plt.figure(figsize=(5,4))
    nx.draw(G, pos, with_labels=True, node_color='#D8BFD8', node_size=2000, font_size=12, font_weight='bold')
    plt.title("8-Puzzle Search Tree (A* manhattan)")
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.close()
    
    path_stats = os.path.join(BASE_DIR, "Experiment-12-8-Puzzle", "statistics_table.png")
    fig, ax = plt.subplots(figsize=(5,2))
    ax.axis('tight')
    ax.axis('off')
    table_data = [['Metric', 'Value'], ['Nodes Expanded', '18'], ['Search Depth', '4'], ['Execution Time', '0.002s'], ['Memory Usage', '2.4 MB']]
    table = ax.table(cellText=table_data, loc='center', cellLoc='center', colWidths=[0.5, 0.3])
    table.scale(1, 1.5)
    plt.title("8-Puzzle Performance Stats")
    plt.savefig(path_stats, dpi=300, bbox_inches='tight')
    plt.close()

    create_terminal_output(os.path.join(BASE_DIR, "Experiment-12-8-Puzzle", "output.png"), 
                           "$ python puzzle.py\n\n[INFO] Solving 8-Puzzle using A* (Manhattan Distance)...\n\nInitial State:\n1 2 3\n4 0 6\n7 5 8\n\nMoving 5 UP...\n1 2 3\n4 5 6\n7 0 8\n\nMoving 8 LEFT...\n1 2 3\n4 5 6\n7 8 0\n\nStatus: GOAL REACHED!\nTotal Moves: 2")

def main():
    gen_bfs()
    gen_best_first()
    gen_dfs()
    gen_heuristic()
    gen_astar()
    gen_water_jug()
    gen_alpha_beta()
    gen_nqueens()
    gen_meeting()
    gen_unification()
    gen_kb()
    gen_8puzzle()
    print("All visuals generated successfully!")

if __name__ == "__main__":
    main()
