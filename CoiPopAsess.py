import csv
import matplotlib.pyplot as plt
import geopandas as gp
import math

## TODO
# To implement this COI analysis, you must import 5 files
# See the README for more information about these 5 files and how to download and import them

# 1, the CSV of your COI
from matplotlib import rcParams

coiBlocks = csv.reader(open(
    "FILLIN.csv"))

# 2, the CSV of the state's PL file
allBlocks = csv.reader(open("FILLIN.csv"))

# 3, the CSV of the census block assignments of the enacted plan
planBlocks = csv.reader(open("FILLIN.csv"))

# 4, the shapefile or geojson of the enacted plan
congress_map_shapefile = gp.read_file(
    "FILLIN.geojson")  

# 5, the shapefile of the US census blocks in the state
blocks_shapefile = gp.read_file("FILLIN.shp")

# create dictionary linking each block ID to its district. Key=blockID, value = district num
DistNums = {}
for x in planBlocks:
    if x[0] == 'GEOID20':
        None
    else:
        geoID = x[0]
        DistNums[geoID] = x[1]

# create dictionary linking each block ID to its population.
# Key = blockID, value = [block population, block district number]
allBlocksDict = {}
for x in allBlocks:
    # GEOID in census data has 10 starter character that have to be cut off
    geoIDLong = str(x[7])
    geoID = geoIDLong[9:]
    block_pop = x[9]
    allBlocksDict[geoID] = [block_pop, DistNums[geoID]]

popByDistrict = {}  # index = district number, value = population of COI in the district
blocks_in_coi = {}

# iterate through blocks in COI and create a dict with every district that contains some of the COI's population
# and tabulate the total population of the COI in these districts
for x in coiBlocks:

    blockID = x[0]
    if x[1] != '0':  # CSV exported from DistrictBuilder includes all census blocks, and marks COI blocks with a '1' in column 2, so ignore all others. DRA exports only the COI blocks, and has the COI name in column 2, so it passes through the if statement

        blocks_in_coi[blockID] = 1
        # add a leading 0 to geoID, because DRA sometimes does not format the geoID properly
        if blockID[0] != '0':
            blockID = '0' + blockID

        # skip first line by ignoring lines where len(string)<10, which would be a label like 'GeoID20'.  All census blocks will have a len(string) = 15
        if len(x[0]) < 10:
            None
        else:
            value = allBlocksDict[blockID]  # value = [block pop, block dist num]
            block_population = value[0]
            block_district_num = value[1]
            if popByDistrict.get(block_district_num) is None:
                popByDistrict[block_district_num] = int(block_population)
            else:
                popByDistrict[block_district_num] = popByDistrict[block_district_num] + int(block_population)

# to plot, the district #'s and their correlated pops must be in their own list.
districts = []
pops = []

# go through popByDistrict, add each district to the list, then sort in order
for x in popByDistrict:
    districts.append(x)
districts.sort()

# using the sorted districts list, search for the districts population, and add this to the pops list.
# now, the districts and pops list are sorted in order so that the district number and its population are at the same list indices
total_pop = 0  # total_pop used to calculate effective splits below
for x in districts:
    pops.append(popByDistrict[x])
    total_pop += popByDistrict[x]

# add wording to the labels
i = 0
for x in districts:
    districts[i] = 'District ' + str(x)
    i += 1

fig = plt.figure(1, figsize=(10, 7))
plt.pie(pops, labels=districts, autopct='%1.1f%%')
plt.text(0.75, -0.95, 'The population of your COI \n is split into ' + str(len(districts)) + ' districts. \n'
         + 'The percent of your COI\'s pop \n in each district is labeled on the pie chart.')


# Effective Splits and Uncertainty of Membership
# Effective Splits = (1/SUM(Ni^2))-1
# Uncertainty of Membership = -SUM(Nilog2Ni)
# where Ni is the proportion of a community contained in a district

sumNi_ES = 0
sumNI_UoM = 0
for x in pops:
    Ni = (int(x) / total_pop)
    sumNi_ES += Ni ** 2
    sumNI_UoM += (Ni * math.log2(Ni))
effective_splits = (1 / sumNi_ES) - 1
uncertainty_of_membership = -1 * sumNI_UoM

print('Effective Splits = ' + str(effective_splits))
print('Uncertainty of Membership = ' + str(uncertainty_of_membership))



## Map
# create new column in GeoDataFrame 'COI_blocks'. Set value to 1 if a block is in the COI. Then fill NaN values to 0.
blocks_shapefile['COI_blocks'] = blocks_shapefile['GEOID20'].map(blocks_in_coi)
blocks_shapefile = blocks_shapefile.fillna(0)

fig2 = plt.figure(2)
ax = fig2.add_subplot()

# apply district number labels
congress_map_shapefile.apply(
    lambda shpFile: ax.annotate(text=shpFile.NAME, xy=shpFile.geometry.centroid.coords[0], ha='right', fontsize=6),
    axis=1)
congress_map_shapefile = congress_map_shapefile.boundary.plot(ax=ax, color='Green', linewidth=.4)

blocks_shapefile.plot(ax=congress_map_shapefile, column='COI_blocks', cmap='OrRd')
plt.savefig('TestCOIMap.png', dpi=200)
plt.show()
