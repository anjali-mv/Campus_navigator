# Campus Navigator 🎓📍
![Campus Navigator Banner](assets/demo.png)
[![Reflex](https://img.shields.io/badge/Reflex-F5F5F5?style=for-the-badge&logo=reflex&logoColor=black)](https://reflex.dev/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Status](https://img.shields.io/badge/Status-Hackathon_MVP-success?style=for-the-badge)]()
**Campus Navigator** is an AI-powered spatial navigation system designed to help students and visitors navigate complex university campuses effortlessly. By combining a modern Glassmorphism UI with robust pathfinding algorithms, we bridge the gap between static maps and dynamic, user-friendly guidance.
---
## 🚀 Features
*   **🤖 AI-Powered Chat**: Ask for directions naturally (e.g., *"Take me to the Library"*).
*   **🗺️ Interactive Map**: Zoomable, pannable Leaflet map with simulated real-time tracking.
*   **📍 Smart Routing**: Instantly visualizes the shortest walking path using Dijkstra's algorithm.
*   **💎 Glassmorphism UI**: A futuristic, high-contrast dark theme designed for visual appeal.
*   **📱 Responsive Design**: Optimized for seamless use on Mobile, Tablet, and Desktop.
*   **♿ Accessible**: Full keyboard support and screen-reader friendly structure.
---
## 🛠️ Tech Stack
This project is built as a **Full-Stack Python Application** using the [Reflex](https://reflex.dev/) framework.
| Component | Technology | Description |
| :--- | :--- | :--- |
| **Framework** | **Reflex** | Unified Frontend & Backend in pure Python. |
| **Language** | **Python 3.12+** | Core logic and scripting. |
| **Pathfinding** | **NetworkX** | Graph algorithms for shortest path calculations. |
| **Geography** | **Geopy** | Distance calculation between physical coordinates. |
| **Mapping** | **Leaflet.js** | Interactive map rendering engine. |
| **Styling** | **CSS / Tailwind** | Custom Glassmorphism styles. |
---
## 🏁 Getting Started
Follow these steps to set up the project locally.
### Prerequisites
*   Python 3.8 or higher
*   Git
### Installation
1.  **Clone the repository**
    ```bash
    git clone https://github.com/anjali-mv/campus_navigator
    cd campus-navigator
    ```
2.  **Create a virtual environment**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```
3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    *(If `requirements.txt` is missing, install manually: `pip install reflex networkx geopy`)*
4.  **Initialize the app**
    ```bash
    reflex init
    ```
### Running the App
Start the development server:
```bash
reflex run
```
The application will be available at:
*   **Frontend**: `http://localhost:3000`
*   **Backend**: `http://localhost:8000`
---
## 📂 Project Structure
```text
campus_navigator/
├── assets/                 # Images and static assets
├── campus_navigator/       # Main application source
│   ├── components/         # UI Components (Chat, Map)
│   ├── services/           # Backend Logic (Graph, Pathfinding)
│   ├── state.py            # App State Management
│   └── styles.py           # Global Styles
├── rxconfig.py             # Reflex Configuration
└── requirements.txt        # Python Dependencies
```
---
## 🤝 Future Roadmap
*   [ ] **Voice Integration**: Speech-to-text for hands-free navigation.
*   [ ] **Real GPS**: Replace simulation with real-time device geolocation.
*   [ ] **Google Maps API**: Switch to satellite tiles for enhanced outdoor visibility.
---
## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
---
*Built from HackHive Team*
