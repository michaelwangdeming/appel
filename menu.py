from nicegui import ui


def menu() -> None:
    ui.link('主页', '/').classes(replace='text-white')
    ui.link('1-5', '/15').classes(replace='text-white')
    ui.link('6-10', '/610').classes(replace='text-white')
    ui.link('11-15', '/1115').classes(replace='text-white')
    ui.link('16-19', '/1619').classes(replace='text-white')
    ui.link('链接','/link').classes(replace='text-white')
    ui.link('旧网址', 'https://gameappel.github.io/').classes(replace='text-white')
