from aqwebengine import AQWebEngineView
import pytest
import asyncio


@pytest.mark.qasync
async def test_call_python():
    '''Test that JS can call Python host'''
    w = AQWebEngineView()
    await w.init()

    f = asyncio.Future()
    async def handler(value):
        f.set_result(value)

    w.register_python_function('test_func', handler)

    w.page().runJavaScript('qt.callPython("test_func", 42);')

    await f

    assert f.result() == 42


@pytest.mark.qasync
async def test_eval_js():
    '''Test that Python can call JS guest'''
    w = AQWebEngineView()
    await w.init()

    w.page().runJavaScript('function inc(x) { return x + 1; }')

    result = await w.eval_js('''inc(41)''')

    assert result == 42


@pytest.mark.qasync
async def test_round_trip():
    '''Test that JS can call Python host'''
    w = AQWebEngineView()
    await w.init()

    async def handler(value):
        result = await w.eval_js(f'{value} + 1')
        return result + 1

    w.register_python_function('test_func', handler)

    result = await w.eval_js('qt.callPython("test_func", 40);')

    assert result == 42
