from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import time
# ตั้งค่า Chrome WebDriver ให้ใช้ Healenium Proxy
options = webdriver.ChromeOptions()
options.add_argument("--no--sandbox")
driver = webdriver.Remote('http://localhost:8085', options=options)



# เข้าเว็บไซต์
driver.get("http://host.docker.internal:5000/")

# ค้นหา Element (หากเจอปัญหา Healenium จะพยายามแก้ไขเอง)
time.sleep(3)
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")

username_input.send_keys("testuser")
password_input.send_keys("password123")

# กดปุ่ม Login
login_button = driver.find_element(By.TAG_NAME, "button")
login_button.click()
time.sleep(3)
print("success")

# คลิกที่ Element
# element.click()
