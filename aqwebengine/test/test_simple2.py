from aqwebengine import AQWebEngineView, async_slot
from aqwebengine.qtx import Signal, QObject
import pytest
import asyncio
import tempfile
import os


@pytest.mark.qasync
async def test_set_html_async():
    '''Test that HTML can be read asynchronously'''
    w = AQWebEngineView()
    await w.init()
    await w.set_html_async('Hello')
    html = await w.to_html_async()
    assert html == '<html><head></head><body>Hello</body></html>'

    await w.set_html_async('Hello, <b>world</b>')
    text = await w.to_plain_text_async()
    assert text == 'Hello, world'


@pytest.mark.qasync
async def test_load_async():
    '''Test that URL can be read asynchronously'''
    w = AQWebEngineView()
    await w.init()

    with tempfile.TemporaryDirectory() as td:
        fname = f'{td}/index.html'
        with open(fname, 'w') as f:
            f.write('<b>Hello, world!</b>')
        await w.load_async('file://' + os.path.abspath(fname))

        html = await w.to_html_async()
        assert html == '<html><head></head><body><b>Hello, world!</b></body></html>'

        text = await w.to_plain_text_async()
        assert text == 'Hello, world!'


@pytest.mark.qasync
async def test_async_slot():
    '''Test that Qt signalls can be connected to async functions with async_slot'''
    class Signaller(QObject):
        signal = Signal(int)

    s = Signaller()

    f = asyncio.Future()
    @async_slot
    async def slot(result):
        f.set_result(result)

    s.signal.connect(slot)
    s.signal.emit(2)

    await f
    assert f.result() == 2