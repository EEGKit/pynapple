# -*- coding: utf-8 -*-
"""
Fastplotlib
===========

Working with calcium data.

For the example dataset, we will be working with a recording of a freely-moving mouse imaged with a Miniscope (1-photon imaging). The area recorded for this experiment is the postsubiculum - a region that is known to contain head-direction cells, or cells that fire when the animal's head is pointing in a specific direction.

The NWB file for the example is hosted on [OSF](https://osf.io/sbnaw). We show below how to stream it.

See the [documentation](https://pynapple-org.github.io/pynapple/) of Pynapple for instructions on installing the package.

This tutorial was made by Sofia Skromne Carrasco and Guillaume Viejo.

"""
# %%
# !!! warning
#     This tutorial uses seaborn and matplotlib for displaying the figure
#
#     You can install all with `pip install matplotlib seaborn tqdm`
#
# mkdocs_gallery_thumbnail_number = 1
#
# Now, import the necessary libraries:

# %qui qt

import pynapple as nap
import numpy as np
import fastplotlib as fpl

import imageio.v3 as iio
import sys
# mkdocs_gallery_thumbnail_path = '../_static/fastplotlib_demo.png'

#nwb = nap.load_file("/Users/gviejo/pynapple/Mouse32-220101.nwb")
nwb = nap.load_file("your/path/to/MyProject/sub-A2929/A2929-200711/pynapplenwb/A2929-200711.nwb")

units = nwb['units']#.getby_category("location")['adn']

tmp = units.to_tsd()

tmp = np.vstack((tmp.index.values, tmp.values)).T 

# Example 1

fplot = fpl.Plot()

fplot.add_scatter(tmp)

fplot.graphics[0].cmap = "jet" 

fplot.graphics[0].cmap.values = tmp[:, 1]

fplot.show(maintain_aspect=False)

# Example 2

names = [['raster'], ['position']]

grid_plot = fpl.GridPlot(shape=(2, 1), controller_ids="sync", names = names)

grid_plot['raster'].add_scatter(tmp)

grid_plot['position'].add_line(np.vstack((nwb['ry'].t, nwb['ry'].d)).T)

grid_plot.show(maintain_aspect=False)

grid_plot['raster'].auto_scale(maintain_aspect=False)


# Example 3
#frames = iio.imread("/Users/gviejo/pynapple/A0670-221213_filtered.avi")
#frames = frames[:,:,:,0]
frames = np.random.randn(10, 100, 100)

iw = fpl.ImageWidget(frames, cmap="gnuplot2")

#iw.show()

# Example 4 

from PyQt6 import QtWidgets


mainwidget = QtWidgets.QWidget()

hlayout = QtWidgets.QHBoxLayout(mainwidget)

iw.widget.setParent(mainwidget)

hlayout.addWidget(iw.widget)

grid_plot.widget.setParent(mainwidget)

hlayout.addWidget(grid_plot.widget)

mainwidget.show()
