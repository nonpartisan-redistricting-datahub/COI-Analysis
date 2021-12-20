# Directions for COIOverlaps and COIPopAssess

# COIOverlap
Note: This program works with Community of Interest maps that were created in DavesRedistricting, Districtr, DistrictBuilder and Representable.  

This program allows a user to import n COI maps, such as all those submitted by the public, and returns a map of hot-spots where multiple COI map submissions outlined the same area as a community.  This is done by calculating an overlap score for each census block. Each census block receives a higher score as more COI maps include the block in their community.  As more people identify a geographic area as a Community of Interest, that area’s overlap score increases; that geographic area then appears darker on the map.
A user can also import a shapefile of a state’s current districts at any level (U.S. House, state senate…) and the program will outline the borders of the districts in the plan so that the COI hot-spots can be visualized with respect to the final district borders.

For any state, a user must download the following 5 data sets and import them into the program.  Directions on these steps are also written in the program itself.

A note on shapefiles: Downloading a shapefile will download a folder that includes a .cpg, .dbf, .prj and .shx file, in addition to the shapefile.  In order for the program to work, all these files must be kept with the shapefile in a single folder.  Import this entire folder to your working environment.  Only the shapefile needs to be directly referenced in the python program, however – the rest will be read automatically.

1. The shapefile (SHP) of the US census blocks in the state which can be found  at redistrictingdatahub.org, under ‘Data’, ‘Download Data’.  On a state’s data page, the file is named ‘2020 Block Boundaries’.  Ex: Arizona’s data set can be found here. 

2. The shapefile (SHP) of the enacted plan, which can be found at either redistrictingdatahub.org or AllAboutRedistricting. On the Redistricting Data Hub website, this can be found under ‘Data’, ‘Download Data’, and is called ‘2021 Adopted __ Plan.'  A geojson of the plan can be used instead of a shapefile here.

3. CSVs of all the COI maps that the user is interested in assessing for overlaps.  

4. The CSV of the census block assignments of the enacted plan

5. The CSV of the state's PL file

What to do once the files are downloaded:

Open the COIOverlap.py file in your Python IDE.  Through Finder (or Windows Explorer), drag and drop all files you downloaded into the folder that COIOverlap.py is in.  Then, put the file path name of the three aforementioned files into their respective variables in the COIOverlap program.  In COIOverlap the variables are listed in the same order as 1-3 above.  

Make sure all the COI maps are in one folder, and in COIOverlap.py set ‘all_COI_files’ equal to the path leading to this folder.  For example, if you have all the COI maps saved in a folder entitled ‘AllCOIMaps’, then your COIOverlap.py line will look like this: 
all_COI_files = os.listdir("put the path leading to AllCOIMaps here/AllCOIMaps")

# COIPopAssess
Note: This program works with Community of Interest maps that were created in DavesRedistricting, Districtr, DistrictBuilder and Representable.  

This program allows a user to import their Community of Interest map and returns the percent of the COI’s population in each district of the enacted plan. It also produces a map outlining the districts of the enacted plan with the COI overlaid for a visual representation of how the COI was split. The COI map can be drawn and downloaded from DavesRedistricting, DistrictBuilder or Districtr – all three are integrated into the program (in Daves and DistrictBuilder select the option to draw a Community rather than a full plan).  After drawing your community, export the block assignments for your community as a CSV.  Note: in Districtr, export as a ‘CSV (blocks),’ rather than a ‘CSV (these units).’

For any state, a user must download the following 5 data sets and import them into the program.  Directions on these steps are also written in the program itself.

1. The CSV of your COI, containing in the first column the GEOID of the blocks in the COI.  Drawing and exporting a COI from DavesRedistricting.org or DistrictBuilder.org will automatically format this file correctly.

2. The CSV of the state’s pl file, which can be found at redistrictingdatahub.org, under ‘Data’, ‘Download Data’.  On a state’s data page, the file is named ‘2020 Census Block level PL 94-171.’  Ex: Arizona’s data set can be found here. 

3. The CSV of the census block assignments of the enacted plan, which can be downloaded from a number of sources, including Davesredistricting.org, a state’s redistricting commission’s website, or a state legislature’s redistricting website.  

4. The shapefile (SHP) of the enacted plan, which can be found at either redistrictingdatahub.org or AllAboutRedistricting. On the Redistricting Data Hub website, this can be found under ‘Data’, ‘Download Data’, and is called ‘2021 Adopted ____ Plan.’  A geojson of the plan can be used instead of a shapefile here.

5. The shapefile (SHP) of the US census blocks in the state which can be found  at redistrictingdatahub.org, under ‘Data’, ‘Download Data’.  On a state’s data page, the file is named ‘2020 Block Boundaries’.  Ex: Arizona’s data set can be found here. 

What to do once the files are downloaded:

Open the COIPopAssess.py file in your Python IDE.  Through Finder (or Windows Explorer), drag and drop all files you downloaded into the folder that COIPopAssess.py is in.  Then, put the file path name of the five aforementioned files into their respective variables in the COIPopAssess program.  In COIPopAssess the variables are listed in the same order as 1-5 above. 
Final note: downloading a shapefile will download a folder that includes a .cpg, .dbf, .prj and .shx file, in addition to the shapefile.  In order for the program to work, all these files must be kept with the shapefile in a single folder.  Import this entire folder to your working environment.  Only the shapefile needs to be directly referenced in the python program, however – the rest will be read automatically.

