from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestClothesPage(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Check for key navigation links
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

            # Check for login link
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))

            # Check for search input
            search_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "s")))
            
            # Check for product containers
            product_container = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "js-product-list")))

            # Interact with an element (Search input in this case)
            search_input.send_keys("t-shirt")
            
            # Confirm UI updates visually by checking search input has the text
            self.assertEqual(search_input.get_attribute("value"), "t-shirt")

        except Exception as e:
            self.fail(f"UI element missing or interaction failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()