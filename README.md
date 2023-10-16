# Young Star Confirmed Exoplanets

## Description

This repository contains work in progress for an analysis of young stars with confirmed transiting exoplanets, using data from the Exoplanet.eu database. We're focusing on young stars due to their high level of variability and the implications this has for exoplanet detection and characterization. We utilize data from the ExoplanetEU and NASA Exoplanet Archive and employ Python for data analysis and visualization.


## Usage

1. Open the Jupyter notebook `counting_young_exo_with_error.ipynb` to view the analysis.
2. Run the cells to generate plots and figures, which will be saved in the `figures` folder.
3. Results, such as young star data, will be saved in the `results` folder.

## Folder Structure

\```
.
├── .gitignore
├── README.md 
├── code
│   ├── counting_young_exo_with_error.ipynb
│   └── utils.py
│   └── plot_utils.py
├── data
│   └── database_NASA.votable
├── figures
│   └── various_plot_images.png
└── results
    └── young_stars_below_100Myr.txt
\```

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Status

This project is currently under active development. Expect frequent updates, and please refer to the Issues section for upcoming features, known bugs, or tasks up for grabs.