import os
import requests
from bs4 import BeautifulSoup
import sys

# Set the base URL
base_url = 'https://sjconsulta.csjn.gov.ar/sjconsulta/documentos/verDocumentoByIdLinksJSP.html?idDocumento=8003291'
base_url = 'https://sjservicios.csjn.gov.ar/sj/tomosFallos.do?method=iniciar'

# Create a folder for saving PDFs
if not os.path.exists('pdf_downloads'):
    os.makedirs('pdf_downloads')

# Send an HTTP request to the webpage
# response = requests.get(base_url)
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(base_url, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Save the soup content to a file
with open('soup_output.html', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())  # prettify formats the HTML nicely


# Find all links to PDF files
pdf_links = soup.find_all('a', href=True)

# Iterate through found links
for link in pdf_links:
    pdf_url = link['href']
    print(pdf_url)
    if pdf_url.endswith('.pdf'):
        # Build the full URL for the PDF
        full_pdf_url = f"{base_url}/{pdf_url}"

        # Get the PDF filename
        pdf_filename = os.path.join('pdf_downloads', pdf_url.split('/')[-1])

        # Download the PDF
        pdf_response = requests.get(full_pdf_url)
        with open(pdf_filename, 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)
        print(f"Downloaded {pdf_filename}")