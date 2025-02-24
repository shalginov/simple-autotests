from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_login(browser):
    browser.get("http://192.168.27.17:8081/en-gb?route=account/login")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.ID, "form-login")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-email")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-password")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary")))
    browser.find_element(By.LINK_TEXT, "Forgotten Password")