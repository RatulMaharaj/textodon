from textual.app import App, ComposeResult
from welcome import Welcome


class Textodon(App):
    def compose(self) -> ComposeResult:
        yield Welcome()


if __name__ == "__main__":
    app = Textodon()
    app.run()
