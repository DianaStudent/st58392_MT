from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_home_page_elements_present(self):
        driver = self.driver
        # Navigate to the home page
        driver.get("http://localhost:8080/en/")

        # Wait for 20 seconds to ensure elements are loaded
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//header")))

        # Check that structural elements (e.g., header) are visible
        self.assertTrue(self.is_element_visible(driver, By.XPATH, "//header"))
        self.assertTrue(self.is_element_visible(driver, By.XPATH, "//footer"))

        # Check the presence and visibility of input fields, buttons, labels, and sections
        self.assertTrue(self.is_element_visible(driver, By.ID, "username"))
        self.assertTrue(self.is_element_visible(driver, By.ID, "password"))
        self.assertTrue(self.is_element_visible(driver, By.ID, "login-btn"))

    def is_element_visible(self, driver, locator_type, locator_value):
        try:
            driver.find_element(locator_type, locator_value)
            return True
        except Exception as e:
            print(e)
            return False

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()