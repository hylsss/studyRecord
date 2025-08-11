import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from datetime import datetime
from selenium.common.exceptions import WebDriverException, TimeoutException
import tkinter as tk
from tkinter import messagebox
from utils import click_button_and_handle_popup, get_current_time, close_popup_if_exists

# 设置日志文件夹和日志文件名
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

get_current_time()


def show_retry_popup(error_msg):
    """显示错误弹窗，并提供重试选项"""
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 弹窗选项：重试 or 关闭
    user_choice = messagebox.askretrycancel(
        "打卡失败",
        f"{error_msg}\n\n请检查网络后点击「重试」，或点击「取消」退出。"
    )

    root.destroy()
    return user_choice  # 返回 True（重试） or False（取消）


def initialize_driver():
    """初始化WebDriver"""
    chromedriver_path = '/usr/local/bin/chromedriver'
    service = Service(chromedriver_path)
    return webdriver.Chrome(service=service)


def run_check_in_process():
    """执行打卡流程"""
    driver = None
    try:
        driver = initialize_driver()

        # 打开指定网址
        logging.info('打开网址: https://myoa.omenow.com/Schedule/MySchedule/')
        driver.get('https://myoa.omenow.com/Schedule/MySchedule/')

        # 输入用户名和密码
        logging.info('输入用户名和密码')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
        ).send_keys('INA.h')

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
        ).send_keys('000000')

        # 点击登录按钮
        logging.info('点击登录按钮')
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="loginbtn"]/button'))
        ).click()

        time.sleep(20)

        # 检查并关闭弹窗（如果有）
        close_popup_if_exists(driver)

        # 获取当前星期几
        now = datetime.now()
        current_weekday = now.weekday()  # 星期一到星期日对应0到6
        current_time = now.time()

        if current_weekday in range(0, 5):  # 周一到周五
            logging.info('---------------------------------------------------')
            logging.info('今天是工作日，执行签出签入流程。')
            logging.info(f"今天是星期{current_weekday}")

            # 检查并点击签出按钮
            logging.info('检查签出按钮状态')
            btnCheckOut_xpath = '//*[@id="btnCheckOut"]'
            btnCheckIn_xpath = '//*[@id="btnCheckIn"]'
            popup_xpath = '//*[@id="popupWindow"]/div/input'

            btnCheckOut = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, btnCheckOut_xpath))
            )

            if btnCheckOut.is_enabled():
                click_button_and_handle_popup(driver, btnCheckOut_xpath, popup_xpath, '签出')
                time.sleep(5)
            else:
                logging.info('签出按钮当前处于禁用状态，无法点击。')

            time.sleep(20)

            # 检查并点击签入按钮
            logging.info('检查签入按钮状态')
            btnCheckIn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, btnCheckIn_xpath))
            )

            if not btnCheckIn.is_enabled():
                logging.info('签入按钮当前处于禁用状态，无法点击。')
                time.sleep(5)
                driver.get('https://.omenow.com/Schedule/MySchedule/')
                time.sleep(10)
            else:
                # 再次检查签出按钮状态
                logging.info('检查签出按钮状态以决定是否点击签入按钮')
                btnCheckOut = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, btnCheckOut_xpath))
                )

                if btnCheckOut.is_enabled():
                    click_button_and_handle_popup(driver, btnCheckOut_xpath, popup_xpath, '签出')
                    time.sleep(20)

                click_button_and_handle_popup(driver, btnCheckIn_xpath, popup_xpath, '签入')
                time.sleep(10)

        elif current_weekday == 5 and current_time.strftime("%H:%M") < "06:00":  # 周六
            logging.info('---------------周六移动办公签入---------------------')
            special_button_xpath = '//*[@id="btnHomeWorkingCheckIn"]'
            popup_button = '//*[@id="popupWindow"]/div/input'

            mobileCheckInBtn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, special_button_xpath))
            )

            if mobileCheckInBtn.is_enabled():
                click_button_and_handle_popup(driver, special_button_xpath, popup_button, '周六移动办公签入')

            time.sleep(5)

        elif current_weekday == 5 and current_time.strftime("%H:%M") > "13:30":  # 周六
            logging.info('---------------周六移动办公签出---------------------')
            special_button_out = '//*[@id="btnHomeWorkingCheckOut"]'
            popup_button = '//*[@id="popupWindow"]/div/input'

            mobileCheckOutBtn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, special_button_out))
            )

            if mobileCheckOutBtn.is_enabled():
                click_button_and_handle_popup(driver, special_button_out, popup_button, '周六移动办公签出')

            time.sleep(5)

    except (WebDriverException, TimeoutException) as e:
        error_msg = f"网页加载失败: {str(e)}"
        logging.error(error_msg)

        # 显示弹窗，让用户选择是否重试
        if show_retry_popup(error_msg):
            if driver:
                driver.quit()
            run_check_in_process()  # 递归调用，重新执行打卡流程
        else:
            logging.info("用户选择取消，程序退出")
            if driver:
                driver.quit()
            return

    except Exception as e:
        error_msg = f"发生未知异常: {str(e)}"
        logging.error(error_msg)
        show_retry_popup(error_msg)
        if driver:
            driver.quit()
        raise

    finally:
        if driver:
            driver.get('https://mycenter.omenow.com/attendance/index/')
            time.sleep(10)
            driver.quit()


if __name__ == "__main__":
    run_check_in_process()