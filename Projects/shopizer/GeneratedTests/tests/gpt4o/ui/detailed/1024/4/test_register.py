import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header is visible
        header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        self.assertIsNotNone(header, "Header is not visible")

        # Check footer is visible
        footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
        self.assertIsNotNone(footer, "Footer is not visible")

        # Check navigation links are visible
        for link_text in ['Home', 'Tables', 'Chairs']:
            link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.assertIsNotNone(link, f"Navigation link '{link_text}' is not visible")

        # Check Login/Register fields and buttons
        self.driver.get("http://localhost/login")
        self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        self.wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))

        login_tab = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Login']")))
        register_tab = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Register']")))
        login_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']")))
        register_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Register']")))

        # Assert all necessary elements are visible
        self.assertIsNotNone(login_tab, "Login tab is not visible")
        self.assertIsNotNone(register_tab, "Register tab is not visible")
        self.assertIsNotNone(login_button, "Login button is not visible")
        self.assertIsNotNone(register_button, "Register button is not visible")

        # Assert the page is interactive (click on register tab)
        register_tab.click()
        self.assertTrue(register_tab.is_selected(), "Register tab cannot be selected")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()