import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_ui_elements_present(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check header elements
            wait.until(EC.visibility_of_element_located((By.ID, "_desktop_logo")))
            wait.until(EC.visibility_of_element_located((By.ID, "category")))
            wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))

            # Check navigation links
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

            # Check subcategories section
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "subcategory-heading")))

            # Check products section
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "products")))

            # Check sign-in elements
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))

            # Check cart
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "blockcart")))

        except Exception as e:
            self.fail(f"UI element not found or not visible: {e}")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()