from flask import Flask, render_template, request

app = Flask(__name__)

# Dijkstra Algorithm Function
def dijkstra(graph, start):
    shortest_distance = {}
    predecessor = {}
    unseen_nodes = graph.copy()
    infinity = float('inf')

    for node in unseen_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        for child_node, weight in graph[min_node].items():
            if weight + shortest_distance[min_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_node]
                predecessor[child_node] = min_node
        unseen_nodes.pop(min_node)

    return shortest_distance, predecessor


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        start = request.form['start'].upper().strip()
        end = request.form['end'].upper().strip()

        graph = {
            'A': {'B': 6, 'D': 1},
            'B': {'A': 6, 'D': 2, 'E': 2, 'C': 5},
            'C': {'B': 5, 'E': 5},
            'D': {'A': 1, 'B': 2, 'E': 1},
            'E': {'B': 2, 'D': 1, 'C': 5}
        }

        if start not in graph or end not in graph:
            result = "Invalid nodes! Please enter between A–E."
        else:
            distances, predecessors = dijkstra(graph, start)

            path = []
            current = end
            while current != start:
                try:
                    path.insert(0, current)
                    current = predecessors[current]
                except KeyError:
                    result = " Path not reachable."
                    break
            path.insert(0, start)
            if result is None:
                result = f"Shortest Path: {' → '.join(path)} | Total Distance: {distances[end]} km"

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)