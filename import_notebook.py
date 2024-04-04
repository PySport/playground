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
            "%pip install requests\n",
            "# Patch requests to make it work in the browser\n",
            "import pyodide_http\n",
            "pyodide_http.patch_all()",
        ]
    },
    {
        "cell_type": "code",
        "source": [
            "%pip install mplsoccer==1.1.12 highlight_text pandas"
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

    # Bumpy Charts
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/d1fdddca141f1aab0658d2d5b234b69e/plot_bumpy.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Bumpy Charts/Bumpy Charts.ipynb"
    ),

    # Pitches
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/64fb4aa390d9f6a43bd388461652f4dc/plot_animation.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Animation.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/d080dd87dd64b093179dff1a558d673e/plot_convex_hull.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Convex Hull.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/3bbe3fd973b50cdb1850d1e4af2ee609/plot_cmap.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Customize colormaps.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/774edea0a398240e65010f4f8dad89dd/plot_cyberpunk.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Cyberpunk theme.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/f13637ec8d87dd2aa6ae03e2b51db961/plot_kde.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Event distribution using kdeplot.ipynb"
    ),

    # NOT WORKING
    # NotebookImport(
    #     url="https://mplsoccer.readthedocs.io/en/latest/_downloads/17c5396ce3776b4a79e934f176506330/plot_fbref.ipynb",
    #     prepend_cells=MPLSOCCER_PREPEND_CELLS,
    #     destination_filename="content/mplsoccer_/Pitches/FBRef Pressure.ipynb"
    # ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/762cafeba876a8c59dc776e2d8dc88ab/plot_grid.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Grid.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/e8683151f194be858d6f02006bb60eac/plot_heatmap.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Heatmap.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/474440d1e2ce835d8f04213e435abf1f/plot_heatmap_positional.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Heatmap Juego de Posición.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/6c75c4a9df0ebb0762325f91ab15d98a/plot_hexbin.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Hexbin plot.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/13f9324ebbf3559a01523772246e6ab6/plot_jointgrid.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Jointgrid.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/b5dd7d59985569f0bc51075b0da56436/plot_pass_network.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Pass Network.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/dcd5f1d4b5998de1876889c31cf68c65/plot_flow.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Pass flow plot.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/e2c124156f827895a57a8ff299e1f823/plot_arrows.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Pass plot using arrrows.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/131b55c53c442f0d01110c77c5293b9a/plot_lines.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Pass plot using lines.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/99090b5c450a39b72ef1b767b15bc5fd/plot_photo.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Photos.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/38762a4d6b50cf3928f0ad232c0c465c/plot_delaunay.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Plots Delaunay Tessellation of Players.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/3853088cdf80d16218241d886eff7c42/plot_voronoi.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Plots a Voronoi diagram.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/c5a5ebfbb89f573fdc5240e619e1b6c0/plot_scatter.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Scatter.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/8b856c3b60cb92f1af8560498afd7eec/plot_shot_freeze_frame.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Shot freeze frame.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/6170511ad10324635804f9309213fce6/plot_standardize.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Standardize data.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/62f5666b7ac6c47e651696277f8bf572/plot_sb360_frame.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/StatsBomb 360.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/c1ba5b3be03934e69ef5d431690704bf/plot_textured_background.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Textured background.ipynb"
    ),
    NotebookImport(
        url="https://mplsoccer.readthedocs.io/en/latest/_downloads/c92cd2de3d1ed404648ae74511d8f5df/plot_twitter_powerpoint.ipynb",
        prepend_cells=MPLSOCCER_PREPEND_CELLS,
        destination_filename="content/mplsoccer_/Pitches/Twitter and Powerpoint friendly.ipynb"
    ),
]


def fix_github_urls(code):
    """
    FROM: https://github.com/googlefonts/SourceSerifProGFVersion/blob/main/fonts/SourceSerifPro-Regular.ttf?raw=true
    TO: https://raw.githubusercontent.com/googlefonts/SourceSerifProGFVersion/main/fonts/SourceSerifPro-Regular.ttf
    """

    # Fix broken font
    code = code.replace(
        "FontManager()",
        "FontManager('https://raw.githubusercontent.com/googlefonts/roboto/main/src/hinted/Roboto-Regular.ttf')"
    )

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
    filename = import_job.destination_filename.replace(" ", "_")
    if not os.path.exists(filename):
        data = requests.get(import_job.url)
        notebook = data.json()
        notebook['cells'] = replace_url(
            import_job.prepend_cells + notebook['cells'],
            import_job.url
        )

        dir_name = os.path.dirname(filename)
        os.makedirs(dir_name, exist_ok=True)

        with open(filename, 'w') as fp:
            json.dump(notebook, fp, indent=2)


if __name__ == "__main__":
    for notebook in notebooks:
        import_notebook(notebook)
