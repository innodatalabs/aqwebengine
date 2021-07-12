import os
from aqwebengine import AQWebEngineView
from aqwebengine.run import run


async def main():
    w = AQWebEngineView()
    await w.init()

    url = 'file://' + os.path.abspath('./example/sample-app/public/index.html')
    await w.load_async(url)

    w.show()


run(main(), app_arguments=['--single-process', '--disable-web-security', '--remote-debugging-port=9999', '--enable-logging'])
