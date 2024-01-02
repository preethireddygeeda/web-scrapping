#### This program scrapes naukri.com's page and gives our result as a
#### list of all the job_profiles which are currently present there.

import xlwt
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#url of the page we want to scrape
url = "http://quotes.toscrape.com/"

# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

# this is just to ensure that the page is loaded
time.sleep(5)

html = driver.page_source

# this renders the JS code and stores all
# of the information in static HTML code.

# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
quote = soup.find_all('div', class_="quote")
language=[]
for i in range(len(quote)):
	span = quote[i].find('span', class_="text")
	language.append(span.text)
	
print(language)


data={'quote':language}
df=pd.DataFrame(data)
df.to_excel("quotes.xls")


#data={'title':title,'companyname':companyname,'exp':exp}
#df=pd.DataFrame(data)
#df.to_excel("naukri.xls")

#data=[title,companyname,exp]
#print(data)
#df=pd.DataFrame(data, columns=['tit','compan','exp'])
#print(df)
#df=pandas.DataFrame(data,columns=[])
#print(data)
#print(title)    
#print(companyname)
#print(exp)



driver.close() # closing the webdrive