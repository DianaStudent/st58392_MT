from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/")

        try:
            # Check navigation links
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Contact us"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Clothes"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Accessories"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Art"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Sign in"))
            )

            # Check inputs and buttons
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='s']"))
            )
            subscribe_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='submitNewsletter']"))
            )
            
            # Check presence of a banner
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='sample-1']"))
            )

            # Interact with elements: Click on 'Clothes'
            clothes_link = driver.find_element(By.LINK_TEXT, "Clothes")
            clothes_link.click()

            # Verify the URL has changed to the clothes category page
            WebDriverWait(driver, 20).until(
                EC.url_to_be("http://localhost:8080/en/3-clothes")
            )

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()