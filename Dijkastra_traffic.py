from flask import Flask, render_template, request, send_file
import networkx as nx
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Create a sample weighted graph
def create_graph():
    G = nx.Graph()
    edges = [
        ("A", "B", 6),
        ("A", "D", 1),
        ("B", "D", 2),
        ("B", "E", 2),
        ("B", "C", 5),
        ("C", "E", 5),
        ("D", "E", 1)
    ]
    G.add_weighted_edges_from(edges)
    return G


def dijkstra_shortest_path(G, start, end):
    try:
        path = nx.dijkstra_path(G, start, end, weight="weight")
        distance = nx.dijkstra_path_length(G, start, end, weight="weight")
        return path, distance
    except nx.NetworkXNoPath:
        return None, None


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    path_img = None
    if request.method == "POST":
        start = request.form["start"].upper().strip()
        end = request.form["end"].upper().strip()

        G = create_graph()

        if start not in G.nodes or end not in G.nodes:
            result = "❌ Invalid nodes! Please use nodes A–E."
        else:
            path, distance = dijkstra_shortest_path(G, start, end)
            if path:
                result = f" Shortest Path: {' → '.join(path)} | Total Distance: {distance} km"

                # Draw the graph
                pos = nx.spring_layout(G)
                plt.figure(figsize=(6, 4))
                nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10)
                edge_labels = nx.get_edge_attributes(G, 'weight')
                nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

                # Highlight shortest path
                path_edges = list(zip(path, path[1:]))
                nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='orange')
                nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

                os.makedirs("static", exist_ok=True)
                plt.savefig("static/graph.png")
                plt.close()
                path_img = "static/graph.png"
            else:
                result = " Path not reachable."

    return render_template("index.html", result=result, path_img=path_img)


if __name__ == "__main__":
    app.run(debug=True)
