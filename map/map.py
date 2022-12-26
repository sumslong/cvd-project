import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
# import sys
from heart_health_site import state_map
import state_map

#states_list = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']


# GEOPANDAS
def create_map():
    '''
    Create map for heart disease mortality rates by state (for each state).
    Creates a geopandas map, outlines the state, and saves map to .png file
  
    Inputs:
        state (str) state person lives in
    '''
    
    states_list = state_map.get_state_list()

    m_data = pd.read_csv("mortality_data.csv", usecols = ['YEAR', 'STATE', 'RATE', 'DEATHS'])
    m_data.rename(columns = {"STATE": "STUSPS"}, inplace = True)
    m_data_2020 = m_data[m_data.YEAR == 2020]
  
    states = gpd.read_file('tl_2021_us_state/tl_2021_us_state.shp')
    states = states.to_crs("EPSG:3395") # geospatial reference system identifier
  
    data = pd.merge(m_data_2020, states, on=["STUSPS"])
    gdf = gpd.GeoDataFrame(data)
    
    for state in states_list:
        base = gdf.plot(column = "RATE", legend=True, \
        legend_kwds={"label": "Heart Disease Mortality Rates by State"}, \
            cmap = plt.cm.Reds)
        if state != "Alaska":
            state_space = state.replace('_', ' ')
            gdf[gdf.NAME == state_space].boundary.plot(ax=base, color="Blue", linewidth=2)
            plt.xlim(-1.433 * 10**7, -0.73 * 10**7)
            plt.ylim(0.25 * 10**7, 0.65 * 10**7)
            plt.axis('off')
            plt.savefig("state_maps/" + state + '.png')
            # plt.show()
        else:
            gdf[gdf.NAME == state].boundary.plot(ax=base, color="Blue", linewidth=2)
            plt.xlim(-2.25 * 10**7, -0.73 * 10**7)
            # plt.ylim(0.25 * 10**7, 0.65 * 10**7)
            plt.axis('off')
            plt.savefig("state_maps/" + state + '.png')


