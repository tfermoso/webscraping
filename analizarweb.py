import requests
from bs4 import BeautifulSoup


# Hacer una solicitud HTTP a la página web
url = 'https://www.marca.com'
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Parsear el contenido HTML de la página web
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar y extraer datos específicos
    # Por ejemplo, encontrar todos los enlaces (<a>) en la página
    enlaces = soup.find_all('form')
    
    # Imprimir los enlaces encontrados
    for enlace in enlaces:
        print(enlace.get('href'))
else:
    print('Error al cargar la página:', response.status_code)
