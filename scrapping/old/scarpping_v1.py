import os
import requests
from bs4 import BeautifulSoup
import sys

# Set the base URL
base_url = 'https://sjconsulta.csjn.gov.ar/sjconsulta/documentos/verDocumentoByIdLinksJSP.html?idDocumento=8003291'


# Send an HTTP request to the webpage
response = requests.get(base_url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Save the soup content to a file
with open('soup_v1.html', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())  # prettify formats the HTML nicely

# Find all links to PDF files
fallos_links = soup.find_all('a', href=True)
word_links = soup.find_all('a', href=True, string="Word")

print(fallos_links)
print(word_links)






