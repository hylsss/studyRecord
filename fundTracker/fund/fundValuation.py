import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('../updated_fund_holdings_with_pe.csv')

# 将'持仓市值（万元人民币）'列转换为数字，移除非数字字符（如逗号）
df['持仓市值（万元人民币）'] = pd.to_numeric(df['持仓市值（万元人民币）'].replace({',': ''}, regex=True))

# 将‘市盈率’列转换为数值类型
df['市盈率'] = pd.to_numeric(df['市盈率'], errors='coerce')

# 计算每行的持仓市值（万元人民币）/市盈率
df['持仓市值（万元）/市盈率'] = df['持仓市值（万元人民币）'] / df['市盈率']

# 计算持仓市值的总和（不需要再乘以10000）
total_value = df['持仓市值（万元人民币）'].sum()

# 计算 持仓市值（万元）/市盈率 的总和
total_pe = df['持仓市值（万元）/市盈率'].sum()

# 输出结果
print(f"持仓市值的总和是: {total_value} 万元")

# 基金估值
print(f"基金估值：{total_value/total_pe}")
