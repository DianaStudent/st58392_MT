from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_key_ui_elements_present(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Assert header is visible
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertIsNotNone(header, "Header is missing")

        # Assert footer is visible
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertIsNotNone(footer, "Footer is missing")

        # Assert navigation links are visible
        nav_links = ["http://localhost:8080/en/", "http://localhost:8080/en/3-clothes",
                     "http://localhost:8080/en/6-accessories", "http://localhost:8080/en/9-art"]
        for link in nav_links:
            nav_element = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{link}']")))
            self.assertIsNotNone(nav_element, f"Navigation link {link} is missing")

        # Assert login link is visible
        login_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
        self.assertIsNotNone(login_link, "Login link is missing")
        
        # Assert registration link is visible
        register_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))
        self.assertIsNotNone(register_link, "Registration link is missing")

        # Assert search input field is visible
        search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='s']")))
        self.assertIsNotNone(search_input, "Search input field is missing")

        # Assert product element is visible
        product_elements = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product")))
        self.assertGreater(len(product_elements), 0, "No products are displayed")

        # Assert button interactions and visibility
        wishlist_buttons = driver.find_elements(By.CLASS_NAME, "wishlist-button-add")
        for button in wishlist_buttons:
            self.assertTrue(button.is_displayed(), "Wishlist button is not visible")
            button.click()
            # Add more assertions or checks here to confirm interaction state if needed

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()