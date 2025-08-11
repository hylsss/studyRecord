import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime


def get_current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def click_button_and_handle_popup(driver, button_xpath, popup_xpath, button_name):
    try:
        # 等待并点击按钮
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, button_xpath))
        )
        button.click()
        logging.info(f"{button_name} 按钮已点击。")

        # 等待并处理弹出窗口
        time.sleep(5)  # 等待弹出窗口加载
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, popup_xpath))
            ).click()
            logging.info(f'{button_name} 弹窗关闭按钮已点击。')
        except Exception as e:
            logging.error(f"处理 {button_name} 弹出窗口时出现异常: {e}")

    except Exception as e:
        logging.error(f"点击 {button_name} 按钮时出现异常: {e}")


def close_popup_if_exists(driver):
    """
    判断页面是否有弹窗，并点击关闭按钮
    """
    try:
        # 等待弹窗出现
        dialog_buttons = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'dialog_buttons'))
        )

        # 查找并点击关闭按钮
        close_button = dialog_buttons.find_element(By.CLASS_NAME, 'confirm_no')
        close_button.click()
        logging.info("弹窗已关闭")
    except Exception as e:
        logging.info("未找到弹窗或弹窗已经关闭")