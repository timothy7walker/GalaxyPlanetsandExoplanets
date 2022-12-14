##pip install -r requirements.txt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

##The data file "exoplanet.Archive.csv" was created from a data file downloaded from the NASA Exoplanet Archive @  http://exoplanetarchive.ipac.caltech.edu. The "exoplanet.Archive.csv" only includes the csv data and excludes the notes and data 
##column header definition index. The size of the data is 3815 rows (exoplanets) and 19 columns (exoplanets characteristics).


planetArch = pd.read_csv("exoplanetArchive.csv")
print(planetArch.shape)

##Preview of the exoplanet list. 
##Index of column header definitions:
##Refer to Readme.md

planetArch.head(5)

##The unused column data removed to condense the list information size."""

planetArch2 = planetArch.drop(columns = ["pl_orbper","pl_orbpererr1", "pl_orbpererr2","pl_orbpererr2","pl_orbperlim","pl_radeerr1","pl_radeerr2","pl_radelim","pl_eqt","pl_eqterr1","pl_eqterr2","pl_eqtlim","sy_disterr1","sy_disterr2"])
planetArch2.head()

##This is the list of current columns left in the data frame."""

planetArch2.columns

##The current column labels are renamed for clarity."""

fixed_columns = {'pl_name' : 'Planet Name', 'hostname' : 'Host Star', 'sy_snum' : 'Number of Stars', 'sy_pnum' : 'Number of Planets',
                 'pl_rade' : 'Radius (x Earth Radius)', 'sy_dist' : 'Distance from Earth (pc)'}

##All the exoplanet columns are renamed for better clarity of what the column values represent."""

planetArch2.rename(columns=fixed_columns, inplace=True)
planetArch2

##Seaborn plot of all exoplanets distance from earth in parsec (1pc = 3.262 lightyears) on the x axis. Radius of the exoplanet times the earth radius, number of other planets in the exoplanets system (hue), and the number of stars in the exoplanets system (size)."""

sns.relplot(data = planetArch2, x="Distance from Earth (pc)", y="Radius (x Earth Radius)", hue="Number of Planets", size="Number of Stars", palette="deep")

##The remaining data columns for analysis will be the Planet ('Planet Name'), system star ('Host Star'), number of stars in the planetary system ('Number of Stars'), and the number of planets in the system ('Number of Planets'). This data will be merged with the Earth's solar system data."""

planetArch3 = planetArch2.drop(columns = ["Radius (x Earth Radius)","Distance from Earth (pc)"])
planetArch3

##This is the Earth's solar system data, obtain from Kaggle.com: https://www.kaggle.com/datasets/iamsouravbanerjee/planet-dataset
##The cvs dataset is read in as 8 rows for the 8 planets in our solar system and 22 columns with characteristics of each planet. The characteristic column headers are clear in what the characteristic means.


ourSystem = pd.read_csv("planets.csv") 
ourSystem.shape
ourSystem

##This is a Solar System planets, including Earth, plot based on the distance from the Sun (x-axis), Mean temperature (y-axis), Diameter (km) as the hue, and the planet Mass (10^24kg) as the size."""

sns.relplot(data = ourSystem, x="Distance from Sun (10^6 km)", y="Mean Temperature (C)", hue="Diameter (km)", size="Mass (10^24kg)", palette="deep")

##The solar system data is condensed down to only the "Planet",	"Diameter (km)", "Distance from Sun (10^6 km)", "Orbital Period (days)", and "Mean Temperature (C)" columns."""

ourSystem2 = ourSystem.drop(columns = ["Color","Mass (10^24kg)","Density (kg/m^3)","Surface Gravity(m/s^2)","Escape Velocity (km/s)",
                         "Rotation Period (hours)","Length of Day (hours)","Orbital Velocity (km/s)","Orbital Inclination (degrees)",
                         "Orbital Eccentricity","Obliquity to Orbit (degrees)","Surface Pressure (bars)","Number of Moons","Ring System?",
                         "Perihelion (10^6 km)","Aphelion (10^6 km)","Global Magnetic Field?"])
ourSystem2

##The "Planet" column is renamed to "Planet Name"."""

fixed_columns2 = {'Planet' : 'Planet Name'}
ourSystem2.rename(columns=fixed_columns2, inplace=True)
ourSystem2

##In order to merge to solar system data (ourSystem2) and the exoplanet data (planetArch3), we are going to make each data set
##have the same column heading parameters of "Planet", "Host Star", "Number of Stars", and "Number of Planets".
##Two new columns are created for the planets.csv data to with sun and total planet data.

ourSystem2['Host Star'] = 'Sun'
ourSystem2['Number of Stars'] = 1
ourSystem2['Number of Planets'] = 8

ourSystem2

##The remaining unneeded columns ("Diameter (km)","Distance from Sun (10^6 km)","Orbital Period (days)","Mean Temperature (C)") are removed from the solar system data set (ourSystem2)."""

ourSystem3 = ourSystem2.drop(columns = ["Diameter (km)","Distance from Sun (10^6 km)","Orbital Period (days)","Mean Temperature (C)"])
ourSystem3

##The solar system data (ourSystem3) and the exoplanet data (planetArch3) are combined into one data set with the same columns:
##Planet Name",	"Host Star", "Number of Stars",	and "Number of Planets".

newPlanetList = pd.concat([planetArch3, ourSystem3], sort=False)
newPlanetList

##A seaborn plot of all planets and exoplanets with the number of planets in the planet's system on the x axis, the number of stars in the planet's system on the y axis, the total number of planets in the planet's system (hue), and the total number of stars in the planet's system (size)."""

sns.relplot(data=newPlanetList, x="Number of Planets", y="Number of Stars", hue="Number of Planets", size="Number of Stars", palette="deep")

##Panda table displaying number of planet in a 1,2,3, or 4 star system."""

graphStar = newPlanetList.groupby('Number of Stars')[['Number of Planets']].count()
graphStar

length = [1,2,3,4]
data = graphStar['Number of Planets']
plt.xticks(range(len(data)), length)
plt.xlabel('Number of Stars in the system')
plt.ylabel('Number of Planets')
plt.title('Planetary systems')
plt.bar(range(len(data)), data) 
plt.show()

##Panda tables displaying the number of star systems with 1,2,3,4,5,6,7, or 8 planets."""

graphStar2 = newPlanetList.groupby('Number of Planets')[['Number of Stars']].count()
graphStar2

length2 = [1,2,3,4,5,6,7,8]
data2 = graphStar2['Number of Stars']
plt.xticks(range(len(data2)), length2)
plt.xlabel('Number of Planets in the System')
plt.ylabel('Number of System')
plt.title('Planetary systems ')
plt.bar(range(len(data2)), data2) 
plt.show()