import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_main_ui_components(self):
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "header")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "nav")))

        # Check for header elements
        self.assertEqual(1, len(self.driver.find_elements(By.TAG_NAME, "h1")))  # Title

        # Check buttons and links in the navigation bar
        nav_links = self.driver.find_elements(By.TAG_NAME, "ul")[0].find_elements(By.TAG_NAME, "li")
        for i, link in enumerate(nav_links):
            if i == 2:  # Clothes category link
                clothes_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='/en/3-clothes'])[1]")))
                self.assertEqual("Clothes", clothes_link.text)
            elif i == 5:  # Accessories category link
                accessories_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='/en/6-accessories'])[1]")))
                self.assertEqual("Accessories", accessories_link.text)

        # Check other navigation bar links
        for i, link in enumerate(nav_links):
            if i != 2 and i != 5:
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"(//a[@href='{link.get_attribute("href")}'])[1]")))

    def test_login_and_register_links(self):
        # Check login link
        login_link = self.driver.find_element(By.LINK_TEXT, "Login")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='/en/login'])[1]")))
        self.assertEqual("http://localhost:8080/en/login", login_link.get_attribute("href"))

        # Check register link
        register_link = self.driver.find_element(By.LINK_TEXT, "Register")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='/en/registration'])[1]")))
        self.assertEqual("http://localhost:8080/en/registration", register_link.get_attribute("href"))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()