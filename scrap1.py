#
## Alumno: Hernán Bocanegra García 1851986 
## Laboratorio para Ciberseguridad 
#
# Importar módulos
import requests
# Obtener la información HTML de la URL
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
# Imprimir el texto de la petición GET
print(page.text)
