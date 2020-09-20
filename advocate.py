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
    with open('advocate.csv', 'w',encoding='ISO-8859-1', newline='') as csvFile:
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

    start_url = 'https://www.seniorsadvocatebc.ca/quickfacts/search/%20/4/all/Vancouver'
    driver.get(start_url)
    time.sleep(5)

    virtualHealthAuthorityOptions = driver.find_elements_by_xpath("//select[@id='osa-quickfacts-hlth-filter']/option")
    temp = -1
    for option in virtualHealthAuthorityOptions:
        temp += 1
        healthAUthorityOptions = driver.find_elements_by_xpath("//select[@id='osa-quickfacts-hlth-filter']/option")
        if (healthAUthorityOptions[temp].text == "Vancouver Coastal Health") or (healthAUthorityOptions[temp].text == "Northern Health") or (healthAUthorityOptions[temp].text == "Fraser Health"):
            healthAuthority = healthAUthorityOptions[temp].text
            print(healthAuthority)
            healthAUthorityOptions[temp].click()
            time.sleep(2)

            driver.find_elements_by_css_selector('button#osa-quickfacts-search-filter')[0].click()
            time.sleep(5)

            pageNations = driver.find_elements_by_css_selector('div.qf-search-pagination>nav>ul>li>a')
            pageTemp = -1
            for pageNation in pageNations:
                pageTemp += 1
                if (pageTemp == 0) or (pageTemp == len(pageNations)-1):
                    continue
                pages = driver.find_elements_by_css_selector('div.qf-search-pagination>nav>ul>li>a')
                pages[pageTemp].click()
                print(pageTemp)
                time.sleep(3)

                links = driver.find_elements_by_css_selector('div.qf-search-record>h2>a')
                linkTemp = -1
                for link in links:
                    linkTemp += 1
                    realLinks = driver.find_elements_by_css_selector('div.qf-search-record>h2>a')
                    realLinks[linkTemp].click()
                    time.sleep(1)

                    facilityName=''
                    healthAuthorityText = ''
                    regulationAndLegislation = ''
                    streetAddress = ''
                    cityPostalCode = ''
                    accreditationStatus = ''
                    accreditationExpiryDate = ''
                    phoneNumber = ''
                    operator = ''
                    phoneNumberOfComplaint = ''
                    opened = ''
                    currentLanguage = ''
                    privateBeds = ''
                    publicyBeds = ''
                    totalBeds = ''
                    privateRooms = ''
                    semiPrivateRooms = ''
                    multiPersonRooms = ''
                    caseMixIndexFacility = ''
                    caseMixIndexBC = ''

                    thTags = driver.find_elements_by_css_selector('table>tbody>tr>th')
                    thTagTemp = -1
                    for thTag in thTags:
                        thTagTemp += 1
                        thTagText = thTag.text
                        if thTagText == "Facility":
                            facilityName = thTags[thTagTemp+1].text
                            break


                    tdTags = driver.find_elements_by_css_selector('table>tbody>tr>td')
                    tdTemp = -1
                    for tdTag in tdTags:
                        tdTemp += 1
                        tdTagText = tdTag.text
                        if tdTagText == "Health authority":
                            healthAuthorityText = tdTags[tdTemp+1].text
                        if tdTagText == "Regulation/Legislation":
                            regulationAndLegislation = tdTags[tdTemp+1].text
                            print(regulationAndLegislation)
                        if tdTagText == "Street address":
                            streetAddress = tdTags[tdTemp+1].text
                        if tdTagText == "City/postal code":
                            cityPostalCode = tdTags[tdTemp+1].text
                        if tdTagText == "Accreditation status":
                            accreditationStatus = tdTags[tdTemp+1].text
                        if tdTagText == "Accreditation expiry date":
                            accreditationExpiryDate = tdTags[tdTemp+1].text
                        if tdTagText == "Phone number":
                            phoneNumber = tdTags[tdTemp+1].text
                        if tdTagText == "Operator (name)":
                            operator = tdTags[tdTemp+1].text
                        if tdTagText == "Phone number of complaint contact":
                            phoneNumberOfComplaint = tdTags[tdTemp+1].text
                        if tdTagText == "Opened":
                            opened = tdTags[tdTemp+1].text
                        if tdTagText == "Current language(s) spoken by staff":
                            currentLanguage = tdTags[tdTemp+1].text
                        if tdTagText == "Private beds (not publicly funded)":
                            privateBeds = tdTags[tdTemp+1].text
                        if tdTagText == "Publicly funded beds (short- and long-term)":
                            publicyBeds = tdTags[tdTemp+1].text
                        if tdTagText == "Total beds":
                            totalBeds = tdTags[tdTemp+1].text
                        if tdTagText == "Private rooms":
                            privateRooms = tdTags[tdTemp+1].text
                        if tdTagText == "Semi-private rooms":
                            semiPrivateRooms = tdTags[tdTemp+1].text
                        if tdTagText == "Multi-person rooms":
                            multiPersonRooms = tdTags[tdTemp+1].text
                        if tdTagText == "Case mix index":
                            caseMixIndexFacility = tdTags[tdTemp+1].text
                            caseMixIndexBC = tdTags[tdTemp+2].text
                    matchDetails = {
                        'Facility': facilityName,
                        'Health authority': healthAuthorityText,
                        'Regulation/Legislation': regulationAndLegislation,
                        'Street address': streetAddress,
                        'City/postal code': cityPostalCode,
                        'Accreditation status': accreditationStatus,
                        'Accreditation expiry date': accreditationExpiryDate,
                        'Phone number': phoneNumber,
                        'Operator (name)': operator,
                        'Phone number of complaint contact':phoneNumberOfComplaint ,
                        'Opened': opened,
                        'Current language(s) spoken by staff': currentLanguage,
                        'Private beds (not publicly funded)': privateBeds,
                        'Publicly funded beds (short- and long-term)': publicyBeds,
                        'Total beds': totalBeds,
                        'Private rooms': privateRooms,
                        'Semi-private rooms': semiPrivateRooms,
                        'Multi-person rooms': multiPersonRooms,
                        'Case mix index Facility': caseMixIndexFacility,
                        'Case mix index B.C.': caseMixIndexBC,
                    }
                    pagedata.append(matchDetails)
                    write_csv(pagedata)
                    driver.back()

    # write_csv(pagedata)
    print("done")
    driver.quit()
        
