# isowater_SEPregion (Underconstruction) 

This repository aim to storage the python scripts and data set used for the paper titled Isotopic characterization of water masses in the Eastern South Pacific Ocean: Paleoceanography implications 

**The paper is available in (xxWebpageofthejournalxx when will be published) 
**The data set is available in (xxpangaeaxx)

# Motivation and scientific goals 

This study aim to hydrologically characterized the water masses of the Southeast Pacific (SEP), going from surface (Subtropical Water, STW and Subantarctic Water, SAAW), to subsurface (Equatorial Subsurface Water, ESSW), intermediate (Antarctic Intermediate Water, AAIW) and finally deep waters (Pacific Deep Water, PDW).
To achieve this we use seawater oxygen, deuterium, dissolved inorganic carbon isotopes in combination with temperature, salinity, oxygen and nutrient concentrations along a coastal (71-78 °W) and an oceanic (82-98 °W) transect in the Eastern South Pacific. 
The data set integrate published and new measurements collected between 1992 and 2018. We hope that the data base, the scripts and the manuscript can promote the idea of use oceanographic data near to the sediment core sites for have accurate modern-analogs to impruve the interpretation of past changes in water mass chemistry and geometry in the Eastern South Pacific. This is relevat specially in coastal zones where continental and oceanographic processes merge in a unique dinamic which is passing to the fossil record. 

As a group we are continue sampling sea water in the SEP for stable isotopes analysis to help: 

i) impruve the cover of data by water masses 
ii) understand temporal variation of the stable isotope signatures of water masses
iii) integrate oceanographic data to understand changes of the tracers in long-term scales 

## Consideration using isowater_SEPregion python code 

The python code that is storage in this project was specifically develop to be used in the creation of Reyes-Macaya et al., (submitted). With the content of this project is possible to obtein any of the plots and stadistical analysis showed in the main text and suplementary information of the paper. With minor modifications the code can be applicable for any oceanographic zone of the Earth with any data cloud. 

## Main products that the code offer 

The code provide the execution of several stadistical analysis and representation of data in plots from the coastal and oceanic section by water masses organized by their porcentage of contribution in the water mixture. A detail list of the analysis is listed here: 

- Histograms for chemical parameters: temperature, salinity, oxygen, nutrients. 
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

## Prerequisites

- Instal python 3 
- Instal python libraries (downloand the file called test from the isowater_SEPregion file list to check if you have all the necesary libraries for run the code in your PC)
- Hydrological data set organize with the format (latitude or longitude, depth, hidrological variable, water mass percentage A, B, C, D, E) 

Example

Latitude	Depth	dD	ESSW	AAIW	PDW	STW	SAAW

## Data managment and script developers 

* **Francisco Manuel García Araya** - [garcicia@gmail.com] Earth Scientist and Big Data Managment  
* **Dharma Andrea Reyes Macaya** - [dharmareyes@gmail.com] Marine Biogeochemist 

## Authors  

Dharma Reyes﹣Macaya, Babette Hoogakker, Gema Martínez﹣Méndez, Pedro J. Llanillo, Mahyar Mohtadi, Patricia Grasse, Alan Mix, Melanie J Leng, Ulrich Struck, Daniel C. McCorkle, Macarena Troncoso, Eugenia M Gayo, Laura Farias, Carina B. Lange, Wilson Carhuapoma, Michelle Graco, Marcela Cornejo﹣D’Ottone, Ricardo De Pol Holz, Camila Fernandez, Diego Narvaez, Cristian A. Vargas, Francisco M. García - Araya, Dierk Hebbeln. 

## Research Institutions and Funding Projects 

* - [*IMARPE - Instituto del Mar del Perú*](https://www.gob.pe/imarpe)*, Perú*
* - [*Nucleo Milenio UPWELL -  Millennium Science Initiative Program*](http://www.upwell.cl/eng/humboldt-biogeochemistry/)*, Chile*
* - [*COPAS Sur-Austral, Research Line 5*](http://www.sur-austral.cl/)*, Chile*
* - [*Instituto Milenio de Oceanografía - Millennium Science Initiative Program*](https://en.imo-chile.cl/)*, Chile*
* - [*Centro IDEAL - Centro de Investigación de Dinámica en Ecosistemas Marinos en Altas Latitudes*](https://www.centroideal.cl/)*, Chile*
* - [*Centro de Investigación GAIA-Antártica (CIGA)*](http://www.umag.cl/gaiaantartica/?lang=en)*, Chile
* - [*Centro de Ciencia del Clima y Resiliencia*](https://www.cr2.cl/)*, Chile*
* - [*Instituto Milenio en Socio-Ecología Costera (SECOS) - Millennium Science Initiative Program*](https://socioecologiacostera.cl/en/), Chile*
* - [*Departamento de Oceanografia, Universidad de Concepción*](http://oceanografia.udec.cl/)*, Chile*
* - [*Departamento de Sistemas Acuáticos, Universidad de Concepción*](http://www.eula.cl/investigacion/unidad-de-sistemas-acuaticos/)*, Chile*
* - [*Escuela de Ciencias del Mar, Pontificia Universidad Católica de Valparaíso](http://www.cienciasdelmar.pucv.cl/)*, Chile*
* - [*MARUM - Zentrum für Marine Umweltwissenschaften der Universität Bremen*](https://www.marum.de/en/about-us/Marine-Sedimentology/Team-3.html)*, Germany*
* - [*AWI﹣Alfred Wegener-Institut Helmholtz-Zentrum für Polar- und Meeresforschung*](https://www.awi.de/en/)*, Germany*
* - [*German Centre for Integrative Biodiversity Research (iDiv), Halle﹣Jena﹣Leipzig*](https://www.idiv.de/en/index.html)*, Germany*
* - [*GEOMAR﹣Helmholtz Centre for Ocean Research Kiel*](https://www.geomar.de/en/news/article/ocean-circulation-and-climate-dynamics)*, Germany*
* - [*Sonderforschungsbereich 754 - Climate – Biogeochemistry Interactions in the Tropical Ocean*](http://www.sfb754.de)*, Germany*
* - [*Museum für Naturkunde, Leibniz Institute for Evolution and Biodiversity Science*](https://www.leibniz-gemeinschaft.de/en/institutes/leibniz-institutes-all-lists/museum-fuer-naturkunde-leibniz-institute-for-evolution-and-biodiversity-science)*, Germany*
* - [*Department of Earth Sciences, Freie Universität Berlin*](https://www.geo.fu-berlin.de/en/index.html)*, Germany*
* - [*Lyell Centre, Heriot-Watt Univeristy*](http://www.lyellcentre.ac.uk/)*, UK*
* - [*FARGO - FAte of ocean oxygenation in a waRminG wOrld*](http://www.lyellcentre.ac.uk/)*, UK*
* - [*National Environmental Isotope Facility, British Geological Survey*](http://www.isotopesuk.org/)*, UK*
* - [*School of Biosciences, University of Nottingham*](https://www.nottingham.ac.uk/biosciences/)*, UK*
* - [*COAS﹣College of Earth, Ocean, and Atmospheric Sciences, Oregon State University*](https://ceoas.oregonstate.edu/)*, USA*
* - [*Woods Hole Oceanographic Institution*](https://www.whoi.edu/)*, USA*
* - [*Scripps Institution of Oceanography*](https://scripps.ucsd.edu/)*, USA*
* - [*Stazione Zoologica Anton Dohrn*](http://www.szn.it/index.php/en/)*, Italy*
* - [*Observatoire Océanologique, de Banyuls sur Mer*](https://www.obs-banyuls.fr/en/)*, France*
