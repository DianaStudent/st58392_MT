import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestShopReactApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_shop_react_app(self):
        # Step 1: Confirm the presence of key interface elements
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/category/tables']"))
        )
        
        navigation_links = self.driver.find_elements(By.XPATH, "//nav/a")
        self.assertEqual(len(navigation_links), 5)

        headers = self.driver.find_elements(By.TAG_NAME, "h1")
        self.assertEqual(len(headers), 3)
        
        # Step 2: Interact with one or two elements
        button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        button.click()

        # Wait for the UI to update visually after clicking the button
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[text()='Button clicked!']"))
        )

        # Step 3: Verify that interactive elements do not cause errors in the UI
        form_fields = self.driver.find_elements(By.TAG_NAME, "input")
        for field in form_fields:
            try:
                field.send_keys("test")
            except Exception as e:
                print(f"Error sending keys to input element: {e}")
                self.fail(f"Failed to send keys to input element")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()