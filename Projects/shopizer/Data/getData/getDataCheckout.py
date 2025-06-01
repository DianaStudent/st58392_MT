import os
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

process_name = "addtocart_checkout"
base_dir = r"C:\diana\MasterCode\code\Projects\shopizer\Processes"

output_dir = os.path.join(base_dir, "data", "getData", "sourceData")
output_file = os.path.join(output_dir, f"{process_name}_html.json")
screenshots_dir = os.path.join(base_dir, "data", "screenshots", "source", f"{process_name}_screen")

os.makedirs(output_dir, exist_ok=True)
os.makedirs(screenshots_dir, exist_ok=True)

BASE_URL = "http://localhost/"
LOGIN = "test22@user.com"
PASSWORD = "test**11"

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)
pages_data = {}
screenshot_counter = 1

def take_screenshot():
    global screenshot_counter
    time.sleep(1)
    filename = os.path.join(screenshots_dir, f"{process_name}_screen{screenshot_counter}.png")
    driver.save_screenshot(filename)
    screenshot_counter += 1

def save_html(name):
    pages_data[name] = driver.page_source
    take_screenshot()

try:
    driver.get(BASE_URL)
    driver.execute_script("document.body.style.zoom='75%'")
    time.sleep(2)
    save_html("home_page")
    driver.find_element(By.CSS_SELECTOR, "button.account-setting-active").click()
    time.sleep(1)
    cookie_banner = driver.find_element(By.CLASS_NAME, "CookieConsent")
    accept_btn = cookie_banner.find_element(By.TAG_NAME, "button")
    driver.execute_script("arguments[0].click();", accept_btn)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
    time.sleep(2)

    driver.find_element(By.NAME, "username").send_keys(LOGIN)
    driver.find_element(By.NAME, "loginPassword").send_keys(PASSWORD)
    save_html("login")
    login_btn = driver.find_element(By.XPATH, "//button[span[text()='Login']]")
    driver.execute_script("arguments[0].click();", login_btn)
    time.sleep(3)
    save_html("after_login")

    driver.get(BASE_URL)
    time.sleep(2)
    save_html("back_home")
    products = driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")[:2]
    for i, product in enumerate(products):
        hover_target = product.find_element(By.CLASS_NAME, "product-img")
        actions.move_to_element(hover_target).perform()
        time.sleep(1)
        add_btn = product.find_element(By.CSS_SELECTOR, "button[title='Add to cart']")
        driver.execute_script("arguments[0].scrollIntoView(true);", add_btn)
        driver.execute_script("arguments[0].click();", add_btn)
        time.sleep(2)
    save_html("after_add_to_cart")

    cart_button = driver.find_element(By.CSS_SELECTOR, "button.icon-cart")
    driver.execute_script("arguments[0].click();", cart_button)
    time.sleep(2)
    save_html("cart_popup")
    view_cart_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shopping-cart-btn a[href='/cart']")))
    driver.execute_script("arguments[0].click();", view_cart_btn)
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(2)
    save_html("cart_page")
    checkout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Proceed to Checkout')]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_btn)
    driver.execute_script("arguments[0].click();", checkout_btn)
    time.sleep(3)
    #save_html("checkout_page")

    driver.find_element(By.NAME, "company").send_keys("Comp1")
    driver.find_element(By.NAME, "address").send_keys("Street1")
    time.sleep(1)
    ok_btn = driver.find_element(By.CLASS_NAME, "dismissButton")
    driver.find_element(By.NAME, "city").send_keys("Quebec")

    def find_state_select(driver):
        selects = driver.find_elements(By.TAG_NAME, "select")
        for sel in selects:
            try:
                label = sel.find_element(By.XPATH, "preceding-sibling::label[1]")
                if "state" in label.text.strip().lower():
                    return sel
            except:
                continue
        return None

    region_select = WebDriverWait(driver, 10).until(lambda d: find_state_select(d))
    if not region_select:
        save_html("state_select_not_found")

    driver.execute_script("""arguments[0].selectedIndex = 1;arguments[0].dispatchEvent(new Event('change', { bubbles: true }));""", region_select)

    driver.find_element(By.NAME, "postalCode").send_keys("1234")
    driver.find_element(By.NAME, "phone").send_keys("1234567891")

    driver.find_element(By.NAME, "isAgree").click()
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(1)

    save_html("after_checkout")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=4, ensure_ascii=False)
    print(f"FIN: {output_file}")

finally:
    driver.quit()
