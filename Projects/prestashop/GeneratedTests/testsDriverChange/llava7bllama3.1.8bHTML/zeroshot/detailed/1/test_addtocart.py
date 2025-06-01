from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestAddToCart(TestCase):
    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_add_to_cart(self):
        # Click on a product category from the top navigation menu (e.g. ART)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//nav[@class='main-nav']/ul/li[2]/a"))).click()

        # Wait for the category page to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@data-name='ART']")))

        # Click on the first product in the list
        product_list = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='row']/div[@class='col-md-4']/a")))
        product_list[0].click()

        # On the product detail page, click the "Add to cart" button
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@data-name='Add to cart']"))).click()

        # Wait for the modal popup to appear after the product is added
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "blockcart-modal")))
        except TimeoutException:
            self.fail("Modal did not appear")

        # Confirm that the modal title or content includes a success message like "successfully added"
        modal_title = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h4[@class='modal-title h6 text-sm-center']"))).text
        self.assertIn("successfully", modal_title)

    def tearDown(self):
        self.driver.quit()