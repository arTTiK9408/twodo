from typing import override

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header


# NOTE https://textual.textualize.io/tutorial
# NOTE https://textual.textualize.io/widget_gallery/
# The App class is where most of the logic of Textual apps is written.
# It is responsible for loading configuration, setting up widgets, handling keys, and more.
class TwoDo(App[None]):
    """A TODO.txt manager, with vim motions"""

    BINDINGS = [  # noqa: RUF012
        ("j", "navigate_down", "down"),
        ("k", "navigate_up", "up"),
        ("q", "quit_app", "quit"),
        ("t", "toggle_dark", "dark mode"),
        ("p", "focus_projects", "projects"),
        ("c", "focus_context", "contexts"),
    ]

    @override
    def compose(self) -> ComposeResult:
        """Create child widget for the app"""
        yield Header(icon="󰄵")  # TODO: add nerd font requirement check
        yield Footer(show_command_palette=False)

    def on_mount(self) -> None:
        self.title = "TwoDo | <placeholder>"
        self.sub_title = "TODO.txt manager"

    @override
    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode"""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = TwoDo()
    app.run()
