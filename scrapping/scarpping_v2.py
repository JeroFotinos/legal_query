import requests
from bs4 import BeautifulSoup

base_url = 'https://sjservicios.csjn.gov.ar/sj/tomosFallos.do?method=iniciar'
response = requests.get(base_url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Buscar todas las etiquetas <a> que contienen los enlaces a los tomos
tomos_links = soup.find_all("a", class_="linkTomo")

print(tomos_links)

# Extraer los enlaces y descargarlos
base_url = "https://sj.csjn.gov.ar"  # Base URL para construir los enlaces completos
for link in tomos_links:
    tomo_url = base_url + link['href']
    tomo_id = link['href'].split('=')[-1]  # Extraer el ID del tomo para el nombre del archivo
    print(tomo_url)
    response = requests.get(tomo_url)
    print(response)
    break
    with open(f"tomo_{tomo_id}.pdf", "wb") as pdf_file:
        pdf_file.write(response.content)
    print(f"Descargado: tomo_{tomo_id}.pdf")

