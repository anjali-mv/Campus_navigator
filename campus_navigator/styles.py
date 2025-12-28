import reflex as rx
# Colors
BG_COLOR = "#0f172a" # Dark Slate
ACCENT_COLOR = "#38bdf8" # Sky Blue
TEXT_COLOR = "#f8fafc" # Slate 50
GLASS_BG = "rgba(30, 41, 59, 0.7)" # Slate 800 with opacity
GLASS_BORDER = "rgba(255, 255, 255, 0.1)"
# Glassmorphism Style
glass_style = {
    "background": GLASS_BG,
    "backdrop_filter": "blur(12px)",
    "border": f"1px solid {GLASS_BORDER}",
    "box_shadow": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    "border_radius": "16px",
}
# Global Styles
base_style = {
    "background_color": BG_COLOR,
    "color": TEXT_COLOR,
    "font_family": "Inter, sans-serif",
}