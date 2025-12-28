import reflex as rx
from typing import List, Tuple
from .services.graph_logic import campus_graph
class State(rx.State):
    """The app state."""
    
    # User Interaction
    chat_history: List[Tuple[str, str]] = [
        ("System", "Welcome to Campus Navigator! Ask me for directions (e.g., 'Way to Library').")
    ]
    input_text: str = ""
    
    # Navigation Data
    current_location: str = "Main Gate" # Simulation start
    target_location: str = ""
    path_coords: List[Tuple[float, float]] = []
    
    # Map Data
    markers: List[dict] = [] # For plotting markers on the map
    def on_load(self):
        """Initialize map markers."""
        locations = campus_graph.get_locations()
        # In a real app, we would load these as markers. 
        # For now we can just log them or prepare them for the UI.
        pass
    def handle_submit(self):
        """Handle chat input."""
        user_msg = self.input_text
        if not user_msg:
            return
        
        self.chat_history.append(("User", user_msg))
        self.input_text = ""
        
        # Simple NLP / Keyword matching
        response = self.process_query(user_msg)
        self.chat_history.append(("System", response))
    def process_query(self, query: str) -> str:
        query = query.lower()
        
        # Check for navigation intent
        locations = campus_graph.get_locations() # ["Library", "Canteen", ...]
        target = None
        
        for loc in locations:
            if loc.lower() in query:
                target = loc
                break
        
        if target:
            self.target_location = target
            path, nodes = campus_graph.get_shortest_path(self.current_location, target)
            if path:
                self.path_coords = path
                return f"Navigating from {self.current_location} to {target}. Follow the blue path."
            else:
                return f"Could not find a path to {target}."
        
        # Check for "Where am I"
        if "where am i" in query:
            return f"You are currently at {self.current_location}."
            
        return "I can help you navigate. Try saying 'Go to Library' or 'Where is Canteen?'"
    def set_location(self, loc: str):
        """Simulate user moving to a location."""
        if loc in campus_graph.get_locations():
            self.current_location = loc