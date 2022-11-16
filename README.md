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
4. The py and ipynb files both are using Python version 3.9.12

Libraries needed for the Python program to run.

pip install matplotlib
pip install pandas
pip install notebook

The py and ipynb files both are using Python version 3.9.12

The project file: https://github.com/timothy7walker/NBA-s-Top-Scorers/blob/main/TimothyWalkerNBA.ipynb

* I recommend using Google Collaborator to view the project notebook:
Google Collaborator does not require Anaconda application install.
1. Go to Google Collaborator: https://colab.research.google.com/?utm_source=scs-index
2. Click on the File menu at the top of Collaborator and click 'Open notebook.' 
3. A menu options window will open. At the top of the menu window click the 'GitHub' tab.
4. Steps to setup a virtual environment:
    a) Clone or download the repository project file from Github to your computer. 
       Project address:
       https://github.com/timothy7walker/GalaxyPlanetsandExoplanets.git
    b) From the command prompt go to the file directory where the download or clone project is located.
    c) To create a virtual environment, we can use the Python venv library. Type this into your terminal or cmd:
       python -m venv env
    d) A virtual environment directory will be setup inside the downloaded file directory.
       to get to this directory type this in the command prompt: cd env/bin/activate.bat
    c) The virtual environment is now active. Run the Python project file by typing this command into the command prompt:
       python galaxyplanetsandexoplanets.py
5. A Notebook file called GalaxyPlanetsandExoplanets.ipynb will run the project from a Google collaborate. The Notebook 
   file includes markup explaining each line of Python code. The Notebook fill will also install the main packages needed to run the project.

This project was setup on Python 3.9.7

Project file name: GalaxyPlanetsandExoplanets.ipynb
Project web location link: https://github.com/timothy7walker/GalaxyPlanetsandExoplanets

******I recommend using Google Collaborator to view the project notebook:
******Google Collaborator: https://colab.research.google.com/?utm_source=scs-index

Other ways to view the project:

Install Jupiter Notebook to view .ipynb files.
Go to https://jupyter.org/install:
Jupyter Notebook
Install the classic Jupyter Notebook with:

pip install notebook
To run the notebook:

jupyter notebook

The Anaconda application can also be installed to view the project. 
Anaconda includes the Jupitor Notebook application along with pandas, matplotlib, numpy, and seaborn libraries 
needed to run this project.
Download Anaconda from: https://www.anaconda.com/
