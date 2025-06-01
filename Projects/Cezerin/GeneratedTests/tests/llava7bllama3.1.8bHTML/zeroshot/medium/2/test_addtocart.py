import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("data:text/html," + html_data)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        # Open home page.
        pass

        # Click on product category
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a']"))).click()

        # Select the first product.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//h1[text()='Product A']")))

        # Click the "Add to cart" button
        self.driver.find_element_by_xpath("//button[@class='button is-success is-fullwidth']").click()

        # Click the cart icon/button to open the shopping bag.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='cart-button']"))).click()

        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[text()='GO TO CHECKOUT']"))))

if __name__ == '__main__':
    unittest.main()