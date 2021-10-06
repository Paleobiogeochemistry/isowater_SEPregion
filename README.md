# isowater_SEPregion
This repository aim to storage the python scripts and data set used for the paper titled Isotopic characterization of water masses in the Eastern South Pacific Ocean: Paleoceanography implications 
# (Under Construction)

# BOT (Bottom water computation)

To determine the theoretical bottom water characteristics on top of the sediment cores sites, we propose a simple finder script. From an hydrological data base organized in ODV software is possible to estimate it.

![GC_MUC_sediment_model](https://user-images.githubusercontent.com/57748370/113622334-231a8e80-965d-11eb-977d-943e565c5e71.png)

## Prerequisites

- Instal or use Ocean Data View software https://odv.awi.de/ or other program that allow you to obtained gridded interpolation plots (eg. surface, matlab, python, R). In this exercise we will use ODV. 
- Instal or use text file manager (eg. note ++, Excel). 
- Hydrological data set organize for be readed in ODV software 
- Create a special folder for your data 


## Getting started




### First Step for OVD users 

Download the latest version of ODV in https://odv.awi.de/software/download/ 

- Organize your data using the Ocean Data View (ODV) data template (excel file example). Excel file example (Please not delete the first row items, you can add new columns after the parameter “depth [m]”) https://drive.google.com/file/d/1ZyONN1T7nXM2F6SS73UdqvW5-ooHM6aB/view?usp=drive_open 
- The excel file with your data needs to be exported as a text file (preference format cvs)
- Import from ODV the txt file 
- Organize the data by meridional o zonal hydrological section 
- Use the tool **clipboard copy (right bottom, option Extra) type export grilled filled values with tabulations** were used. The full grilled data was a copy in an excel file, edited the first line taking care to avoid text space and saved in txt separated with tabulations or in comma-separated csv. For futher information use https://odv.awi.de/fileadmin/user_upload/odv/misc/odv4Guide.pdf 

### Second Step (data-sediments)...

#### Determination of relative bottom water characteristics at the surface sediment sites

With the goal of finding the relative bottom water hydrological characteristics from the grilled hydrological interpolations (explained in point 1) in top of surface sediments collected in the South-East Pacific, a python script was developed. 

**Step 1.** Install Python (recommendable last edition) https://www.python.org/ 

**Step 2.** Create in your PC a single folder for each hydrological parameter (eg. one specific folder for oxygen, temperature, salinity). In that folder, add 

i) the hydrological parameter grilled text file obtained previously in Ocean Data View (example file format, https://drive.google.com/open?id=1DU3xOgopRsxX4oWs65YJ8nyRAoMPxk-9) 

ii) the station’s text file (example file format https://drive.google.com/open?id=1usasObWq-_4XA57hb3dHwZay6TwVpQc2) and the 

iii) python script. Remember that the name of the files needs to be simple and without spaces.  


### Third Step (Script-Python)...



## Example ...






## Authors

* **Dharma Reyes** - *MARUM Research, University of Bremen, Germany* 

* **Pablo Santamarina** - [*Innovex Tecnologías (Ltd.)*](www.innovex.cl)*, Chile*

* **Rodrigo Troncoso** - *Arturo Prat University, Iquique, Chile*



### Collaborators

> **Dharma Reyes** - *MARUM Institute, University of Bremen, Germany* - [dreyesmacaya@marum.de]

> **Pablo Santamarina** - *Innovex (Ltd.), Chile*

> **Rodrigo Troncoso** - *Arturo Prat University, Iquique, Chile*



See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
