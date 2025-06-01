from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import unittest

class TestLogin(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)

    def test_login(self):
        # 1. Open the homepage.
        self.driver.get("http://localhost/")

        # 2. Click the account icon in the top navigation bar.
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='header-middle']//a[@title='My Account']"))
        ).click()

        # 3. Click the "Login" link.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//ul[@id='top-links']//li[1]//a[@title='Login']"))).click()

        # 4. Fill in the email and password fields.
        self.driver.find_element(By.NAME, "email").send_keys("test2@user.com")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//form[@id='login']//input[@name='password']"))).send_keys("test**11")

        # 5. Submit the login form.
        self.driver.find_element(By.NAME, "login").click()

        # 6. Confirm success by checking:
        current_url = self.driver.current_url
        self.assertTrue("/my-account" in current_url)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()