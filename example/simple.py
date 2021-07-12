from aqwebengine import AQWebEngineView
from aqwebengine.run import run


async def main():
    w = AQWebEngineView()
    await w.init()

    await w.set_html_async('Hello, world!')
    w.show()


run(main(), app_arguments=['--single-process', '--disable-web-security', '--remote-debugging-port=9999', '--enable-logging'])
