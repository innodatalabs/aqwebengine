import os
from aqwebengine import AQWebEngineView, async_slot
from aqwebengine.run import run
from aqwebengine.qtx import QPushButton, QVBoxLayout, QWidget


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self._l = QVBoxLayout()
        self.setLayout(self._l)

        self._w = AQWebEngineView(self)
        self._l.addWidget(self._w)

        self._b = QPushButton('hitme')
        self._l.addWidget(self._b)

        self._b.clicked.connect(async_slot(self.loadme))

    async def init(self):
        await self._w.init()

    async def loadme(self, *_):
        url = as_file_url('./example/sample-app/public/index.html')
        print(url)
        await self._w.load_async(url)

async def main():
    w = Main()
    await w.init()

    w.resize(800, 600)
    w.show()

def as_file_url(fname):
    p = os.path.abspath(fname).replace('\\', '/')
    if not p.startswith('/'):
        p = '/' + p
    return 'file://' + p




run(main(), app_arguments=['--single-process', '--disable-web-security', '--remote-debugging-port=9999', '--enable-logging'])
