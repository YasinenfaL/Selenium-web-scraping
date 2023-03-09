# Libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# Driver path
driver = webdriver.Chrome(executable_path="C:/Users/Yasin/selenium/chromedriver.exe")

# URL of the site
url = "https://www.kariyer.net/is-ilanlari?kw=veri%20analisti"
# We need to let selenium know which browser I should use.
driver = webdriver.Chrome(executable_path="C:/Users/Yasin/selenium/chromedriver.exe")
# Opens the web page by going to the specified URL
driver.get(url)
# We got the HTML source codes
html = driver.page_source
# Parse processing
sp = BeautifulSoup(html, 'html.parser')

# After we find those with div tags and class ,kad-card-info , we return them as a list.
job_cards = sp.find_all('div', {"class": "kad-card-info"})

jobs = []

for job in job_cards:
    # we found job postings
    job_div = job.find("div", {"class": "d-flex kad-card-title-wrapper"})
    job_title = job_div.get_text().strip() if job_div else "NaN"

    # company names
    company_span = job.find("span", {"class": "kad-card-subtitle"})
    company_names = company_span.get_text().strip() if company_span else 'NaN'

    # company locations
    company_div = job.find("div", {"class": "kad-card-location-wrapper"})
    company_locations = company_div.get_text().strip() if company_div else 'NaN'

    job_dict = {'Job Name': job_title, 'Company': company_names, 'Location': company_locations}
    jobs.append(job_dict)
 

df = pd.DataFrame(jobs)
print(df)
df.to_csv('job_listings.csv', index=False)

