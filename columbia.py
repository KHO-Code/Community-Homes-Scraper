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
    with open('columbia.csv', 'w',encoding='ISO-8859-1', newline='') as csvFile:
        fields = pagedata[0].keys()
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        writer.writeheader()
        for data in pagedata:
            writer.writerow(data)
    csvFile.close()

if __name__ == "__main__":

    options=webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(chrome_options=options,executable_path='/Users/KevinHo/Desktop/jubo/chromedriver')
    time.sleep(0.3)
    pagedata=[]

    start_url = 'https://www.health.gov.bc.ca/assisted/locator/index.php/displaycommunity/index'
    driver.get(start_url)
    time.sleep(5)

    virtualCommunityOptions = driver.find_elements_by_xpath("//select[@id='search-by-community']/option")
    temp = -1
    for communityOption in virtualCommunityOptions:
        temp += 1
        communityOptions = driver.find_elements_by_xpath("//select[@id='search-by-community']/option")
        if (communityOptions[temp].text == "Abbotsford") or (communityOptions[temp].text == "Burnaby") or (communityOptions[temp].text == "Vancouver"):
            community = communityOptions[temp].text
            communityOptions[temp].click()
            time.sleep(2)
            
            driver.find_elements_by_css_selector('button#start-alr-search')[0].click()
            time.sleep(2)

            cards = driver.find_elements_by_css_selector('div.tile')
            for card in cards:
                nameOfTheResidence = card.find_elements_by_css_selector('div>h3')[0].text
                pTags = card.find_elements_by_css_selector('div>p')
                for pTag in pTags:
                    pTagElements = pTag.text.split("\n")
                    for i in range(len(pTagElements)):
                        if "Total Assisted Living units:" in pTagElements[i]:
                            totalAssistedLivingUnits = pTagElements[i].split("Total Assisted Living units:")
                        if "Publicly subsidized units:" in pTagElements[i]:
                            publiclySubsidizedUnits = pTagElements[i].split("Publicly subsidized units:")
                        if "Private pay units:" in pTagElements[i]:
                            privatePayUnits = pTagElements[i].split("Private pay units:")
                        if "Address:" in pTagElements[i]:
                            address = pTagElements[i].split("Address:")
                        if "Phone:" in pTagElements[i]:
                            phone = pTagElements[i].split("Phone:")
                        if "Fax:" in pTagElements[i]:
                            fax = pTagElements[i].split("Fax:")
                        if "Website:" in pTagElements[i]:
                            website = pTagElements[i].split("Website:")
                        if "Health Authority:" in pTagElements[i]:
                            healthAuthority = pTagElements[i].split("Health Authority:")
                matchDetail = {
                    'Community': community,
                    'Name of the residence': nameOfTheResidence,
                    'Total Assisted Living units': totalAssistedLivingUnits[1],
                    'Publicly subsidized units': publiclySubsidizedUnits[1],
                    'Private pay units': privatePayUnits[1],
                    'Address': address[1],
                    'Phone': phone[1],
                    'Fax': fax[1],
                    'Website': website[1],
                    'healthAuthority': healthAuthority[1],
                }
                pagedata.append(matchDetail)
                time.sleep(1)
    write_csv(pagedata)
    print("done")
    driver.quit()
        
