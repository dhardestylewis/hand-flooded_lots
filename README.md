# hand-flooded_lots
Python script to determine which lots in Austin are at risk of flooding

## This Python script is a template
If you would like an understanding of the preprocessing workflow, I provide a simplified but representative example in this [Jupyter notebook](https://github.com/dhardestylewis/GeoFlood-preprocessing/blob/master/GeoFlood-Preprocessing.ipynb).

## Main Python script
`hand-flooded_lots.py` can be run by:
```
python3 hand-flooded_lots.py
```

## Required source data inputs
There are 2 inputs.
* _HAND vector image:_ HAND vector GIS file of a basin in Austin, discretized into polygons of levels
* _[Zoning vector image](https://data.austintexas.gov/Locations-and-Maps/Zoning-Small-Map-Scale-/5rzy-nm5e):_ Austin's zoning vector GIS file, either entirely or a subset covering the basin of choice

## Description of outputs
There is 1 output.
* _Lots at risk:_
    * lots within basin in Austin that are at risk of flooding
    * selected if there is _any_ intersection with a lot and the HAND levels
    * include an attribute of the least HAND level for which a lot is at risk

An example of this output is on the right-hand side, as presented by former AAAI President [Yolanda Gil](https://viterbi.usc.edu/directory/faculty/Gil/Yolanda) during her outgoing President's speech at [AAAI 2020](https://aaai.org/Conferences/AAAI-20/). On the left-hand side is a [buyout map of the same area](https://www.austintexas.gov/department/williamson-creek-flood-risk-reduction) as produced by hand by the City of Austin. Prof Gil's brings up this topic at [39:18 in this recorded video of her speech](https://vimeo.com/400177695). They are at [pp 13-15 of these slides presented at the conference](https://www.dropbox.com/scl/fi/0opj6ff7cjyh0gpc2ettm/HANDEdits_PA-MINT.pptx?dl=0&rlkey=70qk5cxlyz04qvr74uwedwj1d).
![Example outputs](https://github.com/dhardestylewis/hand-flooded_lots/blob/main/refs/hand-flooded_lots-comparison.png)
