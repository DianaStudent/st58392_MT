import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_add_to_cart(self):
        self.driver.get("http://localhost:8080/en/")

        # Wait for the modal to appear after adding to cart
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-name='modal-header']"))
        )

        # Add product to cart (select variation and quantity)
        self.driver.find_element(By.XPATH, "//label[@for='variation-1']").click()  # Select variation
        self.driver.find_element(By.NAME, "quantity").send_keys("2")  # Set quantity

        # Click add to cart button
        self.driver.find_element(By.ID, "add-to-cart-button").click()

        # Wait for the modal to appear after adding to cart
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-name='modal-header']"))
        )

        # Check if the title of the modal contains "successfully added"
        self.assertTrue("successfully added" in self.driver.find_element(By.XPATH, "//h4").text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()