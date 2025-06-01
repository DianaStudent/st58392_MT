from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestClothingPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_UI_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check if navigation links are present and visible
        nav_home = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'http://localhost:8080/en/')]")))
        nav_clothes = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'http://localhost:8080/en/3-clothes')]")))
        nav_accessories = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'http://localhost:8080/en/6-accessories')]")))
        nav_art = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'http://localhost:8080/en/9-art')]")))

        # Check if login and register links are present and visible
        login_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'http://localhost:8080/en/login')]")))
        register_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'http://localhost:8080/en/registration')]")))

        # Check if the search input is present and visible
        search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='s']")))

        # Check presence and visibility of product elements
        product_list = wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
        product_items = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "js-product-miniature")))

        # Interact with the search input and verify no errors
        search_input.send_keys("t-shirt")
        search_input.submit()

        # Wait for results to load and ensure there are no errors
        wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))

        # Confirm the presence of the cart icon
        cart_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart")))

        # Verify elements are clickable and do not cause UI errors
        try:
            nav_home.click()
            wait.until(EC.url_contains("http://localhost:8080/en/"))
        except Exception as e:
            self.fail(f"Navigation click failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()