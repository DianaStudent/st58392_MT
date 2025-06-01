from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestDemoPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_key_ui_elements(self):
        try:
            # Verify header elements
            header = self.wait.until(EC.visibility_of_element_located((By.ID, 'header')))
            self.assertTrue(header.is_displayed(), "Header is not visible")

            # Verify top menu links
            self.verify_element_visible(By.ID, '_desktop_top_menu')

            # Verify category links
            clothes_link = self.driver.find_element(By.XPATH, '//a[@href="http://localhost:8080/en/3-clothes"]')
            self.assertTrue(clothes_link.is_displayed(), "Clothes link is not visible")

            accessories_link = self.driver.find_element(By.XPATH, '//a[@href="http://localhost:8080/en/6-accessories"]')
            self.assertTrue(accessories_link.is_displayed(), "Accessories link is not visible")

            art_link = self.driver.find_element(By.XPATH, '//a[@href="http://localhost:8080/en/9-art"]')
            self.assertTrue(art_link.is_displayed(), "Art link is not visible")

            # Verify search input
            search_input = self.driver.find_element(By.XPATH, '//input[@placeholder="Search our catalog"]')
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")

            # Verify login link
            login_link = self.driver.find_element(By.XPATH, '//a[@href="http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art"]')
            self.assertTrue(login_link.is_displayed(), "Login link is not visible")

            # Verify register link
            register_link = self.driver.find_element(By.XPATH, '//a[@href="http://localhost:8080/en/registration"]')
            self.assertTrue(register_link.is_displayed(), "Register link is not visible")

            # Click on a menu link and check UI updates
            login_link.click()
            self.wait.until(EC.url_contains("login"))
            self.assertIn("login", self.driver.current_url, "Redirect to login page failed")

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def verify_element_visible(self, by, value):
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        if not element.is_displayed():
            self.fail(f"Element with locator {by}='{value}' is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()