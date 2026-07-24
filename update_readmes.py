import os

BASE_DIR = r"d:\ARTIFICIAL INTELLIGENCE LAB\AI-LAB-JNTUA-R23"

# Update generate_visuals.py to use high DPI
gen_script_path = os.path.join(BASE_DIR, "generate_visuals.py")
with open(gen_script_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("plt.savefig(path)", "plt.savefig(path, dpi=300, bbox_inches='tight')")
content = content.replace("plt.savefig(path_stats)", "plt.savefig(path_stats, dpi=300, bbox_inches='tight')")

with open(gen_script_path, "w", encoding="utf-8") as f:
    f.write(content)

# Update README.md files to include image links
dirs = [
    "Experiment-01-Breadth-First-Search",
    "Experiment-02-Best-First-Search",
    "Experiment-03-Depth-First-Search",
    "Experiment-04-Heuristic-Search",
    "Experiment-05-A-Star-AO-Star",
    "Experiment-06-Water-Jug",
    "Experiment-07-Alpha-Beta-Pruning",
    "Experiment-08-N-Queens",
    "Experiment-09-Meeting-Scheduling",
    "Experiment-10-Unification",
    "Experiment-11-Knowledge-Base-System",
    "Experiment-12-8-Puzzle"
]

for d in dirs:
    readme_path = os.path.join(BASE_DIR, d, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            readme_content = f.read()

        # Insert graph image after ## Graph Representation
        # or ## Visualization if it exists
        if "![Graph]" not in readme_content:
            if "## Graph Representation" in readme_content:
                readme_content = readme_content.replace(
                    "## Graph Representation\n",
                    "## Graph Representation\n\n![Graph](graph.png)\n"
                )
            elif "## Visualization" in readme_content:
                readme_content = readme_content.replace(
                    "## Visualization\n",
                    "## Visualization\n\n![Graph](graph.png)\n"
                )

        # Insert output image after ## Output
        if "![Output]" not in readme_content:
            if "## Output" in readme_content:
                readme_content = readme_content.replace(
                    "## Output\n",
                    "## Output\n\n![Output](output.png)\n"
                )
        
        # for Exp 7, it's tree.png
        if d == "Experiment-07-Alpha-Beta-Pruning":
            readme_content = readme_content.replace("![Graph](graph.png)", "![Graph](tree.png)")
        
        # for Exp 8, it's chessboard.png
        if d == "Experiment-08-N-Queens":
            readme_content = readme_content.replace("![Graph](graph.png)", "![Graph](chessboard.png)")
            
        # for Exp 9, it's schedule_chart.png
        if d == "Experiment-09-Meeting-Scheduling":
            readme_content = readme_content.replace("![Graph](graph.png)", "![Graph](schedule_chart.png)")
            
        # for Exp 10, it's flowchart.png
        if d == "Experiment-10-Unification":
            readme_content = readme_content.replace("![Graph](graph.png)", "![Graph](flowchart.png)")
            
        # for Exp 11, it's knowledge_graph.png
        if d == "Experiment-11-Knowledge-Base-System":
            readme_content = readme_content.replace("![Graph](graph.png)", "![Graph](knowledge_graph.png)")
            
        # for Exp 12, it's search_tree.png and statistics_table.png
        if d == "Experiment-12-8-Puzzle":
            readme_content = readme_content.replace("![Graph](graph.png)", "![Graph](search_tree.png)\n\n![Statistics](statistics_table.png)")

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(readme_content)

print("Updated generate_visuals.py and README.md files.")
