# isowater_SEPregion (Underconstruction) 

This repository aim to storage the python scripts and data set used for the paper titled Isotopic characterization of water masses in the Eastern South Pacific Ocean: Paleoceanography implications 

**The paper is available in (xxWebpageofthejournalxx when will be published) 
**The data set is available in (xxpangaeaxx)

# Motivation and scientific goals 

This study aim to hydrologically characterized the water masses of the Southeast Pacific (SEP), going from surface (Subtropical Water, STW and Subantarctic Water, SAAW), to subsurface (Equatorial Subsurface Water, ESSW), intermediate (Antarctic Intermediate Water, AAIW) and finally deep waters (Pacific Deep Water, PDW).
To achieve this we use seawater oxygen, deuterium, dissolved inorganic carbon isotopes in combination with temperature, salinity, oxygen and nutrient concentrations along a coastal (71-78 °W) and an oceanic (82-98 °W) transect in the Eastern South Pacific. 
The data set integrate published and new measurements collected between 1992 and 2018. We hope that the data base, the scripts and the manuscript can promote the idea of use oceanographic data near to the sediment core sites for have accurate modern-analogs to impruve the interpretation of past changes in water mass chemistry and geometry in the Eastern South Pacific. This is relevat specially in coastal zones where continental and oceanographic processes merge in a unique dinamic which is passing to the fossil record. 

As a group we are continue sampling sea water in the region for stable isotopes analysis with the goals i) impruve the cover of data ii) understand temporal variation of the stable isotope signatures of water masses iii) integrate oceanographic data to understand changes of the tracers in long-term scales. 


## Target group for apply python code 

The python code that is storage in this project was specifically develop to be used in the creation of Reyes-Macaya et al., (submitted). With the content of this project is possible to obtein any of the plots and stadistical analysis showed in the main text and suplementary information of the paper. With minor modifications the code can be applicable for any oceanographic zone of the Earth with any data cloud. 

## Main products that the code offer 

The code provide the execution of several stadistical analysis and representation of data in plots from the coastal and oceanic section by water masses organized by their porcentage of contribution in the water mixture. A detail list of the analysis is listed here: 

- Histograms for hidrological parameters: temperature, salinity, oxygen, nutrients. 
- Histograms for stable isotope parameters: oxygen, deuterium, carbon isotopes with carbon isotope sea-air exchange 
- Mann Whitney test by water comparing isotopic signatures (oxygen, deuterium, carbon) 
- Computation of carbon isotope sea-air exchange effect corrected by phosphate (Broecker and Maier-Reimer, 1992) or apparent oxygen utilization (Keir et al., 1998). 
- Linear regresion between isotopic signatures (oxygen, deuterium, carbon) versus salinity in the oceanic section
- Linear regresion between isotopic signatures (oxygen, deuterium, carbon) versus salinity in the coastal section

## Execute isowater_SEPregion python code

When this code is execute in the terminal, it will ask to the user if want manually select what to do. Otherwise it will use the code preconfiguration and do everything. 

Example: 

Do you want to manually select what to do? y/n  s

Do you want to make the chemical histograms?  y/n  s

Do you want to make the isotopic histograms?  y/n  y

Do you want to make the Mann Whitney analysis?  y/n  o



## Prerequisites

- Instal python 3 
- Instal python libraries (downloand the following archive to check if you have all the necesary libraries that will be necesary for run the code in your PC)
- Hydrological data set organize with the following format 

## Getting started
s

## Example ...


## Data managment and script developers 

* **Francisco Manuel García Araya** - [garcicia@gmail.com] Earth Scientist and Big Data Managment  
* **Dharma Andrea Reyes Macaya** - [dharmareyes@gmail.com] Marine Biogeochemist 

## Authors  

Dharma Reyes﹣Macaya, Babette Hoogakker, Gema Martínez﹣Méndez, Pedro J. Llanillo, Mahyar Mohtadi, Patricia Grasse, Alan Mix, Melanie J Leng, Ulrich Struck, Daniel C. McCorkle, Macarena Troncoso, Eugenia M Gayo, Laura Farias, Carina B. Lange, Wilson Carhuapoma, Michelle Graco, Marcela Cornejo﹣D’Ottone, Ricardo De Pol Holz, Camila Fernandez, Diego Narvaez, Cristian A. Vargas, Francisco M. García - Araya, Dierk Hebbeln. 

## Projects and Funding iniciatives 

* - [*MARUM - Zentrum für Marine Umweltwissenschaften der Universität Bremen*](https://www.marum.de/en/about-us/Marine-Sedimentology/Team-3.html)*, Germany*
* - [*FARGO- FAte of ocean oxygenation in a waRminG wOrld*](http://www.lyellcentre.ac.uk/)*, UK*
* - [*Nucleo Milenio UPWELL -  Millennium Science Initiative Program*](http://www.upwell.cl/eng/humboldt-biogeochemistry/)*, Chile*
* - [*Sonderforschungsbereich 754 - Climate – Biogeochemistry Interactions in the Tropical Ocean*](http://www.sfb754.de)*, Germany*
* - [*COPAS Sur-Austral, Research Line 5*](http://www.sur-austral.cl/)*, Chile
* - [*Deparment of Oceanography, Universidad de Concepción*](http://oceanografia.udec.cl/)*, Chile
* - [*Instituto Milenio de Oceanografía - Millennium Science Initiative Program*](https://en.imo-chile.cl/)*, Chile
* - [*Centro IDEAL - Centro de Investigación de Dinámica en Ecosistemas Marinos en Altas Latitudes*](https://www.centroideal.cl/)*, Chile
