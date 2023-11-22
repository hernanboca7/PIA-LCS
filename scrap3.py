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
# Buscar todos los elementos que el class "card-content"
job_elements = results.find_all("div", class_="card-content")
# Por cada elemento encontrado job_elements imprimimos.
for job_element in job_elements:
    print(job_element, end="\n"*2)