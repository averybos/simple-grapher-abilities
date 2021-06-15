
"""
test_grapher.py
replicate assignment about pytest

parameterized tests as well
 for all functions returning a value

makeGraph given df and county
"""

import pandas as pd
import pytest
from grapher import makeGraph, processCounties, getCSV, main

CSV_FILE = "fake - fake3.csv"

def test_makeGraph():
	assert makeGraph(df, county) == "" + ".html"


def test_processCounties():
	fixed = create_instance()
	df = pd.read_csv(CSV_FILE, index_col = 'county')
	assert processCounties(df.T) == fixed.columns.tolist()


def test_getCSV(create_instance, CSV_FILE):
	#pytest.fixture
	assert getCSV(CSV_FILE) == create_instance()


def test_main():
	df = pd.read_csv(CSV_FILE, index_col = 'county')
	assert main() == processCounties(df.T)


# creates instance of pandas dataframe, reads csv file 
# and returns transposed csv file
@pytest.fixture
def create_instance():
	df = pd.read_csv(CSV_FILE, index_col = 'county')
	return df.T
