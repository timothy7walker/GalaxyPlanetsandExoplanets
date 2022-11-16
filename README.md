# GalaxyPlanetsandExoplanets
 Code Louisville Data 2 Final Project
 The Galaxy Planets ad Exoplanets project analyzes data from a file produced by the NASA Exoplanet Archive  http://exoplanetarchive.ipac.caltech.edu. This file includes exoplanet data online. A copy of the raw data file downloaded from the NASA Exoplanet Archive  http://exoplanetarchive.ipac.caltech.edu is PSCompPars_2022.11.03_17.07.58.csv and has been included in the GalaxyPlanetsandExoplanets archive. The file contains index information about the column categories and what they mean:

# COLUMN pl_name:        Planet Name
# COLUMN hostname:       Host Name
# COLUMN sy_snum:        Number of Stars
# COLUMN sy_pnum:        Number of Planets
# COLUMN pl_orbper:      Orbital Period [days]
# COLUMN pl_orbpererr1:  Orbital Period Upper Unc. [days]
# COLUMN pl_orbpererr2:  Orbital Period Lower Unc. [days]
# COLUMN pl_orbperlim:   Orbital Period Limit Flag
# COLUMN pl_rade:        Planet Radius [Earth Radius]
# COLUMN pl_radeerr1:    Planet Radius Upper Unc. [Earth Radius]
# COLUMN pl_radeerr2:    Planet Radius Lower Unc. [Earth Radius]
# COLUMN pl_radelim:     Planet Radius Limit Flag
# COLUMN pl_eqt:         Equilibrium Temperature [K]
# COLUMN pl_eqterr1:     Equilibrium Temperature Upper Unc. [K]
# COLUMN pl_eqterr2:     Equilibrium Temperature Lower Unc. [K]
# COLUMN pl_eqtlim:      Equilibrium Temperature Limit Flag
# COLUMN sy_dist:        Distance [pc]
# COLUMN sy_disterr1:    Distance [pc] Upper Unc
# COLUMN sy_disterr2:    Distance [pc] Lower Unc

Dictionary table of contents for PSCompPars_2022.11.03_17.07.58.csv and edited exoplanetArchive.csv file used in this project.


![Alt text](GalaxyPlanetsandExoplanets\System Composition Data.jpg)
![Alt text](GalaxyPlanetsandExoplanets\System Composition Data 1.jpg)
![Alt text](GalaxyPlanetsandExoplanets\System Composition Data 2.jpg)
![Alt text](GalaxyPlanetsandExoplanets\System Composition Data 3.jpg)
![Alt text](GalaxyPlanetsandExoplanets\System Composition Data 4.jpg)

Project Feature list:
1. Two different csv datasets are read into the program.
2. The 2 datasets (exoplanetArchive.csv and planets.csv) are cleaned by deleting uneeded column data and renaming the column headings to easily understood heading titles. The two data sets are merge after each dataset are cleaned to have the same heading titles that can be 
merged into 1 data set with all the same column headings.
3. There are a total of 5 data plots, including 3 seaborn scatterplots from the exoplanetArchive.csv data set, a scatterplot of the Solar System dataset (planets.csv), and a scatterplot of the exoplanetArchive.csv and planets.csv combined dataset. There are 2 matplotlib bar graphs, including 1 bar graph of the total number of exoplanets with 1,2,3,4 stars in the system, and 1 bar chart with the total number of planets in 1,2,3,4,5,6,7,8 planets sytems.
4.