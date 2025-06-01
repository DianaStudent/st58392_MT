import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestEcommerceApp(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        
    def test_homepage_elements(self):
        # Confirm the presence of key interface elements
        self._wait_for_element(By.ID, 'header')
        self._wait_for_element(By.XPATH, "//a[@title='Clothes']")
        self._wait_for_element(By.NAME, "email")
        self._wait_for_element(By.ID, "submit_login")

    def test_clothes_page_elements(self):
        # Interact with one or two elements
        self.driver.get("http://localhost:8080/en/3-clothes")
        self._wait_for_element(By.XPATH, "//h1[@class='page-title']")
        self._wait_for_element(By.ID, "add-to-cart")

    def test_interactive_elements(self):
        # Verify that interactive elements do not cause errors in the UI
        self.driver.get("http://localhost:8080/en/3-clothes")
        self._click_button_by_id("add-to-cart")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-success']")))

    def tearDown(self):
        self.driver.quit()

    def _wait_for_element(self, by, value):
        try:
            element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((by, value)))
            if not element.is_displayed():
                raise AssertionError(f"Element {value} is not visible")
        except TimeoutException:
            self.fail(f"Element {value} was not found")

    def _click_button_by_id(self, id):
        button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, id)))
        button.click()

if __name__ == '__main__':
    unittest.main()