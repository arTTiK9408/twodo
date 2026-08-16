from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

class TwoDoApp(App):
    """A TODO.txt manager, with vim motions"""
    BINDINGS = [
        ("j", "navigate_down", "Down"),
        ("k", "navigate_up", "Up"),
        ("q", "quit_app", "Quit"),
        ("t", "toggle_dark", "Dark mode")
    ]

    def compose(self) -> ComposeResult:
        """Create child widget for the app"""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode"""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

if __name__ == "__main__":
    app = TwoDoApp()
    app.run()
