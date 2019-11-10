import csv
import urllib.request
import urllib
import pandas as pd
import time

BaseFilePath = "C:/Users/YOURNAME/PandasDFProjects/RedfinData/CSVDownload/"


class DataframeLoad:

    def __init__(self):
        self.zillowFilePath = BaseFilePath + "ZillowData.csv"
        self.redfinFilePath = BaseFilePath + "RedfinData.csv"
        self.zillowRentFilePath = BaseFilePath + "ZillowRentData.csv"

        self.ZillowRent1FilePath = BaseFilePath + "ZillowRentApend/ZillowRent1Data.csv"
        self.ZillowRent2FilePath = BaseFilePath + "ZillowRentApend/ZillowRent2Data.csv"
        self.ZillowRent3FilePath = BaseFilePath + "ZillowRentApend/ZillowRent3Data.csv"
        self.ZillowRent4FilePath = BaseFilePath + "ZillowRentApend/ZillowRent4Data.csv"
        self.ZillowRent5FilePath = BaseFilePath + "ZillowRentApend/ZillowRent5Data.csv"
        self.ZillowRentArrayFilePath = [self.ZillowRent1FilePath, self.ZillowRent2FilePath, self.ZillowRent3FilePath, self.ZillowRent4FilePath, self.ZillowRent5FilePath]


    def GetZillowDF(self):
        data = pd.read_csv(self.zillowFilePath,usecols=['RegionName','2019-09'], encoding = "ISO-8859-1")
        return data

    def GetZillowRentDF(self):
        bedrooms = 1
        appendedDF = pd.DataFrame(columns=['BEDS', 'RegionName', '2019-09'])
        for rentfile in self.ZillowRentArrayFilePath:
            arrayDF = pd.read_csv(rentfile, usecols=['RegionName', '2019-09'], encoding = "ISO-8859-1", dtype=str)
            arrayDF['BEDS'] = str(bedrooms)
            arrayDF['ZipBedKey'] = arrayDF['RegionName'].astype(str) + "-" + arrayDF['BEDS'].astype(str)

            appendedDF = appendedDF.append(arrayDF)    
            bedrooms += 1
        data = appendedDF
        return data

    def GetRedfinDF(self):
        data = pd.read_csv(self.redfinFilePath, encoding = "ISO-8859-1", dtype=str)
        data['ZipBedKey'] = data['ZIP OR POSTAL CODE'].astype(str) + "-" + data['BEDS'].astype(str)
        return data

class RedfinDataRetrieve:
    
    def __init__(self):
        self.redfinurl = "https://www.redfin.com/stingray/api/gis-csv?al=1&market=centralflorida&min_stories=1&num_homes=10000&ord=redfin-recommended-asc&page_number=1&poly=-81.64322%2028.46669%2C-81.08071%2028.46669%2C-81.08071%2028.78949%2C-81.64322%2028.78949%2C-81.64322%2028.46669&sf=1,2,3,5,6,7&status=9&uipt=1,2,3,4,5,6&v=8"
        self.zillowUrl = "http://files.zillowstatic.com/research/public/Zip/Zip_MedianValuePerSqft_AllHomes.csv"
        
        self.zillowRent1Url = "http://files.zillowstatic.com/research/public/Zip/Zip_MedianRentalPrice_1Bedroom.csv"
        self.zillowRent2Url = "http://files.zillowstatic.com/research/public/Zip/Zip_MedianRentalPrice_2Bedroom.csv"
        self.zillowRent3Url = "http://files.zillowstatic.com/research/public/Zip/Zip_MedianRentalPrice_3Bedroom.csv"
        self.zillowRent4Url = "http://files.zillowstatic.com/research/public/Zip/Zip_MedianRentalPrice_4Bedroom.csv"
        self.zillowRent5Url = "http://files.zillowstatic.com/research/public/Zip/Zip_MedianRentalPrice_5BedroomOrMore.csv"
        self.ZillowRentUrlArray = [self.zillowRent1Url, self.zillowRent2Url, self.zillowRent3Url, self.zillowRent4Url, self.zillowRent5Url]
        
        self.zillowRentUrl = "http://files.zillowstatic.com/research/public/Zip/Zip_ZriPerSqft_AllHomes.csv"
        
        self.filepath = BaseFilePath + "RedfinData.csv"
        self.zillowFilePath = BaseFilePath + "ZillowData.csv"
        
        self.ZillowRent1FilePath = BaseFilePath + "ZillowRentApend/ZillowRent1Data.csv"
        self.ZillowRent2FilePath = BaseFilePath + "ZillowRentApend/ZillowRent2Data.csv"
        self.ZillowRent3FilePath = BaseFilePath + "ZillowRentApend/ZillowRent3Data.csv"
        self.ZillowRent4FilePath = BaseFilePath + "ZillowRentApend/ZillowRent4Data.csv"
        self.ZillowRent5FilePath = BaseFilePath + "ZillowRentApend/ZillowRent5Data.csv"
        self.ZillowRentArrayFilePath = [self.ZillowRent1FilePath, self.ZillowRent2FilePath, self.ZillowRent3FilePath, self.ZillowRent4FilePath, self.ZillowRent5FilePath]

        self.zillowRentFilePath = BaseFilePath + "ZillowRentData.csv"
    
    def Get_Redfin_Data(self):
        print("get data called")
        f = open(self.filepath, 'wb+')
        useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
        headers = {
            'User-Agent': useragent,
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1'
        }
        req = urllib.request.Request(self.redfinurl, data=None,headers=headers)
        response = urllib.request.urlopen(req)
        responsedata = response.read()
        
        f.write(responsedata)
        #responsedata
        #responsedata_toCSV = csv.DictReader(responsedata)

        print(response.getcode())

    def Get_Zillow_Data(self):
        print("get data called")
        f = open(self.zillowFilePath, 'wb+')
        useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
        headers = {
            'User-Agent': useragent,
            'Upgrade-Insecure-Requests': '1'
        }
        req = urllib.request.Request(self.zillowUrl, data=None,headers=headers)
        response = urllib.request.urlopen(req)
        responsedata = response.read()
        
        f.write(responsedata)
        #responsedata
        #responsedata_toCSV = csv.DictReader(responsedata)

        print(response.getcode())

    def Get_ZillowRent_Data(self):
        print("get data called")
        urlresourcecount = 0
        for urlresource in self.ZillowRentUrlArray:
            f = open(self.ZillowRentArrayFilePath[urlresourcecount], 'wb+')
            useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
            headers = {
                'User-Agent': useragent,
                'Upgrade-Insecure-Requests': '1'
            }
            req = urllib.request.Request(urlresource,data=None,headers=headers)
            response = urllib.request.urlopen(req)
            responsedata = response.read()
            
            f.write(responsedata)
            #responsedata
            #responsedata_toCSV = csv.DictReader(responsedata)

            print(response.getcode())
            time.sleep(5)
            urlresourcecount = urlresourcecount + 1

