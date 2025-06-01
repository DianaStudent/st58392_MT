import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_present(self):
        driver = self.driver

        # Wait for header elements
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "header"))
            )
        except:
            self.fail("Header is not visible")

        # Check search input
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input"))
            )
        except:
            self.fail("Search input is not visible")

        # Check cart button
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "span.cart-button"))
            )
        except:
            self.fail("Cart button is not visible")

        # Check primary navigation links
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a']"))
            )
        except:
            self.fail("Category A link is not visible")
        
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-b']"))
            )
        except:
            self.fail("Category B link is not visible")
        
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-c']"))
            )
        except:
            self.fail("Category C link is not visible")

        # Check footer exists
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "footer"))
            )
        except:
            self.fail("Footer is not visible")


if __name__ == "__main__":
    unittest.main()