from GetData.dataqueryanalyze import RedfinDataRetrieve, DataframeLoad
import pandas as pd

redfin = RedfinDataRetrieve()

#Use the three below methods to update the redfin and zillow data -- don't query too often
redfin.Get_Redfin_Data() #gets individual housing data
redfin.Get_Zillow_Data() #get market pricing data
redfin.Get_ZillowRent_Data() #gets market rental data
