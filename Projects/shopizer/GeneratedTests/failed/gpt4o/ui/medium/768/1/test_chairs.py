from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestShopizerUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_presence(self):
        driver = self.driver

        try:
            # Verify navigation links are present and visible
            home_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[text()='Home']"))
            )

            tables_link = driver.find_element(By.XPATH, "//a[text()='Tables']")
            self.assertTrue(tables_link.is_displayed(), "Tables link is not visible")

            chairs_link = driver.find_element(By.XPATH, "//a[text()='Chairs']")
            self.assertTrue(chairs_link.is_displayed(), "Chairs link is not visible")

            # Verify 'Accept' cookies button is present and click it
            accept_cookies_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()

            # Verify that interaction does not cause errors
            try:
                # Clicking the login button should not cause any errors
                login_button = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//a[text()='Login']"))
                )
                login_button.click()
            except Exception as e:
                self.fail(f"Interacting with login button caused an error: {str(e)}")

        except Exception as e:
            self.fail(f"An expected UI element is missing: {str(e)}")

if __name__ == "__main__":
    unittest.main()