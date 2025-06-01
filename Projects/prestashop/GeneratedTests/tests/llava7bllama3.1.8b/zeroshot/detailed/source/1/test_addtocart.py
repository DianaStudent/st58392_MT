import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/en/')

    def test_add_to_cart(self):
        # Click on the ART category from the top navigation menu
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//ul[@class="nav navbar-nav"]/li[2]/a'))).click()

        # Wait for the category page to load and click on the first product in the list
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="product-list"]/ul/li')))
        self.driver.find_element(By.XPATH, '//div[@class="product-list"]/ul/li[1]/a').click()

        # Click the "Add to cart" button
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]'))).click()

        # Wait for the modal popup to appear after the product is added
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@id="modal-product-cart"]/h4')))
            self.assertTrue("successfully added" in self.driver.find_element(By.XPATH, '//div[@id="modal-product-cart"]/h4').text)
        except TimeoutException:
            self.fail("Modal popup did not appear within 20 seconds.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()