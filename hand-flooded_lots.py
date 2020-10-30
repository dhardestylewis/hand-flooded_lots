import geopandas as gpd
import numpy as np
import os
import rasterio as rio
import rasterio
import rasterio.features

dd0 = gpd.read_file('ATX-LU-Inv-HUC120902050408bufdd0/ATX-LU-Inv-HUC120902050408bufdd0.shp')
zones = gpd.read_file('Zoning/geo_export_e17a0dd0-7b44-442f-818e-1cf280b410e7.shp')

dd0_mod = dd0
dd0_mod.property_i = dd0_mod.property_i.astype(np.float64)
dd0_zoned_contains = gpd.sjoin(dd0, zones, op='contains', how='left')
dd0_zoned_contains.to_file('dd0_zoned_contains.shp')

dd0_zoned_intersects = gpd.sjoin(dd0, zones, op='intersects', how='inner')
dd0_zoned_intersects.to_file('dd0_zoned_intersects.shp')

dd0_zoned_intersects_utm = dd0_zoned_intersects.to_crs({'init': 'epsg:6343'})
dd0_min = (dd0.to_crs({'init': 'epsg:6343'})['geometry'].area/10**6*247.105).min()
dd0_population = dd0_zoned_intersects_utm.land_use
dd0_zoned_intersects_utm = dd0_zoned_intersects.to_crs({'init': 'epsg:6343'})
dd0_population = dd0_zoned_intersects_utm.land_use.copy()

for i,i_land_use in enumerate(dd0_zoned_intersects_utm.land_use):
    #i_area = dd0_zoned_intersects_utm['geometry'].area.iloc[i]/10**6*247.105
    if i_land_use==100.0:
        dd0_population.iloc[i] = 6.
    elif i_land_use==113.0:
        dd0_population.iloc[i] = 6. * 5.
    elif i_land_use==150.0:
        dd0_population.iloc[i] = 6. * 2.
    elif i_land_use==160.0:
        dd0_population.iloc[i] = 6.
    elif i_land_use==210.0:
        dd0_population.iloc[i] = 6. * 4.
    elif i_land_use==220.0:
        dd0_population.iloc[i] = 6. * 5.
    elif i_land_use==230.0:
        dd0_population.iloc[i] = 10.
    elif i_land_use==240.0:
        dd0_population.iloc[i] = 10.
    elif i_land_use==610.0:
        dd0_population.iloc[i] = 10.
    else:
        dd0_population.iloc[i] = np.nan

dd0_risk = dd0_population / (dd0_zoned_intersects_utm['geometry'].area/10**6*247.105)
dd0_zoned_intersects_utm['risk'] = dd0_risk
dd0_zoned_intersects_utm.to_file('dd0_zoned_intersects_utm.shp')

dd = rasterio.open('Travis-DEM-10m-HUC120902050408bufdd/Travis-DEM-10m-HUC120902050408bufdd.tif')
out_fn = './rasterized.tif'

meta = dd.meta.copy()
out = rasterio.open(out_fn,'w+',**meta)
out_arr = out.read(1)
dd0_zoned_intersects_utm['risk'].fillna(0,inplace=True)
shapes = ((geom,value) for geom,value in zip(dd0_zoned_intersects_utm.geometry, dd0_zoned_intersects_utm.risk))
burned = rasterio.features.rasterize(shapes=shapes,out=out_arr,transform=out.transform)

ddshp = gpd.read_file('Travis-DEM-10m-HUC120902050408bufdd/Travis-DEM-10m-HUC120902050408bufdd.shp')

ddshpcut = ddshp.drop([0,6,7])
ddshpcut['const'] = 1.
ddshpall = ddshpcut.dissolve(by='const')
ddshpall = ddshpall.reset_index().drop(columns=['mean','const'])
ddshpall['bin_right'] = 6.0
ddshpall.to_file('Travis-DEM-10m-HUC120902050408bufdd-ALL.shp')

inv = gpd.read_file('ATX-LU-Inv-HUC120902050408buf/ATX-LU-Inv-HUC120902050408buf.shp')
inv06 = gpd.sjoin(inv,ddshpall.to_crs(inv.crs),how='inner',op='intersects')
inv06.to_file('inv06.shp')

