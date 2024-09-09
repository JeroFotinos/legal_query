from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Path to your ChromeDriver executable
chrome_driver_path = 'C:/Program Files (x86)/chromedriver.exe'

# Set up Chrome options
chrome_options = Options()
# Add options if needed
# chrome_options.add_argument('--headless')  # Uncomment if you want to run headless

# Initialize the ChromeDriver service with the path
service = Service(executable_path=chrome_driver_path)

# Initialize the Chrome driver with the service and options
driver = webdriver.Chrome(service=service, options=chrome_options)


base_url = 'https://sjconsulta.csjn.gov.ar/sjconsulta/documentos/verDocumentoByIdLinksJSP.html?idDocumento=8003291'
driver.get(base_url)

link = driver.find_element_by_link_text("Word")


print(search)

time.sleep(15)
driver.quit()