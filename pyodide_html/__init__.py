from textwrap import dedent

try:
    import js
except ImportError:
    print(
        "Unable to import 'js'. This module will not work without pyodide. Make sure you are importing this inside pyodide and try again."
    )

    def js():
        return "js"

    js.document = lambda: "document"
    js.document.createElement = lambda x: (lambda y: "element")


def __to_camel_case(snake_str):
    components = snake_str.split("_")
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + "".join(x.title() for x in components[1:])


def build_element(tag):
    """
    Builds an element from a tag name.
    """

    def add_method(self, *children, **props):
        props = {__to_camel_case(k): v for k, v in props.items()}

        for key, value in props.items():
            setattr(self, key, value)

        self.append(*children)

        return self

    def initial_add(*children, **props):
        ele = js.document.createElement(tag)
        ele.add = add_method.__get__(ele, ele.__class__)

        return ele.add(*children, **props)

    initial_add.__name__ = tag
    initial_add.__qualname__ = tag
    initial_add.__doc__ = dedent(
        f"""
        Creates the '{tag}' HTML element. It's equivalent to calling  '<{tag} **props>*children</{tag}>'.
        Values in `**props` will be converted from 'snake_case' to 'camelCase'.
        For more information, please visit: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/{tag}
        """
    )

    return initial_add


def __create_tags():
    accepted_tags = (
        "head link meta style title body "
        # content sectioning
        "address article aside footer header h1 h2 h3 h4 h5 h6 main nav section "
        # text content
        "blockquote dd div dl dt figcaption figure hr li ol p pre table ul "
        # inline text semantics
        "a abbr b bdi bdo br cite code data dfn em i kbd mark q rp rt ruby s samp small span strong sub sup time u var wbr "
        # image and multimedia
        "area audio img map track video "
        # embedded content
        "embed iframe object param picture portal source "
        # svg and mathML
        "svg math "
        # scripting
        "canvas noscript script "
        # demarcating edits
        "del ins "
        # table content
        "caption col colgroup table tbody td tfoot th thead tr "
        # forms
        "button datalist fieldset form input label legend meter optgroup option output progress select textarea "
        # interactive elements
        "details dialog menu summary "
        # web components
        "slot template "
    )

    for tag in accepted_tags.strip().split():
        ele = build_element(tag)
        globals()[tag] = ele


__create_tags()
