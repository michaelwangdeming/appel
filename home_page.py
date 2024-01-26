from nicegui import ui

description = """
# ![](https://gameappel.github.io/res/Title.svg)
- 😂使用方向键或 WASD 进行奔跑、跳跃和蹲下、沿墙跳跃 - 触碰墙壁并按下“上”键,长按上键可以跳得更高
- 😜沿天花板移动 - 长按上键 - 但要小心，当“黏”在表面上时无法横向移动、长按下键蹲下（你可以在地面、墙壁和天花板上蹲下！）
- 😉按下 Q + R 键可以快速重新开始关卡
"""
def content() -> None:
    ui.markdown(description)

