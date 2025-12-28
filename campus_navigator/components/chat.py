import reflex as rx
from ..state import State
from ..styles import glass_style, ACCENT_COLOR
def chat_bubble(message: tuple[str, str]):
    """Display a single chat message."""
    sender = message[0]
    text = message[1]
    is_user = sender == "User"
    return rx.box(
        rx.text(text, color=rx.cond(is_user, "white", "black")),
        padding="10px",
        border_radius="10px",
        background_color=rx.cond(is_user, ACCENT_COLOR, "white"),
        align_self=rx.cond(is_user, "flex-end", "flex-start"),
        margin_bottom="10px",
        max_width="80%",
    )
def chat_component():
    return rx.vstack(
        rx.scroll_area(
            rx.vstack(
                rx.foreach(State.chat_history, chat_bubble),
                align_items="stretch",
                width="100%",
            ),
            height="300px",
            width="100%",
            padding="10px",
        ),
        rx.hstack(
            rx.input(
                placeholder="Ask for directions...",
                value=State.input_text,
                on_change=State.set_input_text,
                style=glass_style,
                color="white",
                width="100%",
            ),
            rx.button(
                "Send",
                on_click=State.handle_submit,
                bg=ACCENT_COLOR,
                color="white",
            ),
            width="100%",
            padding_top="10px",
        ),
        style=glass_style,
        padding="20px",
        width="100%",
        max_width="400px",
    )