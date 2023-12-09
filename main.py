from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--disable-notifications")

chrome_options.add_argument("--disable-save-password-bubble")


driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()


username = input("Nickname:")
password = input("Password:")


driver.get("https://www.instagram.com")


WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
username_element = driver.find_element(By.NAME, "username")
password_element = driver.find_element(By.NAME, "password")

username_element.send_keys(username)
password_element.send_keys(password)


login_element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]")
login_element.click()


WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[4]/span/div/a")))
reelselement = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[4]/span/div/a")
reelselement.click()


input("Press Enter to close the browser...")

while True:
    continue
