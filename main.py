import streamlit as st

import numpy as np

import pandas as pd
import geopandas as gpd

import matplotlib.pyplot as plt
import seaborn as sns

import folium
from streamlit_folium import folium_static

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('schools_combined.csv')


my_page = st.sidebar.radio('Page Navigation', ['Page 1', 'Page 2', 'Page 3', 'Page 4'])

if my_page == 'Page 1':
	st.title("Data")

	st.header("Public School Data in the Philippines")
	st.subheader('2015')

	data_load_state = st.text('Loading data...')

	st.write(df.head(20))

	# Customize texts using markdown
	data_load_state.markdown('Loading data...**done!**')



	if st.checkbox('Show data', value=True):
	    st.subheader('Data')
	    data_load_state = st.text('Loading data...')
	    st.write(df.head(20))
	    data_load_state.markdown('Loading data...**done!**')


	option = st.sidebar.selectbox(
	    'Which region do you want to see?',
	     df['region'].unique())

	'You selected: ', option


elif my_page == 'Page 2':

	#Copy paste your code from Jupyter but assign plt.figure to variable
	grade_level = df.groupby("year_level")["enrollment"].sum()
	st.header("Count of Students Per Year Level")

	fig = plt.figure(figsize=(8,6)) 
	plt.bar(grade_level.index, grade_level.values) 
	plt.title("Students in Public Schools", fontsize=16)
	plt.ylabel("Number of Enrollees", fontsize=12)
	plt.xlabel("Year Level", fontsize=12)
	year = ["grade 1","grade 2", "grade 3", "grade 4", "grade 5", "grade 6",
	        "first year", "second year", "third year", "fourth year"]
	plt.xticks(range(len(grade_level.index)), year, rotation=45)

	# display graph by plotting figure variable
	plt.show()
	st.pyplot(fig)


elif my_page == 'Page 3':
    st.title("Geospatioal Analysis of Schools")
    schools = gpd.read_file('phl_schp_deped/phl_schp_deped.shp')
    schools["x"] = schools.geometry.centroid.x
    schools["y"] = schools.geometry.centroid.y
    #st.write(schools.head(20))
    # Coordinates to show
    map_center = [14.583197, 121.051538]

    # Styling the map
    mymap = folium.Map(location=map_center, height=700, width=1000, tiles="OpenStreetMap", zoom_start=14)
    option_city = st.sidebar.selectbox(
        'Which city',
        schools["Division"].unique())
    'You selected: ', option_city
    city = option_city

    df_city = schools[schools["Division"]==city]

    for i in np.arange(len(df_city)):
        lat = df_city["y"].values[i]
        lon = df_city["x"].values[i]
        name = df_city["School"].values[i]
        folium.Marker([lat, lon], popup=name).add_to(mymap)
    folium_static(mymap)

elif my_page == 'Page 4':
    st.title("Geospatioal Analysis of Schools : st.map")
    schools = gpd.read_file('phl_schp_deped/phl_schp_deped.shp')
    # to plot a map using st.map, you need a column names lon and lat
    schools["lon"] = schools.geometry.centroid.x
    schools["lat"] = schools.geometry.centroid.y
    st.map(schools.head(10))

