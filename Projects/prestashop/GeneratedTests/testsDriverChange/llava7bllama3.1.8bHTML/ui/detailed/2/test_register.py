import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TestUI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up ChromeDriver with options to run headless
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("http://localhost:8080/en/")

    def test_page_structure(self):
        # Check that structural elements are present and visible
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//header")))
        self.assertTrue(header.is_displayed())

        footer = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//footer")))
        self.assertTrue(footer.is_displayed())

    def test_input_fields_buttons_labels(self):
        # Check that input fields, buttons, labels, and sections are present and visible
        login_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        self.assertTrue(login_link.is_visible())

        register_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@name='submit']")))
        self.assertTrue(register_button.is_displayed())

    def test_ui_interaction(self):
        # Interact with key UI elements and confirm that the UI reacts visually
        login_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        login_link.click()

        WebDriverWait(self.driver, 20).until(EC.title_contains("Login"))

    def test_required_elements_present(self):
        # Check that no required UI element is missing
        try:
            self.driver.find_element(By.XPATH, "//header")
            self.driver.find_element(By.XPATH, "//footer")
            self.driver.find_element(By.LINK_TEXT, "Login")
            self.driver.find_element(By.XPATH, "//button[@name='submit']")
        except:
            self.fail("Required UI elements are missing")

if __name__ == "__main__":
    unittest.main()