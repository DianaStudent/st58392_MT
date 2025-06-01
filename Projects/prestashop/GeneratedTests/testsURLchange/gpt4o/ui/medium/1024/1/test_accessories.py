import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AccessoriesPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_ui_elements_presence(self):
        driver = self.driver

        # Verifying the presence of the header
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "header"))
        )
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Verifying the presence of navigation links
        nav_links = driver.find_elements(By.CSS_SELECTOR, ".top-menu .category")
        expected_links = ["Clothes", "Accessories", "Art"]
        for link_text in expected_links:
            self.assertTrue(any(link_text in link.text for link in nav_links),
                            f"Navigation link for {link_text} is missing")

        # Verifying the presence of a search input
        search_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='s']"))
        )
        self.assertTrue(search_input.is_displayed(), "Search input is not visible")

        # Verifying the presence of the 'Sign in' link
        sign_in_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Sign in"))
        )
        self.assertTrue(sign_in_link.is_displayed(), "Sign in link is not visible")

        # Verifying the presence of the cart button
        cart_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart"))
        )
        self.assertTrue(cart_button.is_displayed(), "Cart button is not visible")

        # Interacting with the 'Sign in' link to check UI updates
        sign_in_link.click()
        login_header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        self.assertTrue("Log in" in login_header.text, "UI did not update to login page")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()