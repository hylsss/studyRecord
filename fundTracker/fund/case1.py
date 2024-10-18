import akshare as ak
import pandas as pd

# 获取股票基金持仓详细信息
stock_report_fund_hold_detail_df = ak.stock_report_fund_hold_detail(symbol="512600", date="20240630")

# 检查 DataFrame 是否为空
if stock_report_fund_hold_detail_df is not None:
    # 将 DataFrame 保存到 Excel 文件
    stock_report_fund_hold_detail_df.to_excel('fund_hold_detail_512600_20240630.xlsx', index=False)
    print("数据已保存到 Excel 文件。")
else:
    print("获取的数据为空。")


fund_stars_all = ak.fund_rating_all()

if fund_stars_all is not None:
    # 将 DataFrame 保存到 Excel 文件
    fund_stars_all.to_excel('fund_all.xlsx', index=False)
    print("数据已保存所有基金评级文件。")
else:
    print("获取的数据为空。")
print(fund_stars_all)