import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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

