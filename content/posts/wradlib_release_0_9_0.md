Title: Release 0.9.0
Date: 2016-08-31 13:00
Category: news
Authors: wradlib
Tags: releases, github, python2, python3
---

With this post, we announce the release of wradlib 0.9.0. This release finalizes our transition 
from example Python scripts to jupyter notebooks (as already announced in a 
[previous post](http://wradlib.org/2016/04/introducing-wradlib-jupyter-notebooks/) ). As a result, 
the documentation pages have become more consistent, and the handling of examples and tutorials 
more convenient and interactive. We hope you agree!

As a consequence, the previous doc sections "Tutorials" and "Recipes" have been replaced by one single 
section [Tutorials and Examples](http://wradlib.org/wradlib-docs/latest/notebooks.html). 
The pages in that section were automatically built from jupyter 
(IPython) notebooks. These notebooks are distributed with the [new release](https://pypi.python.org/pypi/wradlib), 
and you can use them to interactively browse through our tutorials and examples. You can always download the latest notebooks 
from the [wradlib repository](https://github.com/wradlib/wradlib/tree/master/notebooks).

For those who do not know, yet, how to handle jupyter notebooks, we prepared a 
[quick tutorial](http://wradlib.org/wradlib-docs/latest/jupyter.html). We also added a 
brief (and certainly incomplete) [intro to Python](http://wradlib.org/wradlib-docs/latest/notebooks/learnpython.html) 
for those who would like to have some entry point to that language. This intro will certainly further be developed 
in the future.

In case you don't want to use notebooks: straight Python scripts are distributed alongside the notebooks with [each new release > 0.9.0](https://pypi.python.org/pypi/wradlib).

Please note another important change: we moved all the example data from the main
[wradlib repository](https://github.com/wradlib/wradlib/) to a new [data repository](https://github.com/wradlib/wradlib-data).
You need to download the example data archive yourself, and extract it to any directory on your computer. Then you need to create
an environment variable pointing to that directory. After that, the example notebooks the data will automagically pull the required
example data from that directory. See [here](http://wradlib.org/wradlib-docs/latest/jupyter.html#how-can-i-get-the-example-data) for more detailed guidance on the process.   

Along with wradlib 0.9.0, we also released a couple of minor, though hopefully useful new features and fixes, e.g.:

- `wradlib.io.read_RADOLAN_composite` can now read the new radolan [FZ product](https://github.com/wradlib/wradlib/pull/73),
- `wradlib.io.readDX` can now read gzipped DX data,
- `wradlib.io.read_Rainbow` was enhanced to read product pixmap data from rainbow5 files,
- fixed [incompatibility issue with scipy 0.18.0](https://github.com/wradlib/wradlib/issues/86),
- and fixed some other issues.

For more details on the new release, please visit our [release notes](http://wradlib.org/wradlib-docs/0.9.0/).

Are you wondering how to update to the new wradlib version? If you installed wradlib with `conda install wradlib` 
(in a virtual environment named e.g. `wradlib` on top of Anaconda), you just need to

```shell

$ activate wradlib
$ conda update wradlib

```

See our [installation instruction](http://wradlib.org/wradlib-docs/0.9.0/gettingstarted.html) in case you need more info. 
In case you forgot the name of the virtual environment, you can use

```shell

$ conda --info envs

```


 