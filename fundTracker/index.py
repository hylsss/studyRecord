import requests
import re
import pandas as pd
from datetime import datetime

# 基金代码列表（你可以将多个基金的代码加入列表中）
fund_codes = ['513180', '159691']  # 替换为你实际的基金代码

# 限制日期，从这个日期之后的数据
limit_date = "2024-09-13"

# 遍历每个基金代码，分别处理数据并生成 Excel
for fund_code in fund_codes:
    # 构建 API URL
    api_url = f'https://fund.eastmoney.com/pingzhongdata/{fund_code}.js'

    # 发送请求获取页面内容
    response = requests.get(api_url)
    response.encoding = 'utf-8'

    # 使用正则表达式从返回的JS文件中提取净值数据
    net_worth_pattern = re.compile(r'var Data_netWorthTrend = (.*?);')  # 匹配净值和涨幅数据

    # 提取净值和涨幅数据部分
    matches = net_worth_pattern.search(response.text)

    if matches:
        # 将净值数据解析为 Python 列表
        net_worth_data = eval(matches.group(1))

        # 构建 DataFrame
        data = []
        initial_net_worth = None  # 用于存储 2024-09-13 的净值

        for entry in net_worth_data:
            # 日期是时间戳格式，需要转换
            date = datetime.fromtimestamp(entry['x'] / 1000).strftime('%Y-%m-%d')

            # 仅处理2024-09-13之后的日期
            if date >= limit_date:
                net_worth = entry['y']  # 当前净值
                growth_rate = entry.get('equityReturn', 0)  # 涨幅，部分可能缺失，默认设置为0

                # 记录首次日期的净值（2024-09-13）
                if date == limit_date:
                    initial_net_worth = net_worth

                # 确保初始净值不为空
                if initial_net_worth:
                    # 计算从2024-09-13以来的净值涨幅
                    net_worth_change = ((net_worth - initial_net_worth) / initial_net_worth) * 100

                    # 保存数据到列表，只保留日期、净值、涨幅、相对09/13后的涨幅
                    data.append({
                        "日期": date,
                        "净值": net_worth,
                        "每天涨幅 (%)": f"{growth_rate}%",
                        "相对09/13涨幅 (%)": f"{round(net_worth_change, 2)}%"
                    })

        # 将数据转换为 DataFrame
        df = pd.DataFrame(data)

        # 保存数据到 Excel 文件，使用基金代码作为文件名的一部分
        excel_filename = f"fund_{fund_code}_nav_and_growth.xlsx"
        df.to_excel(excel_filename, index=False)

        print(f"基金 {fund_code} 的数据已保存到 {excel_filename}")

    else:
        print(f"未能匹配到基金 {fund_code} 的净值数据。")
