import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from datetime import datetime
from utils import click_button_and_handle_popup, get_current_time

log_folder = '/Users/ina.h/Documents/autoCheckIn/pythonLogs'
log_file = 'operation_log.log'

# 确保日志文件夹存在
os.makedirs(log_folder, exist_ok=True)

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(log_folder, log_file)),
        logging.StreamHandler()
    ]
)

# 获取当前时间（如有需要，进一步处理）
current_time = get_current_time()
logging.info(f"Current time: {current_time}")

# 初始化WebDriver
service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

try:
    # 打开指定网址
    logging.info('打开网址: https://myoa.omenow.com/Schedule/MySchedule/')
    driver.get('https://myoa.omenow.com/Schedule/MySchedule/')

    # 输入用户名和密码
    logging.info('输入用户名和密码')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
    ).send_keys('INA.H')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
    ).send_keys('000000')  # 确保在此输入正确的密码

    # 点击登录按钮
    logging.info('点击登录按钮')
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="loginbtn"]/button'))
    ).click()

    time.sleep(20)

    # 检查今天是否是周六
    current_weekday = datetime.now().weekday()  # 星期一到星期日对应0到6

    if current_weekday == 5:
        logging.info('---------------------------------------------------')
        logging.info('周六移动办公签出')
        special_button_out = '//*[@id="btnHomeWorkingCheckOut"]'  # 你需要替换这个XPath
        popup_button = '//*[@id="popupWindow"]/div/input'

        mobileCheckOutBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, special_button_out))
        )

        if mobileCheckOutBtn.is_enabled():
            click_button_and_handle_popup(driver, special_button_out, popup_button, '周六移动办公签出')

        # 点击按钮后等待
        time.sleep(5)

    else:
        logging.info('周六才需要移动办公签出')

except Exception as e:
    logging.error(f"发生异常: {str(e)}")

finally:
    logging.info('关闭浏览器')
    driver.get('https://mycenter.omenow.com/attendance/index/')
    time.sleep(10)
    driver.quit()
