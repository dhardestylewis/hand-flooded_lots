for i,i_land_use in enumerate(dd0_zoned_intersects_utm.land_use):
    i_area = dd0_zoned_intersects_utm['geometry'].area.iloc[i]/10**6*247.105
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
