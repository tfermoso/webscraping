import requests
import re

# Hacer una solicitud HTTP a la página web
url = 'https://www.ceica.net'  # Reemplaza 'example.com' con la URL de la página web que deseas analizar
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener el contenido HTML de la página web
    html_content = response.text
    
    # Definir la expresión regular para buscar direcciones de correo electrónico
    regex_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Buscar direcciones de correo electrónico en el contenido HTML utilizando la expresión regular
    matches = re.findall(regex_pattern, html_content)
    
    # Imprimir las direcciones de correo electrónico encontradas
    for match in matches:
        print(match)
else:
    print('Error al cargar la página:', response.status_code)
