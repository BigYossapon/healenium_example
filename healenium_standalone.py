from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# ใช้ Chrome WebDriver ปกติ
chrome_options = Options()
# chrome_options.add_argument("--headless")  # รันแบบไม่มี UI
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# ใช้ ChromeDriver ปกติ
# service = Service("/path/to/chromedriver")  # เปลี่ยนเป็น path จริงของ ChromeDriver
driver = webdriver.Chrome( options=chrome_options)

# ใช้ Healenium Proxy
driver.command_executor._proxy_url = "http://localhost:8085"



# เข้าเว็บไซต์
# driver.get("http://host.docker.internal:5000/")
driver.get("http://localhost:5000/")
# ค้นหา Element (หากเจอปัญหา Healenium จะพยายามแก้ไขเอง)
time.sleep(3)
username_input = driver.find_element(By.ID, "isis")
password_input = driver.find_element(By.ID, "password")

username_input.send_keys("testuser")
password_input.send_keys("password123")

# กดปุ่ม Login
login_button = driver.find_element(By.TAG_NAME, "button")
login_button.click()
time.sleep(3)
print("success")

# ปิดเบราว์เซอร์
driver.quit()
