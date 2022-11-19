from textual.app import ComposeResult
from textual.widgets import Static, Input, Button
from textual.containers import Horizontal


class Welcome(Static):
    DEFAULT_CSS = """
    Screen {
        layout: vertical;
        background: #111827;
        scrollbar-background: #111827;
        scrollbar-color: #6366f1;
        content-align: center middle;
    }

    .header {
        height: 5;
        margin-top: 2;
        color: #6366f1;
        content-align: center middle;
        text-style: underline;
    }

    .tagline {
        border: round #6366f1;
        height: 5;
        max-width: 100%;
        content-align: center middle;
        margin: 0 4;
    }

    .label {
        margin-top: 2;
        content-align: center middle;
    }

    #server {
        width: 100%;
        margin: 2 40;
        content-align: center middle;
        border: tall #111827;
        background: #1f2937;
    }

    #server:focus {
        border: tall #7c3aed;
    }

    #signup {
        width: 100%;
        margin: 2 40;
        background: #7c3aed;
        border: tall #7c3aed;
    }

    #signup_link {
        link-color: #6366f1;
        link-style: bold italic underline;
        content-align: center middle;
        margin: 1 0;
    }

    #signup_link:hover {
        link-background: #6366f1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("Welcome to Textodon!", classes="header")
        yield Static(
            "Textodon is a mastodon client that let's you toot from a terminal.",
            classes="tagline",
        )
        yield Static("Enter your username to get started:", classes="label")
        yield Input(placeholder="@RatulMaharaj@fosstodon.org", id="server")
        yield Button("Sign In", id="signup", classes="signup")
        yield Static(
            "No account? Sign up now at [@click=set_background('#6366f1')]https://joinmastodon.org/[/]",
            id="signup_link",
        )
