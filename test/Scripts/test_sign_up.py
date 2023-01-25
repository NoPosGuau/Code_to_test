import time
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import homePage

# clase para realizar el test
class course_packTest(WebDriverSetup):

    # funcion para crear un objeto con la clase de la carpeta de la pagina importada y enviarle los parametros.
    def test_add_item_to_course_pack(self):
        driver = self.driver
        self.driver.get(homePage.get_base_url())
        home_page = homePage(driver)
        time.sleep(3)
        home_page.sign_up("Samuel", "Romney", "809-828-2892", "Dom Rep", "Sto Dgo", "samuel@gmail.com")
        home_page.click_sign_up()