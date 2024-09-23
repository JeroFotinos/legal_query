import requests
import time
from bs4 import BeautifulSoup

base_url = 'https://sjconsulta.csjn.gov.ar/sjconsulta/documentos/verDocumentoByIdLinksJSP.html?idDocumento=8003291'
response = requests.get(base_url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')


# Buscar todos los enlaces que tienen la clase "btn btn-link"
links = soup.find_all('a', class_='btn btn-link')
links = soup.find_all("a")
links = soup.find_all("div", class_= "panel-group")

for link in links:
    print(link)

"""
# Extraer los enlaces y descargarlos
tomo_url = "https://sjservicios.csjn.gov.ar"  # Base URL para construir los enlaces completos
for link in tomos_links[0:5]:
    fallo_url = tomo_url + link['href']    
    tomo_id = link['href'].split('=')[-1]  # Extraer el ID del tomo para el nombre del archivo
    response = requests.get(fallo_url)  
    if response.status_code == 200:
        print(f"Descargado: tomo_{tomo_id}.pdf")
        with open(f"pdf_downloads/tomo_{tomo_id}.pdf", "wb") as pdf_file:
            pdf_file.write(response.content)
        time.sleep(2)
    else:
        print("status_code:", response.status_code)
"""