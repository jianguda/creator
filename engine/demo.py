import pyxel

from engine.common import Area, Loader


class App:
    win = Area(256, 256)
    scenes = Loader.load(win)
    tab_idx, tab_len = 0, len(scenes)
    topology = scenes[tab_idx]

    def __init__(self):
        pyxel.init(App.win.w, App.win.h)
        pyxel.run(self.update, self.draw)

    @staticmethod
    def update():
        if pyxel.btnr(pyxel.KEY_TAB):
            App.tab_idx = (App.tab_idx + 1) % App.tab_len
            App.topology = App.scenes[App.tab_idx]
        if pyxel.btnp(pyxel.KEY_SPACE, 0, 1):
            App.topology.show()

    @staticmethod
    def draw():
        pyxel.cls(0)
        App.topology.draw(pyxel)


App()
