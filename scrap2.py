#
## Alumno: Hernán Bocanegra García 1851986 
## Laboratorio para Ciberseguridad 
#
# Importación de modulogs
import requests
from bs4 import BeautifulSoup
# Obtención de los datos mediante petición GET
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
# Analizamos el contenido HTML con BeatifulSoup
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
# Formateamos la salida del objeto results de BeautifulSoup
print(results.prettify())