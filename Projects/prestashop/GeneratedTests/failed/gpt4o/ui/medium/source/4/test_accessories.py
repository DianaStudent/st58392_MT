from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Verify navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            art_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))

            # Verify key elements
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            contact_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/contact-us']")))
            sign_in = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F6-accessories']")))
            search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='s']")))

            # Verify product section
            product_list = wait.until(EC.presence_of_element_located((By.ID, "js-product-list")))
            first_product = wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[contains(@class, 'product')])[1]//a[@class='thumbnail product-thumbnail']")))

            # Verify interaction: Click the first product
            first_product.click()
            product_detail = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'product')]")))
        
        except Exception as e:
            self.fail(f"Test failed due to missing element or interaction error: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()