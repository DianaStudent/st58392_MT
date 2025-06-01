import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_main_ui_components(self):
        driver = self.driver
        wait = self.wait

        # Verify header presence
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header not found")

        # Check the presence of navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            art_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
        except:
            self.fail("One or more main navigation links are not found")

        # Check login and register buttons
        try:
            login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
            register_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))
        except:
            self.fail("Login or Register button not found")

        # Verify presence of the search form
        try:
            search_form = wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@method='get' and @action='//localhost:8080/en/search']")))
            search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='s']")))
        except:
            self.fail("Search form or input field not found")

        # Verify presence of the cart
        try:
            cart = wait.until(EC.visibility_of_element_located((By.ID, "_desktop_cart")))
        except:
            self.fail("Cart not found")

        # Check presence of footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()