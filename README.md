# hand-flooded_lots
Python script to determine which lots in Austin are at risk of flooding

## Main Python script
`hand-flooded_lots.py` can be run by:
```
python3 hand-flooded_lots.py
```

## Required source data inputs
There are 4 inputs.
* _HAND vector image:_ HAND vector GIS file of a basin in Austin, discretized into polygons of levels
* _[Zoning vector image](https://data.austintexas.gov/Locations-and-Maps/Zoning-Small-Map-Scale-/5rzy-nm5e):_ Austin's zoning vector GIS file, either entirely or a subset covering the basin of choice

## Description of outputs
There are 4 outputs per HUC12.
* _Lots at risk:_
    * lots within basin in Austin that are at risk of flooding
    * selected if there is _any_ intersection with this lot and the HAND levels
    * include an attribute of the least HAND level for which this lot is at risk

Here is an example of these outputs, originally visualized by [Prof David Maidment](https://www.caee.utexas.edu/faculty/directory/maidment).
![Example outputs](https://github.com/dhardestylewis/GeoFlood-preprocessing/blob/master/DEM-HUC12-Outputs_example.jpg)

## Already preprocessed DEMs
Already preprocessed DEMs are now available for the vast majority of Texas's HUC12s if you are a [TACC user](https://portal.tacc.utexas.edu/). You can request a TACC account [here](https://portal.tacc.utexas.edu/account-request).
### Notes about preprocessed DEMs
* The DEMs are not provided for any HUC12s that have any gap in 1m resolution data.
* All of the DEMS are reprojected to [WGS 84 / UTM 14N](https://epsg.io/32614), even if the HUC12 is outside of UTM 14.
### Where to find them
The DEMs are located on [Stampede2](https://www.tacc.utexas.edu/systems/stampede2) at `/scratch/projects/tnris/dhl-flood-modelling/TX-HUC12-DEM_outputs`.
### If you run into trouble
Please [submit a ticket](https://portal.tacc.utexas.edu/tacc-consulting) if you have trouble accessing this data. You may also contact me directly at [@dhardestylewis](https://github.com/dhardestylewis) or <dhl@tacc.utexas.edu>
### Available preprocessed HUC12s
These HUC12 DEMs are available right now on [Stampede2](https://www.tacc.utexas.edu/systems/stampede2).
![Available HUC12 DEMs](https://github.com/dhardestylewis/GeoFlood-preprocessing/blob/master/DEM-HUC12-Availability.png)
### Confirmed successfully preprocessed HUC12s
These HUC12 DEMs have been successfully preprocessed in the past, and will soon be available once again on [Stampede2](https://www.tacc.utexas.edu/systems/stampede2). If you need any of these _right now_, please contact me.
![Confirmed HUC12 DEMs](https://github.com/dhardestylewis/GeoFlood-preprocessing/blob/master/DEM-HUC12-Confirmed.png)

## Preprocessing workflow
If you would like an understanding of the preprocessing workflow, I provide a simplified but representative example in this [Jupyter notebook](https://github.com/dhardestylewis/GeoFlood-preprocessing/blob/master/GeoFlood-Preprocessing.ipynb).
