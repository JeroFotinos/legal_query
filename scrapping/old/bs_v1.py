import requests
from bs4 import BeautifulSoup

# URL de la página
url = "https://sjconsulta.csjn.gov.ar/sjconsulta/documentos/verDocumentoByIdLinksJSP.html?idDocumento=8003291"

# Realizar una solicitud GET a la página
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Analizar el HTML con BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Buscar el enlace que contiene 'bajarDocumentoWordById' y el 'idDocumento=8003295'
    download_link = soup.find("a", href=lambda href: href and "bajarDocumentoWordById" in href and "idDocumento=8003295" in href)

    if download_link:
        # Obtener la URL completa del archivo a descargar
        file_url = "https://sjconsulta.csjn.gov.ar" + download_link['href']
        
        # Realizar una solicitud GET para descargar el archivo
        file_response = requests.get(file_url)
        
        # Guardar el archivo descargado
        file_name = "documento_word_8003295.docx"  # Cambia el nombre si lo deseas
        with open(file_name, "wb") as file:
            file.write(file_response.content)
        
        print(f"Archivo descargado como: {file_name}")
    else:
        print("No se encontró el enlace de descarga con el idDocumento=8003295.")
else:
    print(f"Error al acceder a la página: {response.status_code}")