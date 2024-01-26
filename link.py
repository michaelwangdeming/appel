import theme
from message import message

from nicegui import APIRouter, ui

router = APIRouter(prefix='/link')


@router.page('/')
def example_page():
    with theme.frame('链接'):
        message('有用的链接')
        ui.link('观看通关视频', "https://gameappel.github.io/res/introduce.mp4").classes('text-xl text-grey-8')
        ui.link('下载桌面版', "https://gameappel.github.io/pack/AppelSetup.exe").classes('text-xl text-grey-8')
        ui.link('项目主页', "https://github.com/GameAppel/GameAppel.github.io").classes('text-xl text-grey-8')
