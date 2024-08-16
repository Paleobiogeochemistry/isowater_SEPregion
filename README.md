# isowater_SEPregion 

This repository aims to store the python script and data set used for the paper titled “Isotopic characterization of water masses in the Eastern South Pacific Ocean: Paleoceanography implications”

Paper available in (https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021JC017525) 

Data set available in https://doi.pangaea.de/10.1594/PANGAEA.940085 and https://github.com/Paleobiogeochemistry/BOT/tree/main  

## Motivation and scientific goals 

This study aims to hydrologically characterize the water masses of the Southeast Pacific (SEP), from surface (Subtropical Water, STW and Subantarctic Water, SAAW), subsurface (Equatorial Subsurface Water, ESSW), intermediate (Antarctic Intermediate Water, AAIW) and finally deep waters (Pacific Deep Water, PDW).
To achieve this we use seawater oxygen, deuterium, dissolved inorganic carbon isotopes in combination with temperature, salinity, oxygen and nutrient concentrations along a coastal (71-78 °W) and an oceanic (82-98 °W) transect in the Southeast Pacific. 
The data set integrates published and new measurements collected between 1992 and 2018. We hope that the database, the scripts and the manuscript can promote the idea of using oceanographic data near to the sediment core sites to have accurate modern-analogs to a better understanding of past changes in water mass chemistry and geometry in the Southeast Pacific. This is relevant especially in coastal zones where continental and oceanic processes merge in a unique dynamic which is passing to the sediment record. 

As a group we are continuing sampling sea water in the SEP for stable isotope analysis with the goals of:  

i) Improve the data cover by water masses.
ii) Understand temporal variation of the stable isotope signatures of water masses.
iii) Integrate oceanographic data to understand changes of the tracers in long-term scales.
iv) Provide to the paleoceanography community a hydrological data set to be used as a modern-analog that can be permanently curated. 

![sampleinformation_project_10152021](https://user-images.githubusercontent.com/80867539/137465439-521b4d6f-07bf-4467-9a0c-314c1632b932.png)

Figure: Location of hydrological sites that our team are currently working on [coloured dots refer to the individual expeditions]. The code developed for this specific publication only can be runed by transects. Features indicated are main ocean currents, oceanographic fronts and the Antarctic Intermediate Water (AAIW) formation zone in the Southeast Pacific. Peru-Chile or Humboldt Current (PCC), Peru-Chile Counter Current (PCCC), Peru-Chile Undercurrent (PCUC), Equatorial Undercurrent (EUC), South Equatorial Current (SEC), Subantarctic Front (SAF) and Subtropical Front (STF). In the data collection, the stations of expeditions P19-P06, SO211 and TABASCO correspond to published data from the project *[*GLODAP v2*](https://www.glodap.info/)*, *[*Martinez-Mendez et al., 2013*](https://agupubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1002/palo.20047?__cf_chl_jschl_tk__=pmd_qLivIu5GB8dsCMRtLVPENswsh0sAP06fW2SAWA46ayc-1634291777-0-gqNtZGzNAiWjcnBszQjR)* and [*Pakulski et al., 2007*](https://www.researchgate.net/publication/250220274_Responses_of_heterotrophic_bacteria_to_solar_irradiance_in_the_eastern_Pacific_Ocean) respectively. 

## New data set that will be uploaded in 2022-2024

- New seawater samples are available to be analyzed from the following locations in Chile: Mejillones, Coquimbo, Reloncavi Fjord, Chilean Patagonia. 
- New projects as [*CLAP*](https://futureoceanslab.org/clap/) from CEAZA and the UK-Chile project [*NERC-Disentangling the Genotype Paleoproxy Challenge in the Humboldt Current System and Beyond*] will continue sampling seawater for stable isotopes in the region. 

## Consideration using isowater_SEPregion python code 

The python code that is stored in this project was specifically developed to be used in the creation of Reyes-Macaya et al., (submitted). With the content of this project it is possible to obtain any of the plots and statistical analysis shown in the main text and supplementary information of the paper. With minor modifications the code can be applicable for any oceanographic zone of the Earth with any data cloud. 

## Main products that the code offers 

The code provides the execution of several statistical analyses and representation of data in plots from the coastal and oceanic section by water masses organized by their percentage of contribution in the water mixture. A detailed list of the analysis is listed here: 

- Histograms for chemical parameters: temperature, salinity, oxygen, nutrients. 
- Histograms for stable isotope parameters: oxygen, deuterium, carbon isotopes of the Dissolved inorganic carbon (DIC) and carbon isotope sea-air exchange signatures. 
- Mann Whitney test by water comparing isotopic signatures: oxygen, deuterium, carbon isotopes of the Dissolved inorganic carbon (DIC). 
- Computation of carbon isotope sea-air exchange effect corrected by phosphate (Broecker and Maier-Reimer, 1992) or apparent oxygen utilization (Keir et al., 1998). 
- Linear regression between isotopic signatures (oxygen, deuterium, carbon DIC) versus salinity in the oceanic section
- Linear regression between isotopic signatures (oxygen, deuterium, carbon DIC) versus salinity in the coastal section

## Execute isowater_SEPregion python code

When this code is executed in the terminal, it will ask the user if they want to manually select what to do. Otherwise it will use the code preconfiguration and do everything. 

Example: 

Do you want to manually select what to do? y/n  y

Do you want to make chemical histograms?  y/n  y

## Prerequisites

- Instal python https://www.python.org/downloads/ 
- Instal python libraries (download the file called *test* from the isowater_SEPregion file list to check if you have all the necessary libraries for running the code in your PC)
- Hydrological data set organized with the format (latitude or longitude, depth, hydrological variable, water mass percentage A, B, C, D, E) (download the file called *dd_coastal.boat*)

Example

Latitude	Depth	dD	ESSW	AAIW	PDW	STW	SAAW

## Data management and script developers 

* **Dharma Andrea Reyes Macaya** - [dharmareyes@gmail.com] Marine Biogeochemist 
* **Francisco Manuel García Araya** - [garcicia@gmail.com] Earth Scientist and Big Data Management  

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
* - [*Departamento de Oceanografía, Universidad de Concepción*](http://oceanografia.udec.cl/)*, Chile*
* - [*Departamento de Sistemas Acuáticos, Universidad de Concepción*](http://www.eula.cl/investigacion/unidad-de-sistemas-acuaticos/)*, Chile*
* - [*Escuela de Ciencias del Mar, Pontificia Universidad Católica de Valparaíso](http://www.cienciasdelmar.pucv.cl/)*, Chile*
* - [*MARUM - Zentrum für Marine Umweltwissenschaften der Universität Bremen*](https://www.marum.de/en/about-us/Marine-Sedimentology/Team-3.html)*, Germany*
* - [*AWI﹣Alfred Wegener-Institut Helmholtz-Zentrum für Polar- und Meeresforschung*](https://www.awi.de/en/)*, Germany*
* - [*German Centre for Integrative Biodiversity Research (iDiv), Halle﹣Jena﹣Leipzig*](https://www.idiv.de/en/index.html)*, Germany*
* - [*GEOMAR﹣Helmholtz Centre for Ocean Research Kiel*](https://www.geomar.de/en/news/article/ocean-circulation-and-climate-dynamics)*, Germany*
* - [*Sonderforschungsbereich 754 - Climate – Biogeochemistry Interactions in the Tropical Ocean*](http://www.sfb754.de)*, Germany*
* - [*Museum für Naturkunde, Leibniz Institute for Evolution and Biodiversity Science*](https://www.leibniz-gemeinschaft.de/en/institutes/leibniz-institutes-all-lists/museum-fuer-naturkunde-leibniz-institute-for-evolution-and-biodiversity-science)*, Germany*
* - [*Department of Earth Sciences, Freie Universität Berlin*](https://www.geo.fu-berlin.de/en/index.html)*, Germany*
* - [*Lyell Centre, Heriot-Watt University*](http://www.lyellcentre.ac.uk/)*, UK*
* - [*FARGO - FAte of ocean oxygenation in a waRminG wOrld*](http://www.lyellcentre.ac.uk/)*, UK*
* - [*National Environmental Isotope Facility, British Geological Survey*](http://www.isotopesuk.org/)*, UK*
* - [*School of Biosciences, University of Nottingham*](https://www.nottingham.ac.uk/biosciences/)*, UK*
* - [*COAS﹣College of Earth, Ocean, and Atmospheric Sciences, Oregon State University*](https://ceoas.oregonstate.edu/)*, USA*
* - [*Woods Hole Oceanographic Institution*](https://www.whoi.edu/)*, USA*
* - [*Scripps Institution of Oceanography*](https://scripps.ucsd.edu/)*, USA*
* - [*Stazione Zoologica Anton Dohrn*](http://www.szn.it/index.php/en/)*, Italy*
* - [*Observatoire Océanologique, de Banyuls sur Mer*](https://www.obs-banyuls.fr/en/)*, France*

