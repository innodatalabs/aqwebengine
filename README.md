# aqwebengine

Qt QWebEngine on `async` steroids:

* `async` versions of methods to load URL and set page html
* `async` versions of methods to get page content as HTML and plain text
* `async` method to call python from JS
* `async` method to call JS from Python

Uses [qasync](https://pypi.org/project/qasync/) as an engine to run PyQt/PySide2 asyncronously.

## Examples

```
w = AQWebEngine()
...
await w.set_html_async('<b>Hello</b>, world!')
...
await w.load('https://www.example.com')
...
html = await w.to_html_async()  # get current page as HTML
...
text = await w.to_plain_text()  # get current page as plain text
...
await w.eval_js('function inc(x) { return x + 1; }')
result = await w.eval_js('inc(41)')
assert result == 42
...
def do_something(x):
    return x + 1
w.register_python_function('do_something', do_something)
result = await w.eval_js('qt.callPython("do_something", 41)')
assert result == 42
```

## Python API

### `eval_js`
Asynchronously evaluates the string argument as a JS expression.
Returns result to the Python caller. JSError is raised if evaluation of JS expression throws an exception.

## JS API

### `callPython`
Calls python host.

Parameters:
* `function_name` - the name of the registered python function
* (optional) `args` - any JSON-serializable value

Python function may return JSON-serializable value, that will be returned to the JS caller.