from re import I
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome(executable_path=r'D:\Progam Files\webdriver\chromedriver.exe')

#Opens Website
driver.get('https://registrar-apps.ucdavis.edu/courses/search/index.cfm')

#Selects the correct quarter
quarter = Select(driver.find_element_by_xpath('//*[@id="termSelect"]/select'))
quarter.select_by_value('202210')

data = []

i = 1
while True:

    sub = []
    clss = []
    sec = []
    tmes = []

    try: 
        subject = Select(driver.find_element_by_xpath('//*[@id="home_tablez"]/tbody/tr[2]/td/h1/select'))
        subject.select_by_index(i)

        search = driver.find_element_by_xpath('//*[@id="home_tablez_bz"]/tbody/tr/td/h1/input[5]')
        search.click()

        #Collects Subject Name
        fSubject = driver.find_element_by_xpath('//*[@id="home_tablez"]/tbody/tr[2]/td/h1/select/option['+str(i+1)+']').text
        fSub = fSubject[len(fSubject)-4:len(fSubject)-1]
        print(fSub)
        sub.append(fSub)

        time.sleep(5)
        
        j = 5
        while True:
            try:
                #Gets Class (001)
                fClss = driver.find_element_by_xpath('//*[@id="mc_win"]/tbody/tr[' + str(j) + ']/td[2]').text.split('\n', 2)[0].split(' ',2)[1]
                # print(fClss)
                
                # #Gets the section (A01)
                fSec = driver.find_element_by_xpath('//*[@id="mc_win"]/tbody/tr['+str(j)+']/td[3]').text.split('\n',2)[0]
                #print(fSec)

                if not fSec == '-':
                    # #Gets the times (12:10 - 1:30 PM, TR)
                    fTime = driver.find_element_by_xpath('//*[@id="mc_win"]/tbody/tr['+str(j)+']/td[1]').text.replace(' ', '').split(',', 2)[1]+', '+driver.find_element_by_xpath('//*[@id="mc_win"]/tbody/tr['+str(j)+']/td[1]').text.replace(' ', '').split(',', 2)[0].split('\n', 2)[1]
                    #Updates the Class array
                    if not fClss in clss:
                        if not len(clss) == 0:
                            sec.append(tmes)
                            clss.append(sec)
                            sub.append(clss)
                            clss = []
                            sec = []
                            tmes = []
                        clss.append(fClss)

                    #Updates the sections array
                    if not fSec in sec:
                        if not len(sec) == 0:
                            sec.append(tmes)
                            clss.append(sec)
                            sec = []
                            tmes = []
                        sec.append(fSec)

                    tmes.append(fTime)
                err = 0                        

            except:
                err += 1
                if err < 2:
                    pass
                else:
                    sec.append(tmes)
                    clss.append(sec)
                    sub.append(clss)
                    break
            j+= 1
        i += 1

        data.append(sub)
    except:
        break

print(data)
