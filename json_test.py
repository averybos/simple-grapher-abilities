"""
csv to json tester

parameterized test

unit test for each county 
open csv, convert to df, df.T, pick one county, x: list of dates and 
	y: list of rates,
	open json file, access json keys x and y, assert x==x && y==y 

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
"""

import json
from grapher import getCSV
import pandas as pd
import pytest


@pytest.mark.parametrize(
	"input, csv_dates",
	[]
)
def test_json_county(file_csv, file_json, county):

	read_file = open(file_json, "r")
	data = json.load(read_file)

	json_dates = data["data"][0]["x"]
	json_rates = data["data"][0]["y"]

	df = getCSV(file_csv)
	csv_dates = df.index.tolist()
	csv_rates = df[county].tolist()

	assert json_dates == csv_dates, "the dates do not match up"
	assert json_rates == csv_rates, "the rates do not match up"

def main():
	test_JSON_county("fake - fake3.csv", "cities/city_abbeville.json", "abbeville")

if __name__ == "__main__":
	main()