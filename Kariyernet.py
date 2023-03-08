# Kütüphane
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C:/Users/Yasin/selenium/chromedriver.exe")

# Sitenin URl'si
url = "https://www.kariyer.net/is-ilanlari?kw=veri%20analisti"
# Hangi tarayıcı üzerinden işlem yapmam gerektiğini selenium bildirmemiz gerekiyor.
driver = webdriver.Chrome(executable_path="C:/Users/Yasin/selenium/chromedriver.exe")
# Belirtilen URL'ye giderek web sayfasını açar
driver.get(url)
# HTML kaynak kodlarını aldık
html = driver.page_source
# Ayrıştırma işleme
sp = BeautifulSoup(html, 'html.parser')

# div etiketli ve class ,kad-card-info olanları bulduktan sonra bunları liste halinde döndürürüz.
job_cards = sp.find_all('div', {"class": "kad-card-info"})

for job in job_cards:
    # iş ilanlarını bulduk
    ıs_ilanı_etiketi = job.find("div", {"class": "d-flex kad-card-title-wrapper"})
    is_ilanı = ıs_ilanı_etiketi.get_text().strip() if ıs_ilanı_etiketi else "NaN"

    # şirket isimler
    sirket_ismi_etiket = job.find("span", {"class": "kad-card-subtitle"})
    sirket_ismi = sirket_ismi_etiket.get_text().strip() if sirket_ismi_etiket else 'NaN'

    # şirketin lokasyonları
    sirket_lokasyon_tag = job.find("div", {"class": "kad-card-location-wrapper"})
    sirket_lokasyon = sirket_lokasyon_tag.get_text().strip() if sirket_lokasyon_tag else 'NaN'

    # İstediğimiz çıktıyı elde ettik
    print('İşin Adı : {}\n'.format(is_ilanı))
    print('Şirket Adı : {}\n'.format(sirket_ismi))
    print('Lokasyon Bilgisi: {}\n\n'.format(sirket_lokasyon))

