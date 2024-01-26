from contextlib import contextmanager

from menu import menu

from nicegui import ui

game_list = ["Appel Game",
             "Rainbow Appel",
             "Space Appel ",
             "Minecraft Appel",
             "Party Appel ",
             "Desert Appel",
             "Candy Appel",
             "AmongUs Appel",
             "Heat Appel",
             "Heat2 Appel",
             "Difficult Appel",
             "Volcano Appel",
             "Lemon Appel",
             "Getting Over",
             "Volcano Appel",
             "White Appel",
             "Multiplayer Appel",
             "3D Appel"
             ]


@contextmanager
def frame(navtitle: str):
    """Custom page frame to share the same styling and behavior across all pages"""
    ui.colors(primary='#f2b007', secondary='#53B689', accent='#111B1E', positive='#ff9933')
    with ui.header().classes('justify-between text-white'):
        ui.label('Appel 游戏').classes('font-bold')
        ui.label(navtitle)
        with ui.row():
            menu()
    with ui.column().classes('absolute-center items-center'):
        yield
