Title: easy install using conda-forge
Date: 2016-03-17 15:00
Category: wradlib
Authors: wradlib
Tags: conda, windows, osx, linux, python
---

With the help of the outstanding community effort named [conda-forge](https://conda-forge.github.io/) wradlib can now be installed within the major OSs _**linux**_, _**windows**_ and _**osx**_.

Until now, installing wradlib and its dependencies can sometimes be a real mess, especially on windows. But also in linux dependency issues are well known.

Using the so-called [conda-forge/wradlib-feedstock](https://github.com/conda-forge/wradlib-feedstock) installable wradlib packages for each of the three OS (also accounting for different python and numpy versions) are generated. For windows also 32bit-packages are available. All built packages are tested and uploaded to the [conda-forge channel](https://anaconda.org/conda-forge/wradlib).

The default-conda channel provides many wradlib dependencies out of the box, but not all. Hence, we also contributed to the [conda-forge/gdal-feedstock](https://github.com/conda-forge/gdal-feedstock) making it the first feedstock serving two different package versions (gdal 1.11.4 and 2.0.2).

With these prerequisites wradlib can be **easy** installed using the [conda package manager](http://conda.pydata.org/docs/intro.html).

1. install the [Anaconda environment of your choice](https://www.continuum.io/downloads)

2. clone the root environment or create one from scratch

        :::bash
        $ conda create --name wradlib --clone root
        or
        $ conda create --name wradlib python=2.7

3. add the conda-forge channel

        :::bash
        $ conda config --add channels conda-forge

4. activate wradlib environment

    * Linux

            :::bash
            $ source activate wradlib

    * Windows

            :::bash
            > activate wradlib

5. install wradlib (and dependencies)

        :::bash
        (wradlib) $ conda install wradlib

6. set GDAL_DATA environment variable (needed for georeferencing)

    * Linux/OSX bash

            :::bash
            (wradlib) $ export GDAL_DATA=/path/to/anaconda/envs/wradlib/share/gdal

    * Windows CMD.exe

            :::bash
            [wradlib] > setx GDAL_DATA C:\path\to\anaconda\envs\wradlib\Library\share\gdal

7. optional dependencies can be installed OS independent with `pip`

        :::bash
        (wradlib) $ pip install xmltodict

* * *

With this on all three OS very straightforward procedure, with the excellent [Anaconda](https://www.continuum.io/why-anaconda) from Continuum(R) and the sustainable conda-forge community effort wradlib usability reaches new heights.





