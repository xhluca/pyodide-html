import pydoc

import pyodide_html as html


generated = pydoc.render_doc(html, renderer=pydoc.plaintext)
generated = generated.split("\nFILE\n")[0].strip()

with open("REFERENCE.txt", "w") as f:
    f.write(generated)