import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestShopReactApp(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_shop_react_app(self):
        # Step 1: Ensure structural elements are visible
        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        footer = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))

        # Step 2: Check presence and visibility of key UI elements
        links = self.driver.find_elements(By.TAG_NAME, "a")
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        input_fields = self.driver.find_elements(By.TAG_NAME, "input")
        labels = self.driver.find_elements(By.TAG_NAME, "label")
        sections = self.driver.find_elements(By.TAG_NAME, "section")

        # Step 3: Interact with key UI elements
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']")))
        login_link.click()

        # Step 4: Confirm that the UI reacts visually
        registration_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Registration']")))
        self.assertTrue(registration_button.is_displayed())

        # Step 5: Assert that no required UI element is missing
        required_elements = ["header", "footer", "links", "buttons", "input_fields", "labels", "sections"]
        for element in required_elements:
            if not hasattr(self, f"{element}_present"):
                self.fail(f"Required element {element} is missing")

if __name__ == "__main__":
    unittest.main()