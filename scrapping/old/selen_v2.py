from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


# Configuración para que Chrome descargue automáticamente los archivos
download_dir = "pdf_downloads"  # Cambia esta ruta a donde quieras descargar el archivo
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    "download.default_directory": download_dir,  # Cambia esta ruta
    "download.prompt_for_download": False,       # No preguntar antes de descargar
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Inicializa el navegador con las opciones configuradas
driver = webdriver.Chrome(options=chrome_options)

try:
    # Abre la página
    driver.get("https://sjconsulta.csjn.gov.ar/sjconsulta/documentos/verDocumentoByIdLinksJSP.html?idDocumento=8003291")

    # Espera hasta que el botón de descarga esté visible
    download_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-link[href*='bajarDocumentoWordById']"))
    )

    # Haz clic en el botón de descarga
    download_button.click()

    # Espera unos segundos para que la descarga se complete
    time.sleep(10)  # Ajusta el tiempo según sea necesario

finally:
    driver.quit()

"""
try:
    # Abre la página
    driver.get("https://sjconsulta.csjn.gov.ar/sjconsulta/documentos/verDocumentoByIdLinksJSP.html?idDocumento=8003291")

    # Espera a que la página cargue
    time.sleep(5)  # Ajusta según sea necesario

    # Encuentra y haz clic en el botón o enlace de descarga
    download_button = driver.find_element(By.CSS_SELECTOR, "selector-del-boton-de-descarga")
    download_button.click()

    # Espera unos segundos para que la descarga se complete
    time.sleep(10)  # Ajusta el tiempo según sea necesario

finally:
    driver.quit()

"""
