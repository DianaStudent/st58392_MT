import unittest
import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegisterUserTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
        
    def generate_random_email(self):
        return f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@user.com"
    
    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        driver.get("http://localhost/")

        # Accept cookies if the button is present
        try:
            accept_cookies_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            pass  # Proceed if the button is not present

        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.account-setting-active")))
        account_button.click()

        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        register_link.click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.login-register-area")))

        email = self.generate_random_email()
        driver.find_element(By.NAME, "email").send_keys(email)
        password = "test**11"
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "repeatPassword").send_keys(password)
        driver.find_element(By.NAME, "firstName").send_keys("Test")
        driver.find_element(By.NAME, "lastName").send_keys("User")

        country_select = driver.find_element(By.XPATH, "//select[./option[text()='Select a country']]")
        ActionChains(driver).move_to_element(country_select).click().perform()
        country_option = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[.//option[text()='Select a country']]/option")))[1]
        ActionChains(driver).move_to_element(country_option).click().perform()

        state_select = driver.find_element(By.XPATH, "//select[./option[text()='Select a state']]")
        ActionChains(driver).move_to_element(state_select).click().perform()
        state_option = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//select[.//option[text()='Select a state']]/option")))[1]
        ActionChains(driver).move_to_element(state_option).click().perform()

        driver.find_element(By.NAME, "lastName").click()  # Click to hide dropdowns

        register_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        register_button.click()

        wait.until(EC.url_contains("/my-account"))
        current_url = driver.current_url
        self.assertIn("/my-account", current_url, "Registration failed, not redirected to /my-account")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()