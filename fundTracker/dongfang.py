import re
from datetime import datetime

import pandas as pd
import requests

# 基金的 API URL
api_url = 'https://fund.eastmoney.com/pingzhongdata/159691.js'

# 用户输入：成本价和持有份额
cost_price = 1.008  # 成本价
holding_shares = 400  # 持有份额
limit_date = "2024-09-13"  # 限制日期，从这个日期之后的数据

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

                # 计算总收益：持有份额 * (当日净值 - 成本价)
                total_cost = cost_price * holding_shares  # 总成本
                total_value = net_worth * holding_shares  # 当前市值
                daily_profit = total_value - total_cost  # 收益

                # 保存数据到列表
                data.append({
                    "日期": date,
                    "净值": net_worth,
                    "每天涨幅 (%)": f"{growth_rate}%",
                    "收益 (元)": daily_profit,  # 相对2024-09-13的涨幅
                    "总金额（元）": total_value,
                    "相对09/13涨幅 (%)": f"{round(net_worth_change, 2)}%"
                })

    # 将数据转换为 DataFrame
    df = pd.DataFrame(data)

    # 保存数据到 Excel 文件
    excel_filename = "fund_159691_nav_and_profit.xlsx"
    df.to_excel(excel_filename, index=False)

    print(f"数据已保存到 {excel_filename}")

else:
    print("未能匹配到净值数据。")
