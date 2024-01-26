import theme
from message import message

from nicegui import APIRouter, ui
from theme import game_list
router = APIRouter(prefix='/1619')


@router.page('/')
def example_page():
    with theme.frame('游戏 16-19'):
        message('😉选择一个游戏!')
        for i in range(16, 19):
            with ui.row():
                ui.link(f'{i} {game_list[i-1]}', f'/1619/list/{game_list[i-1]}').classes('text-xl text-grey-8')


@router.page('/list/{id}')
def game(id: str):
    with theme.frame(f'- {id} -'):
        message(f'Play {id}')
        web=f"https://gameappel.github.io/games/{id}.html"
        ui.link('Play', web).classes('text-xl text-grey-8')
        ui.link('Go Back', router.prefix).classes('text-xl text-grey-8')
