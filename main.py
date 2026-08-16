from textual.app import App, ComposeResult
from textual.widgets import Footer, Header
# https://textual.textualize.io/widget_gallery/

# The App class is where most of the logic of Textual apps is written.
# It is responsible for loading configuration, setting up widgets, handling keys, and more.
class ToDoApp(App):
    """A TODO.txt manager, with vim motions"""
    BINDINGS = [
        ("j", "navigate_down", "Down"),
        ("k", "navigate_up", "Up"),
        ("q", "quit_app", "Quit"),
        ("t", "toggle_dark", "Dark mode"),
        ("p", "focus_projects", "Projects"),
        ("c", "focus_context", "Context")
    ]

    def compose(self) -> ComposeResult:
        """Create child widget for the app"""
        yield Header(icon = "󰄵")
        yield Footer(show_command_palette=False)

    def on_mount(self) -> None:
        self.title = "2do | <placeholder>"
        self.sub_title = "TODO.txt manager"

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode"""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

if __name__ == "__main__":
    app = ToDoApp()
    app.run()
