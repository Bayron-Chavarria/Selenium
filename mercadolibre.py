import unittest
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class MercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        driver = self.driver
        driver.maximize_window()
        driver.get("https://mercadolibre.com/")

    def test_mercado_libre(self):
        driver = self.driver
        country = driver.find_element(By.ID, "CO")
        country.click()

        # aceptar cookies
        driver.find_element(By.CSS_SELECTOR,
                            "button.cookie-consent-banner-opt-out__action:nth-child(1)").click()  # noqa: E501
        WebDriverWait(driver, 5)

        # Barra de búsqueda, id
        search_field = driver.find_element(By.ID, "cb1-edit")
        button_search = driver.find_element(By.CSS_SELECTOR, ".nav-icon-search")  # noqa: E501
        search_field.click()
        search_field.clear()
        search_field.send_keys("playstation 4")
        button_search.click()
        WebDriverWait(driver, 5)

        # Ubicación --> Antioquia, condición - nuevo
        ubic = driver.find_element(By.PARTIAL_LINK_TEXT, "Antioquia")  # noqa: E501
        ubic.click()
        WebDriverWait(driver, 5)
        cond = driver.find_element(By.PARTIAL_LINK_TEXT, "Nuevo")
        cond.click()
        WebDriverWait(driver, 5)

        # ordenar por- tiene nombre de clase o id
        order_menu = driver.find_element(By.CLASS_NAME, "andes-dropdown__trigger")  # noqa: E501
        order_menu.click()
        WebDriverWait(driver, 20)
        css_mayor_precio = r"#\:Rlh9bb\:-menu-list-option-price_desc > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)"  # noqa: E501
        mayor_precio = driver.find_element(By.CSS_SELECTOR, css_mayor_precio)  # noqa: E501
        mayor_precio.click()
        WebDriverWait(driver, 5)

        products = driver.find_elements(By.CSS_SELECTOR, "h2.ui-search-item__title")  # noqa: E501
        price_products = driver.find_elements(By.CSS_SELECTOR, ".andes-money-amount.ui-search-price__part.ui-search-price__part--medium")  # noqa: E501
        product_data = []
        for product, price in zip(products, price_products):
            price = price.text.replace('\n', '')
            product_data.append({
                'title': product.text,
                'price': price
                })
        with open('products.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['title', 'price'])  # escribir encabezado
            for product in product_data:
                writer.writerow([product['title'], product['price']])

        # print(product_data)

    def tearDown(self):
        self.driver.implicitly_wait(15)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
