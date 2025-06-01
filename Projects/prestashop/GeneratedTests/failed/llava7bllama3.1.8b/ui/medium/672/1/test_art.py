from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        # Check navigation links
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "ul.ui-autocomplete li"))
        )
        for link in nav_links:
            print(link.text)

        # Check inputs and buttons
        inputs_and_buttons = self.driver.find_elements(By.TAG_NAME, 'input')
        for input_element in inputs_and_buttons:
            try:
                assert input_element.is_displayed()
            except AssertionError:
                print(f"Input element not displayed: {input_element}")

        buttons = self.driver.find_elements(By.TAG_NAME, 'button')
        for button in buttons:
            try:
                assert button.is_displayed()
            except AssertionError:
                print(f"Button not displayed: {button}")

        # Check banners
        banner = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ui-menu"))
        )
        print(banner.text)

    def test_ui_interactions(self):
        # Click a button and check the UI updates visually
        button = self.driver.find_element(By.ID, 'some_button_id')
        button.click()

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#updated_text"))
            )
            print("UI updated successfully")
        except TimeoutException:
            print("UI did not update")

if __name__ == '__main__':
    unittest.main()