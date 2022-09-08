import json
import os.path
import re
from dataclasses import dataclass
from typing import List

import requests


@dataclass
class NotebookImport:
    url: str
    prepend_cells: List[dict]
    destination_filename: str


MPLSOCCER_PREPEND_CELLS = [
    {
        "cell_type": "markdown",
        "source": [
            "## *Setup required for Playground*\n",
            "\n",
            "The online playground requires a little bit of code to run first."
        ]
    },
    {
        "cell_type": "code",
        "source": [
            "import micropip\n",
            "await micropip.install('pyodide-http')\n",
            "await micropip.install('mplsoccer')\n",
            "await micropip.install('highlight_text')\n",
            "await micropip.install('pandas')\n",
            "await micropip.install('requests')\n",
            "\n",
            "import pyodide_http\n",
            "pyodide_http.patch_all()"
        ]
    },
    {
        "cell_type": "markdown",
        "source": [
            "Original notebook can be found [here](%URL%)"
        ]
    }
]

notebooks = [
    # Radar Charts
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/5fa8e8f5d40b355b46cf461a103e017b/plot_radar.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Radar Charts/Radar Charts.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/7ac4a0df587f1bd47b8fc0e32a075cab/plot_turbine.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Radar Charts/Turbine Charts.ipynb"
    ),

    # Pizza Plots
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/0b16c024a559a55e94e57b24ecda605b/plot_pizza_basic.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pizza Plots/Basic Pizza Plot (Percentiles).ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/c2106d1fdd9ac69205bfc17a93df37b4/plot_pizza_colorful.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pizza Plots/Colorful Pizza (Percentiles).ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/85545abab4375813e2accc6fb5922856/plot_pizza_comparison.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pizza Plots/Comparison Pizza (Percentiles).ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/e0006fa41e6fe557f5fecf7bfecc7b51/plot_pizza_comparison_vary_scales.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pizza Plots/Comparison Pizza (scales vary).ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/ae815be842e8c446d525f74cbf497cfe/plot_pizza_dark_theme.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pizza Plots/Dark Theme Pizza (Percentiles).ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/cb487bab89c573a3366f030fc1627e2a/plot_pizza_scales_vary.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pizza Plots/Different Scales Pizza.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/525aa9d6d399a75c6ac8c0a4bd828a5c/plot_pizza_different_units.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pizza Plots/Different Units Pizza.ipynb"
    ),
]


def fix_github_urls(code):
    """
    FROM: https://github.com/googlefonts/SourceSerifProGFVersion/blob/main/fonts/SourceSerifPro-Regular.ttf?raw=true
    TO: https://raw.githubusercontent.com/googlefonts/SourceSerifProGFVersion/main/fonts/SourceSerifPro-Regular.ttf
    """
    return re.sub(
        r"https://github\.com/([^/]+/[^/]+)/blob/([a-zA-Z0-9.&/?:@\-_=#]+)",
        r"https://raw.githubusercontent.com/\1/\2",
        code
    )


def replace_url(cells, url):
    def fix(cell):
        if cell['cell_type'] == "code":
            return dict(
                cell_type='code',
                execution_count=None,
                metadata=cell.get('metadata', {}),
                outputs=[],
                source=[
                    fix_github_urls(source.replace('%URL%', url)) for source in cell['source']
                ],
            )
        else:
            return dict(
                cell_type=cell['cell_type'],
                metadata=cell.get('metadata', {}),
                source=[
                    fix_github_urls(source.replace('%URL%', url)) for source in cell['source']
                ],
            )

    return [
        fix(cell) for cell in cells
    ]


def import_notebook(import_job: NotebookImport):
    data = requests.get(import_job.url)
    notebook = data.json()
    notebook['cells'] = replace_url(
        import_job.prepend_cells + notebook['cells'],
        import_job.url
    )

    dir_name = os.path.dirname(import_job.destination_filename)
    os.makedirs(dir_name, exist_ok=True)

    with open(import_job.destination_filename, 'w') as fp:
        json.dump(notebook, fp, indent=2)


if __name__ == "__main__":
    for notebook in notebooks:
        import_notebook(notebook)
