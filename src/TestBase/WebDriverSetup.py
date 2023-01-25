# librerias a importar
import unittest
from selenium import webdriver
import urllib3

# clase de la configuracion del navegador con los driver.
class WebDriverSetup(unittest.TestCase):

    # funcion para la configuracion del driver y maximizar la ventana del navegador
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # funcion para cerrar y quitar el driver
    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()