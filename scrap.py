from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# LinkedIn iş ilanları sayfasının URL'si
linkedin_url = 'https://www.linkedin.com/jobs/search/?currentJobId=3812876862&distance=25.0&f_TPR=r86400&geoId=102105699&keywords=front%20end%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER'

# Chromedriver'ın yolunu belirtme
chrome_driver_path = 'C:/Users/bedir/Desktop/chromedriver-win64/chromedriver'  # Chromedriver'ın yolunu belirtin
chrome_service = ChromeService(chrome_driver_path)

# ChromeDriver'ı başlatma
driver = webdriver.Chrome(service=chrome_service)

# LinkedIn sayfasını açma
driver.get(linkedin_url)

# Sayfanın yüklenip yüklenmediğini kontrol etmek için bekleme
for _ in range(10):  # Maksimum 10 kez kontrol et
    time.sleep(2)  # Her kontrol arasında 2 saniye bekleyin
    dynamic_content = driver.find_element(By.TAG_NAME, 'html').get_attribute('innerHTML')
    soup = BeautifulSoup(dynamic_content, 'html.parser')

    # 'li.jobs-search__results-list' öğesinin sayfada bulunup bulunmadığını kontrol et
    job_list_element = soup.find('li', class_='jobs-search__results-list')
    
    if job_list_element:
        break  # Öğe bulunduysa döngüden çık

# İş ilanlarını içeren HTML öğelerini seçme
job_elements = soup.find_all('li', class_='jobs-search-results__list-item')

# Her iş ilanını yazdırma
for job in job_elements:
    title = job.find('a', class_='job-title-text').text.strip()
    company = job.find('a', class_='job-company-name').text.strip()
    location = job.find('span', class_='job-result-card__location').text.strip()

    print(f"Title: {title}")
    print(f"Company: {company}")
    print(f"Location: {location}")
    print("\n")

# Tarayıcıyı kapatma
driver.quit()
