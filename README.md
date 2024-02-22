# Prueba de Test en Mercado Libre
Este proyecto consiste en una prueba de test automatizado en la página web de Mercado Libre, buscando la palabra clave "playstation4". El script realiza las siguientes acciones:

1. Accede a la página de Mercado Libre Colombia.
2. Filtra los resultados por el departamento de Antioquia.
3. Ordena los resultados por los productos más nuevos y con el mayor precio.
4. Obtiene el listado de objetos en pantalla junto con sus precios.
5. Crea un archivo CSV con el listado obtenido.

## Requisitos

- Navegador Firefox
- Python 3.9
- [Selenium 4.17](https://www.selenium.dev/documentation/webdriver/getting_started/install_library/)
- [Geckodriver](https://github.com/mozilla/geckodriver/releases) (para Firefox)

## Uso
1. Ejecuta el script `mercado_libre.py`
2. El script abrirá una instancia de Firefox y realizará la prueba automatizada en Mercado Libre.
3. Crea un archivo 'producst.csv' con el listado de productos y precios de los mismos.
