import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        try:
            # Check navigation links
            home_link = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']"))
            )
            clothes_link = self.driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")
            accessories_link = self.driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")
            art_link = self.driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")

            # Check buttons and form fields
            search_input = self.driver.find_element(By.XPATH, "//input[@name='s']")
            sign_in_link = self.driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F6-accessories']")

            # Check that elements are visible
            self.assertTrue(home_link.is_displayed(), "Home link is not visible.")
            self.assertTrue(clothes_link.is_displayed(), "Clothes link is not visible.")
            self.assertTrue(accessories_link.is_displayed(), "Accessories link is not visible.")
            self.assertTrue(art_link.is_displayed(), "Art link is not visible.")
            self.assertTrue(search_input.is_displayed(), "Search input is not visible.")
            self.assertTrue(sign_in_link.is_displayed(), "Sign in link is not visible.")

            # Interact with an element
            search_input.send_keys("Mug")
            search_button = self.driver.find_element(By.XPATH, "//button[@aria-label='Search']")
            search_button.click()

            # Check for UI update after interaction
            products = self.wait.until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-miniature"))
            )
            self.assertGreater(len(products), 0, "No products found after search.")

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()