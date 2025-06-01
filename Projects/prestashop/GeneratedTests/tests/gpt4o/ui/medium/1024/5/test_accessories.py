import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check presence of key UI elements
        try:
            # Check for navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

            # Check for input fields
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='text'][name='s']")))

            # Check for buttons
            filter_button = wait.until(EC.visibility_of_element_located((By.ID, "search_filter_toggler")))
            subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='submitNewsletter']")))

            # Check for banners
            banner = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.category-cover img")))

            # Interacting with an element (click a button and check for item on page)
            filter_button.click()
            availability_filter = wait.until(EC.visibility_of_element_located((By.ID, "facet_input_34213_0")))
            availability_filter.click()
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".facet-label :checked")))

        except Exception as e:
            self.fail(f"Test failed due to missing element or interaction failure: {str(e)}")

if __name__ == "__main__":
    unittest.main()