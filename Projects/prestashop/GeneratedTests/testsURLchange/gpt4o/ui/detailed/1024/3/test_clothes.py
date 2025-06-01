import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ClothesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = self.wait

        # Check header visibility
        header = wait.until(
            EC.visibility_of_element_located((By.ID, "header"))
        )

        # Check footer visibility
        footer = wait.until(
            EC.visibility_of_element_located((By.ID, "footer"))
        )

        # Check main elements
        main = wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "main"))
        )

        # Check navigation links
        nav_links = [
            (By.LINK_TEXT, "Home"),
            (By.LINK_TEXT, "Clothes"),
            (By.LINK_TEXT, "Accessories"),
            (By.LINK_TEXT, "Art"),
            (By.LINK_TEXT, "Contact us")
        ]
        for link in nav_links:
            self.assertIsNotNone(wait.until(EC.visibility_of_element_located(link)))

        # Check input fields and buttons
        search_input = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#search_widget input[type='text']"))
        )
        search_button = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#search_widget .material-icons.search"))
        )
        sign_in_button = wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Sign in"))
        )
        self.assertIsNotNone(search_input)
        self.assertIsNotNone(search_button)
        self.assertIsNotNone(sign_in_button)

        # Interact with elements
        sign_in_button.click()

        # Assert modal or redirect
        sign_in_modal = wait.until(
            EC.url_contains("login")
        )
        self.assertIsNotNone(sign_in_modal)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()