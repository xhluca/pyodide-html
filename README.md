# Pyodide HTML

HTML elements for `pyodide`, implemented as Python functions.

## Quickstart

```python
import micropip

micropip.install('pyodide-html')

import pyodide_html as html

ele = html.h1('Hello, world!')

js.document.body.appendChild(ele)
```

## Motivation

In `pyodide`, you can create HTML elements using `js.document`, but it is extremely verbose. For example, a range input would look like:
```python
import js

ele = js.document.createElement('input')
ele.type = 'range'
ele.min = 0
ele.max = 50
ele.value = 25
ele.step = 1
```

With `pyodide_html`, you can do all this with a single function call:
```python
import pyodide_html as html

ele = html.input(type="range", min=0, max=50, value=25, step=1)
```

## Usage

All the [HTML tags](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) are implemented as Python functions. For example, `html.h1` creates a `<h1>` element, `html.input` creates an `<input>` element, and so on.

The signature of the function is:
```python
html.element(*children, **props)
```

which is equivalent to calling `<element **props>*children</element>`.

Every element has an `add` method that lets you add new, or update existing children or props. It has the following signature:
```python
html.element(*children, **props).add(*children, **props)
```

This is convenient if you want to initialize an element with certain `props`, then add/update the `children` or `props` later using `add`. For example:

```python
import pyodide_html as html

# initialize your element
ele = html.div(className="container")

# Add children
ele.add(
    html.h1("My header"),
    html.p("Some paragraph here"),
    # ...
)

# You can add new props:
ele.add(style="background-color: lightgray")

# You can also update existing props:
ele.add(style="background-color: lightblue")
```

You can also chain `add` calls:
```python
ele.add(style="...").add(className="...").add(html.div("a child"))
```

Note that `add` modifies an element in-place.

## Documentation

See [REFERENCE.txt](./REFERENCE.txt) ([GitHub Link](https://github.com/xhlulu/pyodide-html/blob/main/REFERENCE.txt)) for the API reference.

## Contributing/Development

After cloning this repo, start with:
```
pip install -r dev-requirements.txt
```

You can then make the desired changes