from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestDemoPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = self.wait

        # Verify navigation links
        nav_links = [
            (By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']"),
            (By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']"),
            (By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")
        ]

        for by, path in nav_links:
            element = wait.until(EC.visibility_of_element_located((by, path)))
            if not element:
                self.fail(f"Navigation link {path} is not visible.")

        # Verify login and register links
        login_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
        register_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))
        
        if not login_link or not register_link:
            self.fail("Login or Register link is not visible.")

        # Verify search input
        search_input = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        if not search_input:
            self.fail("Search input is not visible.")

        # Verify banner image
        banner = wait.until(EC.visibility_of_element_located((By.XPATH, "//img[contains(@src, 'sale70.png')]")))
        if not banner:
            self.fail("Banner image is not visible.")

        # Interact with an element
        cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='_desktop_cart']//a")))
        cart_button.click()

        # Verify UI update
        cart_header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-header")))
        if not cart_header:
            self.fail("UI did not update after clicking cart button.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()