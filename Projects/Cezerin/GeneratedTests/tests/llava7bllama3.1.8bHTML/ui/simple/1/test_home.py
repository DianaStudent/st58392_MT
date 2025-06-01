import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestMainUIComponents(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("http://localhost:8000") # Replace with your URL

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_headers(self):
        headers = [
            "home",
            "category_a",
            "category_a_1"
        ]
        for header in headers:
            header_element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, f"//h2[contains(text(), '{header}')]"))
            )
            self.failUnless(header_element.is_displayed())

    def test_buttons(self):
        buttons = ["button_addtocart_text"]
        for button in buttons:
            button_element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, f"//button[contains(text(), '{button}')]"))
            )
            self.failUnless(button_element.is_displayed())

    def test_links(self):
        links = ["BEST SELLERS"]
        for link in links:
            link_element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, f"//a[contains(text(), '{link}')]"))
            )
            self.failUnless(link_element.is_displayed())

    def test_form_fields(self):
        form_fields = ["checkout-field"]
        for field in form_fields:
            field_element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, f"//input[@class='{field}']"))
            )
            self.failUnless(field_element.is_displayed())

if __name__ == "__main__":
    unittest.main()