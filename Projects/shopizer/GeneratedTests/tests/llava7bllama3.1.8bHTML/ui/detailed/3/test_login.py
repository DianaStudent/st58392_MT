from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestShopUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def tearDown(self):
        self.driver.quit()
        
    def test_shop_ui(self):
        # Load the page and ensure that structural elements (e.g., header, footer, navigation) are visible.
        self.driver.get("http://localhost/")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "header")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "footer")))

        # Check the presence and visibility of input fields, buttons, labels, and sections.
        self._check_presence_and_visibility("tables", By.LINK_TEXT, "Tables")
        self._check_presence_and_visibility("chairs", By.LINK_TEXT, "Chairs")
        self._check_presence_and_visibility("login", By.LINK_TEXT, "Login")
        self._check_presence_and_visibility("register", By.LINK_TEXT, "Register")

        # Interact with key UI elements (e.g., click buttons).
        self.driver.get("http://localhost/login")
        button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "login-button")))
        button.click()

        # Confirm that the UI reacts visually.
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "react-toast-notifications__container")))

        # Assert that no required UI element is missing.
        self.driver.get("http://localhost/")
        required_elements = ["header", "footer", "tables", "chairs", "login", "register"]
        for element in required_elements:
            try:
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, element)))
            except TimeoutException:
                self.fail(f"Required element '{element}' is missing")

    def _check_presence_and_visibility(self, url, locator_type, text):
        self.driver.get("http://localhost/" + url)
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((locator_type, text)))
        except TimeoutException:
            self.fail(f"Element '{text}' is not visible")

if __name__ == "__main__":
    unittest.main()