from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# create new figure, axes instances.
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
# setup mercator map projection.
m = Basemap(llcrnrlon=19,llcrnrlat=14,urcrnrlon=65,urcrnrlat=50,\
            rsphere=(6378137.00,6356752.3142),\
            resolution='l',projection='merc',\
            lat_0=40.,lon_0=20,lat_ts=20.)
df = pd.read_csv("C:\\Users\\GANDI\\Downloads\\Book1.csv")
m.drawcoastlines()
m.drawcountries()
m.fillcontinents()
lon, lat= m(df["lon"].values, df["lat"].values)
popu = df["popu"].values
colors = plt.cm.tab10(np.arange(len(df)))
m.scatter(lon, lat, popu, colors, alpha =0.8)
for i in range(len(df)):
    lon, lat = m(df.loc[i,"lon"], df.loc[i,"lat"])
    plt.text(lon, lat, df.loc[i,"countries"])

ax.set_title('the five most populous countries in middle East')
plt.show()
