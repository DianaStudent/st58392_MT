import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestEcommerceWebsite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_page_structure(self):
        self.driver.get("http://localhost:8080/en/")
        
        # Ensure structural elements are visible
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//header")))
        self.assertTrue(header.is_displayed())
        
        footer = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//footer")))
        self.assertTrue(footer.is_displayed())

        # Check presence and visibility of input fields, buttons, labels, and sections
        nav_items = ["clothes", "accessories", "art"]
        for item in nav_items:
            link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, f"//a[text()='{item}']")))
            self.assertTrue(link.is_displayed())

        login_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Login']")))
        self.assertTrue(login_link.is_displayed())
        
        register_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Register']")))
        self.assertTrue(register_link.is_displayed())

    def test_page_interaction(self):
        self.test_page_structure()
        
        # Interact with key UI elements (e.g., click buttons)
        clothes_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Clothes']")))
        clothes_button.click()

    def test_ui_reaction(self):
        self.test_page_structure()
        
        # Confirm that the UI reacts visually
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Art')]")))

    def test_required_elements_present(self):
        self.test_page_structure()
        
        # Assert that no required UI element is missing
        elements = ["header", "footer", "nav items", "login link", "register link"]
        for item in elements:
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//{item}")))
            except Exception as e:
                self.fail(f"Missing required element: {item}")

if __name__ == "__main__":
    unittest.main()