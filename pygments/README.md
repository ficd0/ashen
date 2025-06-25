# Pygments Ashen

This repository contains the Pygments style plugin for the
[Ashen](https://sr.ht/~ficd/ashen) theme. Available as the `pygments-ashen`
package on [PyPI](https://pypi.org/project/pygments-ashen/) for use in your
Python projects, or with the Pygments CLI tool. The actual name of the _style_
within `pygments` is `ashen`.

## How To Use

The following shows how to use the style with `uv`, which is currently the
cleanest way to manage Python projects and libraries. You may, of course,
install the package into a virtual environment with `pip`, if you wish:

```sh
pip install pygments-ashen
```

### Pygments CLI

Third-party Pygments styles are Python packages that must be available in the
environment `pygments` is running in. For example, you can use `uv` to create a
one-off environment for a single command:

```sh
uv run --with 'pygments-ashen,pygments' \
pygmentize -O full,style=ashen \
-l python -f html foobar.py > foobar.html
```

The above command invokes `pygmentize` with the `pygments-ashen` and `pygments`
dependencies available, and renders the file `foobar.py` in HTML format with the
Ashen theme applied.

### In Your Projects

If your project uses Pygments for code highlighting, you can easily add support
for Ashen. The `pygments-ashen` package must be installed in the project
environment:

```sh
uv add pygments-ashen
```

Then, you can use `ashen` as the `style` in Pygments formatters. Here's an
example from Zona. This code renders a Markdown code block in HTML with Ashen
highlighting, using the `marko` library:

```python
# method part of subclass of marko.html_renderer.HTMLRenderer
@override
def render_fenced_code(self, element: FencedCode):
    # pygments expects a single string, not a list of lines
    code = "".join(child.children for child in element.children)
    # fallback to "text" if no language specified
    lang = element.lang or "text"

    # load the correct pygments lexer
    try:
        lexer = get_lexer_by_name(lang, stripall=False)
    except Exception:
        lexer = TextLexer(stripall=False)

    # use the "ashen" style, requires pygments-ashen package
    formatter = HtmlFormatter(style="ashen", nowrap=True, noclasses=True)
    # highlight the code
    highlighted = highlight(code, lexer, formatter)

    # return rendered code block
    return (
        f'<pre class="code-block language-{lang}">'
        f"<code>{highlighted}</code></pre>"
    )
```
