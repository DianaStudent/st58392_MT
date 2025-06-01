from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

class TestWebPageUI(unittest.TestCase):
    def setUp(self):
        self.driver: WebDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        try:
            # Check header is present
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            
            # Check language selector
            language_selector = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "language-selector")))

            # Check sign in link
            sign_in = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))

            # Check cart link
            cart_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart")))

            # Check search widget
            search_widget = wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))

            # Check navigation menu (clothes, accessories, art)
            clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

            # Check footer is present
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))

        except Exception as e:
            self.fail(f"UI element not found or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()