import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAddProductToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")  # Replace with your home page URL

    def test_add_product_to_cart(self):
        # Click on a product category from the top navigation menu
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-name='ART']"))).click()

        # Wait for the category page to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content > div.container")))

        # Click on the first product in the list
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='product-list']/li[1]/div/div[2]/a"))).click()

        # On the product detail page, click the "Add to cart" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart > button"))).click()

        # Wait for the modal popup to appear after the product is added
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "blockcart-modal")))

        # Confirm that the modal title or content includes a success message like "successfully added"
        self.assertTrue("successfully added" in self.driver.find_element(By.CSS_SELECTOR, "#myModalLabel").text)

        # Optionally, locate and assert the presence of a "Proceed to checkout" button inside the modal
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@data-name='Proceed to checkout']")))
        except TimeoutException:
            pass

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()