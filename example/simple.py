from aqwebengine import AQWebEngineView
from aqwebengine.run import run

from PyQt5.QtWidgets import QShortcut, QMainWindow


async def main():
    w = AQWebEngineView()
    await w.init()

    m = QMainWindow()
    m.setCentralWidget(w)

    shortcut = QShortcut('CTRL+Q', w, activated=m.close)

    await w.set_html_async('Hello, world!')
    m.show()

    return locals()  # prevents our GUI objects from being garbage-collected


run(main(), app_arguments=['--single-process', '--disable-web-security', '--remote-debugging-port=9999', '--enable-logging'])
