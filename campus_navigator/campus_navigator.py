import reflex as rx
from .state import State
from .components.map_wrapper import map_component
from .components.chat import chat_component
from .styles import base_style, glass_style, ACCENT_COLOR
def index() -> rx.Component:
    return rx.box(
        # Background Map
        rx.box(
            map_component(),
            width="100vw",
            height="100vh",
            position="absolute",
            top="0",
            left="0",
            z_index="0",
        ),
        
        # Overlay Content
        rx.vstack(
            # Header
            rx.box(
                rx.heading("Campus Navigator", color=ACCENT_COLOR, font_size="2em"),
                rx.text("AI-Powered Navigation", color="white"),
                style=glass_style,
                padding="20px",
                margin_top="20px",
                margin_left="20px",
                pointer_events="auto",
            ),
            
            rx.spacer(),
            
            # Chat Interface
            rx.box(
                chat_component(),
                margin_bottom="20px",
                margin_left="20px",
                pointer_events="auto",
            ),
            
            height="100vh",
            padding="20px",
            position="relative",
            z_index="10",
            pointer_events="none", # Let clicks pass through to map where not covered
        ),
    )
app = rx.App(style=base_style)
app.add_page(index)