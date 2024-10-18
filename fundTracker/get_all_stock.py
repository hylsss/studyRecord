from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 设置Selenium的Chrome选项
chrome_options = Options()
# chrome_options.add_argument("--headless")  # 不打开浏览器界面

# 设置ChromeDriver的路径
chrome_driver_path = '/usr/local/bin/chromedriver'  # 这里填入你的chromedriver路径

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
        wait = WebDriverWait(driver, 30)  # 设置最长等待时间为10秒
        pe_ratio_element = wait.until(
            EC.presence_of_element_located((By.XPATH, '//td[contains(text(),"市盈率")]/span/span')))

        if pe_ratio_element:
            return pe_ratio_element.text.strip()  # 返回市盈率
        else:
            return "PE值未找到"

    except Exception as e:
        return f"获取数据时出错: {e}"


# 股票代码列表
stock_codes = ['00700', '03690', '01810', '09988', '09618', '01024', '09999', '02015', '00992', '00981',
               '09961', '06690', '09888', '09868', '09626', '02382', '00020', '00285', '06618', '03888',
               '00241', '00780', '01347', '00268', '00772', '06060', '01833', '01797', '09866', '09898']

# 循环获取每个股票的市盈率
pe_ratios = {}
for stock_code in stock_codes:
    pe_ratios[stock_code] = get_pe_ratio(stock_code)

# 输出每个股票的市盈率
for stock, pe in pe_ratios.items():
    print(stock, pe)

file_path = 'fund_holdings.csv'  # 修改为你本地的CSV文件路径
fund_data = pd.read_csv(file_path)


# pe_ratios_dict = dict(stock_pe_list)
#
# file_path = 'fund_holdings.csv'
# fund_data = pd.read_csv(file_path)
#
# # 正确地使用字典 'pe_ratios' 进行映射，而不是使用 'stock_pe_list' 列表
# fund_data['市盈率'] = fund_data['股票代码'].map(pe_ratios_dict)
#
# output_file_path = 'updated_fund_holdings_with_pe.csv'
# fund_data.to_csv(output_file_path, index=False)

# 关闭浏览器
driver.quit()
