import theme
from message import message

from nicegui import APIRouter, ui
from theme import game_list
router = APIRouter(prefix='/15')


@router.page('/')
def example_page():
    with theme.frame('游戏 1-5'):
        message('😉选择一个游戏!')
        for i in range(1, 6):
            with ui.row():
                ui.link(f'{i} {game_list[i-1]}', f'/15/list/{game_list[i-1]}').classes('text-xl text-grey-8')


@router.page('/list/{id}', dark=False)
def game(id: str):
    with theme.frame(f'- {id} -'):
        message(f'Play {id}')
        web=f"https://gameappel.github.io/games/{id}.html"
        ui.link('Play', web).classes('text-xl text-grey-8')
        ui.link('Go Back', router.prefix).classes('text-xl text-grey-8')
