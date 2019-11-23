# Stock-Market-Analysis

https://drive.google.com/open?id=1yQA8o5krmdbmAiaO7xE5F34u7qLeHxiE

We have uploaded our "complete.csv" file onto Google Drive as when we git clone our repo, we only get a pointer to where it is stored because of its large file size. (~309mb) Github allows us only upto 100mb.

We have various data cleaning python files:
1) consolidate.py to consolidate the test data into 1 file (output.txt in folder 'all')
2) toCSV.py converts all our comma seperated .txt files into a .csv files. This has been used to generate all our final usable datasets.

We have scraped bonus and splits data using Beautiful soup. (scrapebonuses.ipynb, stockSplitParser.ipynb)

Code to be run:

final_DA.rmd

Change the path to the respective path on your system

final_DA_Workspace.RData is the corresponding workspace with a fresh copy of the data from complete.csv, in case there is an issue in loading the dataset. (Please don't run the chunk of code which has read.csv(complete.csv))
