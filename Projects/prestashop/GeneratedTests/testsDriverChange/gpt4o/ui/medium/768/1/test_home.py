from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present(self):
        driver = self.driver

        # Verify that key navigation links are present and visible
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            clothes_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
            login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        except:
            self.fail("One or more navigation links are not present or visible.")

        # Verify that key buttons and inputs are present and visible
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))
            cart_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart")))
        except:
            self.fail("Key buttons or inputs are not present or visible.")

        # Interact with the search bar and verify UI updates
        try:
            search_input.send_keys("Hummingbird")
            search_button = driver.find_element(By.CLASS_NAME, "material-icons.search")
            search_button.click()

            # Confirm that search results update without errors (e.g., presence of some result)
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "h3.product-title")))
        except:
            self.fail("Interaction with the search bar failed or did not update UI as expected.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()