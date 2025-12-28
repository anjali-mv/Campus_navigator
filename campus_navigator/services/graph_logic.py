import networkx as nx
from geopy.distance import geodesic
class CampusGraph:
    def __init__(self):
        self.graph = nx.Graph()
        self.init_graph()
    def init_graph(self):
        # Define Nodes (Simulated Campus Data)
        # Center: 12.2958, 76.6394
        locations = {
            "Campus Center": (12.2958, 76.6394),
            "Library": (12.2965, 76.6394),        # North
            "Canteen": (12.2958, 76.6405),        # East
            "Hostel A": (12.2958, 76.6380),       # West
            "Academic Block": (12.2945, 76.6394), # South
            "Sports Complex": (12.2970, 76.6410), # North East
            "Main Gate": (12.2940, 76.6394),      # South of Academic Block
            "Auditorium": (12.2960, 76.6385)      # North West
        }
        # Add nodes with attributes
        for name, coords in locations.items():
            self.graph.add_node(name, pos=coords)
        # Define Edges (Walkable paths)
        edges = [
            ("Main Gate", "Academic Block"),
            ("Academic Block", "Campus Center"),
            ("Campus Center", "Library"),
            ("Campus Center", "Canteen"),
            ("Campus Center", "Hostel A"),
            ("Library", "Sports Complex"),
            ("Hostel A", "Auditorium"),
            ("Library", "Auditorium"), # Shortcut
            ("Canteen", "Sports Complex") # Shortcut
        ]
        # Add edges with weights (distance in meters)
        for u, v in edges:
            coord_u = locations[u]
            coord_v = locations[v]
            dist = geodesic(coord_u, coord_v).meters
            self.graph.add_edge(u, v, weight=dist)
    def get_shortest_path(self, start_node, end_node):
        """Returns a list of coordinates [(lat, lon), ...] for the shortest path."""
        try:
            path_nodes = nx.shortest_path(self.graph, source=start_node, target=end_node, weight="weight")
            # Convert node names to coordinates
            path_coords = [self.graph.nodes[node]["pos"] for node in path_nodes]
            return path_coords, path_nodes
        except nx.NetworkXNoPath:
            return None, []
        except nx.NodeNotFound:
             return None, []
    def get_locations(self):
        """Returns a list of location names."""
        return list(self.graph.nodes())
# Instance for easy access
campus_graph = CampusGraph()