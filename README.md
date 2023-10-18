# Young Star Confirmed Exoplanets

## Project Overview

This project is a part of a larger team effort for the course "Introducción a la Computación" of the Astrophysics Master's program at Universidad de la Laguna. We aim to identify young stars, specifically those less than a certain age, with confirmed transiting exoplanets. Our analysis relies on data from the NASA Exoplanet Archive database.

After identifying young host stars with confirmed transiting exoplanets, we then use the lightkurve library to retrieve their lightcurves. We first check if the lightcurves are available and analyze their cadences to ensure that they are suitable for further analysis. We then create a dataset with this information, which includes the mission, number of results, target name, and exposure time of each lightcurve. Finally, we download the lightcurves in a structured way and save them to a folder for further analysis. This process allows us to obtain a dataset of lightcurves for young host stars that can be used for various scientific analyses.



## Description
This repository contains work in progress for an analysis of young stars with confirmed transiting exoplanets. We're focusing on young stars due to their high level of variability, which has significant implications for exoplanet detection and characterization.

1. Open the Jupyter notebook counting_young_exo_with_error.ipynb to view the analysis.
2. Run the cells to generate plots and figures, which will be saved in the figures folder.
3. Results, such as young star data, will be saved in the results folder.
The repository also includes the following files:

- `identify_young_stars.ipynb`: A Jupyter notebook that identifies young host stars with confirmed transiting exoplanets using data from the NASA Exoplanet Archive database.
- `create_lk_dataset.ipynb`: A Jupyter notebook that uses the lightkurve Python library to search for and download lightcurves of young host stars.
- `utils.py`: Contains various utility functions that assist in data manipulation and calculations.
- ``plot_utils.py``: Houses functions specifically designed for plotting and visualization.

These files are essential for the analysis of young stars with confirmed transiting exoplanets and provide a framework for further scientific research.

## Status

This project is currently under active development. Expect frequent updates and refer to the Issues section for upcoming features, known bugs, or tasks up for grabs.

## Author Contributions

This repository has been possible thanks to the contributions of David Mirabal, Urma González, Iris Ortega, Carlota Mendez, Guillermo Villa, Cathaysa Perdomo, Álvaro García, María Helena Rivero, Daniel García, y Pere Rosselló.
