import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        self.assertIsNotNone(header, "Header is not present or visible")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
        self.assertIsNotNone(footer, "Footer is not present or visible")

        # Check main menu visibility
        main_menu = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "main-menu")))
        self.assertIsNotNone(main_menu, "Main menu is not present or visible")

        # Check product list visibility
        product_list = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shop-area")))
        self.assertIsNotNone(product_list, "Product list is not present or visible")

        # Interact with buttons
        self.assert_element_and_click(By.XPATH, "//button[text()='Add to cart']", "Add to cart button")

        # Check input fields and sections
        email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        self.assertIsNotNone(email_input, "Email input field is not present or visible")

        # Assert no critical elements are missing
        self.assert_element_exists_and_visible(By.XPATH, "//a[text()='Home']", "Home link")
        self.assert_element_exists_and_visible(By.XPATH, "//a[text()='Tables']", "Tables link")
        self.assert_element_exists_and_visible(By.XPATH, "//a[text()='Chairs']", "Chairs link")
        self.assert_element_exists_and_visible(By.XPATH, "//a[text()='Login']", "Login link")
        self.assert_element_exists_and_visible(By.XPATH, "//a[text()='Register']", "Register link")

    def assert_element_and_click(self, by, selector, description):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((by, selector)))
        self.assertIsNotNone(element, f"{description} is not present or visible")
        element.click()

    def assert_element_exists_and_visible(self, by, selector, description):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((by, selector)))
        self.assertIsNotNone(element, f"{description} is not present or visible")
    
if __name__ == "__main__":
    unittest.main()