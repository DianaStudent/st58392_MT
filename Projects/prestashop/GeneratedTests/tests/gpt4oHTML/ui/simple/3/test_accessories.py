import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAccessoriesPageUI(unittest.TestCase):

    def setUp(self):
        # Set up the driver with Chrome and ChromeDriver manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_main_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for header
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertIsNotNone(header)
        except Exception as e:
            self.fail(f"Header not found or not visible: {str(e)}")

        # Check for navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
            self.assertIsNotNone(home_link)

            clothes_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            self.assertIsNotNone(clothes_link)

            accessories_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            self.assertIsNotNone(accessories_link)

            art_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
            self.assertIsNotNone(art_link)

        except Exception as e:
            self.fail(f"Navigation link not found or not visible: {str(e)}")

        # Check for login button
        try:
            login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
            self.assertIsNotNone(login_button)
        except Exception as e:
            self.fail(f"Login button not found or not visible: {str(e)}")

        # Check for registration link
        try:
            register_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))
            self.assertIsNotNone(register_link)
        except Exception as e:
            self.fail(f"Register link not found or not visible: {str(e)}")

        # Check for search form
        try:
            search_form = wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
            search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @name='s' and @placeholder='Search our catalog']")))
            self.assertIsNotNone(search_form)
            self.assertIsNotNone(search_input)
        except Exception as e:
            self.fail(f"Search form or input not found or not visible: {str(e)}")
            
        # Check for product list
        try:
            product_list = wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
            self.assertIsNotNone(product_list)
        except Exception as e:
            self.fail(f"Product list not found or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()