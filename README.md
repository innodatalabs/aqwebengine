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

### register_python_function
Registeres a python (sync or async) function to be callable from JS (see qt.callPython JS API below).

Python function should take a single JSON-serializable parameter.

Arguments:
* `function_name` - the name of the function, as seen by JS
* `function` - python function. Can be sync or async, should take a single JSON-serializable argument.

## JS API

### `qt.callPython`
Calls python host.

Arguments:
* `function_name` - the name of the registered python function
* (optional) `args` - any JSON-serializable value

Python function may return JSON-serializable value, that will be returned to the JS caller.
