import csv
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from itertools import islice

def write_csv(pagedata):
    res_list = [] 
    for i in range(len(pagedata)): 
        if pagedata[i] not in pagedata[i + 1:]: 
            res_list.append(pagedata[i]) 
    pagedata=res_list
    with open('alberta.csv', 'w',encoding='ISO-8859-1', newline='') as csvFile:
        fields = pagedata[0].keys()
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        writer.writeheader()
        for data in pagedata:
            writer.writerow(data)
    csvFile.close()


if __name__ == "__main__":

    options=webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(chrome_options=options,executable_path='/Users/KevinHo/Desktop/jubo/files/chromedriver')
    time.sleep(0.3)
    pagedata=[]

    start_url = 'https://www.albertahealthservices.ca/cc/page15328.aspx#ccfd'
    driver.get(start_url)
    time.sleep(5)

    virtualCareOptions = driver.find_elements_by_xpath("//select[@name='ddlCity'][@id='ddlCity']/option")
    temp = -1
    for option in virtualCareOptions:
        temp += 1
        careOptions = driver.find_elements_by_xpath("//select[@name='ddlCity'][@id='ddlCity']/option")
        if (careOptions[temp].text == "Banff"):
            Care = careOptions[temp].text
            print(Care)
            careOptions[temp].click()
            time.sleep(2)

            driver.find_elements_by_css_selector('a#lbtSearch')[0].click()
            time.sleep(5)

            links = driver.find_elements_by_css_selector('div.gridContainer>a')
            linkTemp = -1
            for link in links:
                linkTemp += 1
                realLinks = driver.find_elements_by_css_selector('div.gridContainer>a')
                realLinks[linkTemp].click()
                time.sleep(1)

                operatorName=''
                operatorType=''
                yearOfBuild=''
                Website=''
                Address=''
                Telephone=''
                Fax=''
                typeofSite=''
                publiclyFundSpaces=''
                residentFamilySurveyResults=''
                accreditationStatus=''
                accreidtationOrganization=''

                thTags = driver.find_elements_by_css_selector('table>tbody>tr>th')
                thTemp = -1
                for thTag in thTags:
                    thTemp += 1
                    thTagText = thTag.text
                    if thTagText == "Type of Site":
                        typeofSite = thTags[thTemp+1].text
                    
                





        


