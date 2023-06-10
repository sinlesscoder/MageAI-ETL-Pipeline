## Diagrams Module in Python

### Description

- `diagrams` is a module in Python that allows an end user to construct high-quality flow charts programmatically. Behind the scenes, it uses a dependency called `graphviz`. This means that the flow charts are represented by a graph data structure in Python.

### Graphs

- Graphs are data structures that contain the following properties:
  - `Nodes` : Different entities in the graph
  - `Edges` : Relationships between different entities in the graph

![](https://p131.p1.n0.cdn.getcloudapp.com/items/DOuKjpk6/03b6b270-828c-4e2d-92c5-fa8be31b13ee.jpg?v=0b61ed5216b0088d3a4f40616dc0de3a)

### Installation

- Graphviz (Windows)

```bash
choco install graphviz
```

- Mac or Linux (Homebrew)

```bash
brew install graphviz
```

- Via `pip`

```python
pip install diagrams
```

### Basic Usage

`Diagram` happens to be a class that gets imported from the `diagrams` package.

```python
from diagrams import Diagram
```

- `Diagram` is essentially a part of a context manager in which you can define your other graph properties such as your `nodes`, `edges`, and groups of `nodes` which are referred to as `clusters`.

- Reminder: context manager refers to any block in Python that starts with the word `with` .

```python
from diagrams import Diagram, Node

# Context Manager
with Diagram('sample_diagram'):
    # Add a node
    node_one = Node('sample_node')

    # Add a second node
    node_two = Node('node_two')

    # Connect them
    node_one >> node_two
```

### Classes

- `Node`: Individual node
- `Edge`: Edge between nodes
- `Cluster`: Groups nodes together
