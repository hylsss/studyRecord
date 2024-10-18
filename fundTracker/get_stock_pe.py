import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# 设置Selenium的Chrome选项
chrome_options = Options()
chrome_options.add_argument("--headless")  # 不打开浏览器界面

# 设置ChromeDriver的路径
chrome_driver_path = '/usr/local/bin/chromedriver'  # 修改为你本地的chromedriver路径

# 初始化webdriver
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 定义获取市盈率的函数
def get_pe_ratio(stock_code):
    try:
        # 使用f-string生成股票页面的URL
        url = f"https://quote.eastmoney.com/hk/{stock_code}.html"
        driver.get(url)  # 使用Selenium获取网页

        # 等待页面加载并查找市盈率元素
        wait = WebDriverWait(driver, 10)  # 设置最长等待时间为10秒
        pe_ratio_element = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//td[contains(text(),"市盈率")]/following-sibling::td/span/span')))

        if pe_ratio_element:
            return pe_ratio_element.text.strip()  # 返回市盈率
        else:
            return "PE值未找到"

    except TimeoutException:
        return "获取数据时出错: 页面加载超时"
    except Exception as e:
        return f"获取数据时出错: {e}"

# 加载CSV文件
file_path = 'fund_holdings.csv'  # 修改为你本地文件的路径
fund_data = pd.read_csv(file_path)

# 股票代码补全为5位数并添加".HK"后缀
fund_data['股票代码'] = fund_data['股票代码'].apply(lambda x: str(x).zfill(5))

# 循环获取每个股票的市盈率并匹配到fund_data中的股票代码
pe_ratios = {}

for index, row in fund_data.iterrows():
    stock_code = row['股票代码']
    pe_ratios[stock_code] = get_pe_ratio(stock_code + ".HK")  # 加上".HK"后缀

# 将市盈率插入到数据框中
fund_data['市盈率'] = fund_data['股票代码'].apply(lambda x: pe_ratios.get(x, "PE值未找到"))

# 保存更新后的数据框到CSV文件中
output_file_path = 'updated_fund_holdings.csv'  # 输出的文件路径
fund_data.to_csv(output_file_path, index=False)

# 关闭浏览器
driver.quit()

print(f"更新后的数据保存为: {output_file_path}")
