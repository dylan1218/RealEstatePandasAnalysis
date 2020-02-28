# RealEstatePandasAnalysis
Python API wrapper to quickly analyze Redfin real estate listings against Zillow market data utilizing Pandas dataframe objects


**NOTE: I provide no disclaimer over the data obtained through the use of this project. All data is obtained from a combination of Redfin and Zillow. There is no official documentation for the queries being utilized, as such be respectful about how much you query -- query no more than you would query as if you were a web-app user.**


Getting started:

(1) Navaigate to RealEstatePandasAnalysis/blob/master/GetData/dataqueryanalyze.py and edit the BaseFilePath variable to the base file path you want to utilize to hold your loaded data.


Sample use is maintained in:

(1) RealEstateAnalyzeDataGenerate.py -- sample use for initial load of the data. Before utilizing the data load class you will first need to generate the data.

(2) RealEstateAnalyze.py -- sample use after the initial data is loaded. These classess are utilized to return pandas dataframes objects from the previously loaded data.

(3) CSVDownload Folder -- this contains the loaded data from Redfin/Zillow. I also load working outputs within the same folder, but they do not have to be maintained there.
