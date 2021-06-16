### avery bostick

`simple-grapher-abilites` is a collection of files created for a school project where I turned csv file information into graphs to see more visually.

Using pandas primarily, the main file grapher.py takes in a csv file and creates a dataframe in order to visualize the data.

This was for a school project in which we pulled data from the John Hopkins coronavirus dashboard in order to get the infection rate across all counties in America. From there, the rates were brought into a csv file and that was where I came in. I took the data and made graphs of each county. 

With these graphs made, I wrote them to .html files and also .json files. I wrote unit tests using pytest to make sure the names, indexes, and file names were correctly formatted.