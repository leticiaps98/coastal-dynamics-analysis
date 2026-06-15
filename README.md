# Coastal Dynamics and Sand Dune Analysis

This repository contains Python scripts used for the geoprocessing and morphodynamic analysis of coastal environments, developed as part of a Master's thesis in Geography. It provides an open-source, automated alternative for calculating shoreline change metrics and evaluating the impact of urban expansion on frontal dune systems.

## Features

* **Shoreline Morphodynamics (`shoreline_dynamics.py`)**: 
  * Automated generation of perpendicular transects from a coastal baseline.
  * Calculation of **End Point Rate (EPR)** and **Linear Regression Rate (LRR)** to quantify coastal erosion and accretion without depending on proprietary GIS extensions (like DSAS).
* **Coastal Squeeze Analysis (`coastal_squeeze_analysis.py`)**: 
  * Evaluation of the morphodynamic decoupling between the beach face and the dune system.
  * Geospatial data visualization of the inverse correlation between urban area expansion and the retraction of frontal dune sediment stocks.

## Technologies Used

* **Python 3**
* **GeoPandas & Shapely**: Advanced spatial intersections and geometry operations.
* **SciPy**: Statistical regressions and confidence metrics.
* **Matplotlib**: Dual-axis plotting and data visualization.

## Context

These scripts were applied to the morphodynamic assessment of Mar Grosso Beach (Rio Grande do Sul, Brazil), processing decades of satellite imagery and demonstrating the occurrence of the *Coastal Squeeze* phenomenon.
