from GetData.dataqueryanalyze import RedfinDataRetrieve, DataframeLoad
import pandas as pd
import numpy as np


#redfin = RedfinDataRetrieve()

#Use the three below methods to update the redfin and zillow data -- don't query too often
#redfin.Get_Redfin_Data() #gets individual housing data
#redfin.Get_Zillow_Data() #get market pricing data
#redfin.Get_ZillowRent_Data() #gets market rental data

#The DataframeLoad class is utilized to return dataframes based upon the data imported from the RedfinDataRetrieve class
pandasquery = DataframeLoad()

ZillowDF = pandasquery.GetZillowDF()
ZillowRentDF = pandasquery.GetZillowRentDF()
RedfinDF = pandasquery.GetRedfinDF()



#inputs
mortgageRate = .045
propertyTaxRate = .0125

#Adds an average price field -- to do a weighted ranking consider price and rent differential
avgPriceMergeDF = pd.merge(RedfinDF, ZillowDF, left_on='ZIP OR POSTAL CODE', right_on='RegionName')
print(avgPriceMergeDF)

#Adds an average rent column and other calculated fields
avgRentMergeDF = pd.merge(RedfinDF, ZillowRentDF, left_on='ZipBedKey', right_on='ZipBedKey', how='left')
print(avgRentMergeDF)
avgRentMergeDF['PRICE'] = avgRentMergeDF['PRICE'].astype(float)
avgRentMergeDF['2019-09'] = avgRentMergeDF['2019-09'].astype(float)

#Monthly rental cost assumptions
mortgageEstimate = np.pmt(mortgageRate,12*30,avgRentMergeDF['PRICE'])/12*-1
propertyTaxEstimate = (avgRentMergeDF['PRICE']*propertyTaxRate)/12
insruanceEstimate = 150
HOACost = 200
depreciationCost = (avgRentMergeDF['PRICE']*.01)/12

monthlyCostEstimate = mortgageEstimate + propertyTaxEstimate + insruanceEstimate + HOACost + depreciationCost

#Adds a monthly cost estimate field
avgRentMergeDF['monthlyCostEstimate'] = monthlyCostEstimate

avgRentMergeDF['AvgRentVariance'] = avgRentMergeDF['2019-09'] - monthlyCostEstimate

#Print the DF to a csv
avgRentMergeDF.to_csv("C:/Users/YOURNAME/PandasDFProjects/RedfinData/CSVDownload/Redfin_ZillowMerge.csv")



