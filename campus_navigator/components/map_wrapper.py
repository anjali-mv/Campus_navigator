import reflex as rx
from ..state import State
def map_component():
    return rx.box(
        # Leaflet CSS
        rx.html('<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" crossorigin="" />'),
        # Leaflet JS
        rx.script(src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js", crossorigin=""),
        
        # Map Container
        rx.html('<div id="map" style="height: 100vh; width: 100vw; border-radius: 16px; z-index: 0;"></div>'),
        
        # Map Initialization & Logic
        rx.script("""
            function initMap() {
                var container = document.getElementById('map');
                if (!container) return;
                
                // If map is already initialized on this container, do nothing
                if (container._leaflet_id) return;
                // Initialize Map and assign to window for global access
                window.campusMap = L.map('map').setView([12.2958, 76.6394], 17);
                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 19,
                    attribution: '© OpenStreetMap'
                }).addTo(window.campusMap);
                
                // Add markers
                var locations = [
                    {"name": "Campus Center", "lat": 12.2958, "lon": 76.6394},
                    {"name": "Library", "lat": 12.2965, "lon": 76.6394},
                    {"name": "Canteen", "lat": 12.2958, "lon": 76.6405},
                    {"name": "Hostel A", "lat": 12.2958, "lon": 76.6380},
                    {"name": "Academic Block", "lat": 12.2945, "lon": 76.6394},
                    {"name": "Sports Complex", "lat": 12.2970, "lon": 76.6410},
                    {"name": "Main Gate", "lat": 12.2940, "lon": 76.6394},
                    {"name": "Auditorium", "lat": 12.2960, "lon": 76.6385}
                ];
                
                locations.forEach(loc => {
                    L.marker([loc.lat, loc.lon])
                     .addTo(window.campusMap)
                     .bindPopup(loc.name);
                });
            }
            
            // Wait for Leaflet to load
            var checkLeaflet = setInterval(function() {
                if (typeof L !== 'undefined') {
                    clearInterval(checkLeaflet);
                    initMap();
                }
            }, 100);
        """),
        
        # Reactive Script to Update Path
        rx.script(
            f"""
            if (typeof L !== 'undefined' && window.campusMap) {{
                // Clear existing path if stored globally or find it
                if (window.pathLayer) {{
                    window.campusMap.removeLayer(window.pathLayer);
                }}
                
                // data is injected from python state
                var pathData = {State.path_coords}; 
                
                if (pathData && pathData.length > 0) {{
                     window.pathLayer = L.polyline(pathData, {{color: 'blue', weight: 5}}).addTo(window.campusMap);
                     window.campusMap.fitBounds(window.pathLayer.getBounds());
                }}
            }}
            """
        ),
        width="100%",
        height="100%",
        position="relative"
    )