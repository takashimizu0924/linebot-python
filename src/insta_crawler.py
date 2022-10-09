from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
import chromedriver_binary
import time
def insta():
    CHROMEDRIVER = '/opt/chrome/chromedriver'
    URL = 'https://www.instagram.com/'

    options = Options()
    options.add_argument('--headless')  
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    chrome_service = fs.Service(executable_path=CHROMEDRIVER) 
    driver = webdriver.Chrome(service=chrome_service, options=options)
    driver.get(URL)
    time.sleep(3)
    driver.find_element(By.NAME,'username').send_keys('takashimizu924')
    time.sleep(2)
    driver.find_element(By.NAME,'password').send_keys('19900924')
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"button[type=submit]").click()
    time.sleep(2)

    html = driver.find_element(By.TAG_NAME,'body')
    print(html.text)

