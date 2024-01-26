#!/usr/bin/env python3

import game_loading15
import game_loading610
import game_loading1115
import game_loading1619

import link
import home_page
import theme

from nicegui import app, ui

@ui.page('/')
def index_page() -> None:
    with theme.frame('主页'):
        home_page.content()


def start():
    app.include_router(game_loading15.router)
    app.include_router(game_loading610.router)
    app.include_router(game_loading1115.router)
    app.include_router(game_loading1619.router)
    app.include_router(link.router)
    app.native.window_args['resizable'] = True

    ui.run(title='Appel Game', native=True, window_size=(720, 540), fullscreen=False)

if __name__=="__main__":
    start()