# hand-flooded_lots
Python script to determine which lots in Austin are at risk of flooding from Height Above Nearest Drainage (HAND) values

## Scientific background
"Height Above Nearest Drainage (HAND) is an approach for estimating the vertical height of any point on the landscape from the nearest stream surface or bed." [Yan Liu](https://www.ornl.gov/staff-profile/yan-liu) [2018](https://www.hydroshare.org/resource/69f7d237675c4c73938481904358c789/).

## This Python script is a template
This repository currently records the workflow to produce risk estimates by lot in Austin, but does not provide an independently executable script. You will need to modify the input filenames within the script itself before you can run it successfully.

## Main Python script
Once modified to your use-case, `hand-flooded_lots.py` can be run by:
```
python3 hand-flooded_lots.py
```

## Required source data inputs
There are 2 inputs.
* _HAND vector image:_ HAND vector GIS file of a basin in Austin, with each polygon being a range of HAND values (ex. 1-2 ft, 2-3 ft, ...) 
* _[Zoning vector image](https://data.austintexas.gov/Locations-and-Maps/Zoning-Small-Map-Scale-/5rzy-nm5e):_ Austin's zoning vector GIS file, either entirely or a subset covering the basin of choice

## Description of outputs
There is 1 output.
* _Lots at risk:_
    * each lot was selected if there is _any_ intersection a HAND level at or below 20 ft
    * each lot includes an attribute the HAND level for which the lot is at risk

The image below contains an example of this output, on the right-hand side. This example demonstrates the similarity between this workflow's automaically generated at-risk lots and [manually created at-risk lots](https://www.austintexas.gov/department/williamson-creek-flood-risk-reduction) produced by the City of Austin. This example was presented by former AAAI President [Yolanda Gil](https://viterbi.usc.edu/directory/faculty/Gil/Yolanda) during her outgoing President's speech at the [AAAI 2020 conference](https://aaai.org/Conferences/AAAI-20/) in February. Prof Gil's brings up this topic at [39:18 in this recorded video of her speech](https://vimeo.com/400177695). They are at [pages 13-15 of these slides presented at the conference](https://www.dropbox.com/scl/fi/0opj6ff7cjyh0gpc2ettm/HANDEdits_PA-MINT.pptx?dl=0&rlkey=70qk5cxlyz04qvr74uwedwj1d).
![Example outputs](https://github.com/dhardestylewis/hand-flooded_lots/blob/main/refs/hand-flooded_lots-comparison.png)

This same example was also presented by [Dr Suzanne Pierce](https://www.tacc.utexas.edu/about/directory/suzanne-pierce) during her [keynote talk](https://csdms.colorado.edu/wiki/Presenters-0473) at the [CSDMS 2020 conference](https://csdms.colorado.edu/wiki/CSDMS_meeting_2020) in May.
