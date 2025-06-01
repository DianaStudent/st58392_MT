import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AccessoriesPageTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_visibility(self):
        driver = self.driver
        wait = self.wait

        # Verify header is visible
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertTrue(header.is_displayed(), "Header is not visible.")

        # Verify footer is visible
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible.")

        # Verify navigation links
        nav_links = [
            (By.LINK_TEXT, "Home"),
            (By.LINK_TEXT, "Clothes"),
            (By.LINK_TEXT, "Accessories"),
            (By.LINK_TEXT, "Art")
        ]

        for by, text in nav_links:
            link = wait.until(EC.visibility_of_element_located((by, text)))
            self.assertTrue(link.is_displayed(), f"{text} link is not visible.")

        # Verify search input field is present and visible
        search_input = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        self.assertTrue(search_input.is_displayed(), "Search input is not visible.")

        # Verify 'Sign in' button is present and visible
        sign_in_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        self.assertTrue(sign_in_button.is_displayed(), "Sign in button is not visible.")

        # Interact with 'Sign in' button
        sign_in_button.click()
        self.assertEqual(driver.current_url, "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F6-accessories")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()