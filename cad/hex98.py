import io

import nbformat
from IPython.core.interactiveshell import InteractiveShell


def exec_ipynb(path):
    from IPython import get_ipython  # pyright: ignore

    shell = InteractiveShell.instance()

    # load the notebook object
    with io.open(path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, 4)

    for cell in nb.cells:
        if cell.cell_type == "code":
            # transform the input to executable Python
            code = shell.input_transformer_manager.transform_cell(cell.source)
            exec(code)


def build():
    exec_ipynb("hex98.ipynb")
