#!/usr/bin/env python
"""
Takes in a CSV file and creates .html and .json files according to each 
row in the file.
"""
import pandas as pd 
import plotly.express as px
import os
import shutil
import sys

__author__ = "Avery Bostick"

CSV_FILE = "fake - fake3.csv"


def getCSV(csvFile):
	df = pd.read_csv(csvFile, index_col = 'county')
	return df.T


def makeGraph(df, county):

	city_name = "cities/city_" + county

	fig = px.line(df, x = df.index, y = county, hover_name = county,
	title = 'Infection Rate Over Time', labels = {"x":"Dates"})
	fig.write_html(city_name + ".html", auto_open=False)
	fig.write_json(city_name + ".json")

	return city_name + ".html"


def processCounties(df):
	counties = []

	for county in df.columns:
		print(county)
		makeGraph(df, county)
		counties.append(county)

	return counties


def main(arg):
	df = getCSV(arg)

	if not os.path.isdir("cities"):
		os.mkdir("cities")

	counties = processCounties(df)

	return counties

if __name__ == "__main__":
 	main(sys.argv[1])