import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestECommerce(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_home_page_elements(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#header"))
        )

        # Check navigation links
        links = self.driver.find_elements(By.XPATH, "//ul[@class='nav-main']/li/a")
        for link in links:
            if not link.text.strip():
                self.fail("Navigation links are missing")

        # Check inputs and buttons
        inputs_and_buttons = self.driver.find_elements(By.TAG_NAME, "input") + self.driver.find_elements(By.TAG_NAME, "button")
        for element in inputs_and_buttons:
            if not element.is_displayed():
                self.fail("Inputs or buttons are missing")

        # Interact with an element (e.g., click a button)
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn btn-default"))
        )
        add_to_cart_button.click()

    def test_home_page_updates_visually(self):
        # Wait for any UI changes
        WebDriverWait(self.driver, 10)

        # Check if the UI has updated visually (e.g., a new message appears)
        try:
            message = self.driver.find_element(By.CSS_SELECTOR, ".message")
            print(message.text.strip())
        except Exception as e:
            self.fail(f"UI did not update visually: {str(e)}")

    def test_interactive_elements_do_not_cause_errors(self):
        # Interact with an element (e.g., fill in a form field)
        search_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "search_query_top"))
        )
        search_input.send_keys("test")

        try:
            self.driver.find_element(By.CSS_SELECTOR, "#search")
        except Exception as e:
            self.fail(f"Error occurred: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()