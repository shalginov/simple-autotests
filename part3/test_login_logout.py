from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_unlogin(browser):
    browser.get("http://192.168.27.17:8081/administration/")
    browser.find_element(By.ID, "input-username").send_keys("user")
    browser.find_element(By.ID, "input-password").send_keys("bitnami")
    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()

    wait = WebDriverWait(browser,2)
    wait.until(EC.visibility_of_element_located((By.ID, "nav-profile")))
    wait.until(EC.element_to_be_clickable((By.ID, "nav-logout"))).click()

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.ID, "form-login")))
