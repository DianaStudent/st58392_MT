import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AccessoriesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_ui_elements_presence(self):
        driver = self.driver
        timeout = 20
        
        # Check the presence and visibility of navigation links
        try:
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Home"))
            )
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Clothes"))
            )
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Accessories"))
            )
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Art"))
            )
        except:
            self.fail("One or more navigation links are missing or not visible.")

        # Check the presence and visibility of a banner (if any)
        try:
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "header-banner"))
            )
        except:
            # Banner may not be visible; include a checks only if necessary elements are missing
            pass

        # Check presence of search bar
        try:
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.NAME, "s"))
            )
        except:
            self.fail("Search bar is missing or not visible.")

        # Check presence of a button
        try:
            lang_button = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "btn-unstyle"))
            )
            # Interact with language dropdown button
            lang_button.click()
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Latvija"))
            )
        except:
            self.fail("Language button is missing or does not function correctly.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()