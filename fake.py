#taking a csv file and plotting. 

import pandas as pd 
import plotly.express as px
import plotly.io as pio
import os
import shutil

csvFile = "fake - fake3.csv"
df = pd.read_csv("fake - fake3.csv", index_col = 'county')

df = df.T 			# flipping graph to get data on certain axes

graphs = [] 		# creating array to store html files as strings

#os.mkdir("cities")
#print(os.getcwd())

#for names in df.columns: 
#	fig = px.line(df, x = df.index, y = names, hover_name = names,
#		title = 'Infection Rate Over Time', labels = {"x":"Dates"})   
#	graph = pio.write_html(fig,"city_"+names+".html", auto_open = False)
#	shutil.move("city_"+names+".html","cities")

assert len(df.columns) == 7, "should be 7"

assert (csvFile) == "fake - fake3.csv", "not its name"