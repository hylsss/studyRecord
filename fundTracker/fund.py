import xalpha as xa
import matplotlib.pyplot as plt

# 实例化基金信息对象
fund = xa.fundinfo('260112')

# 定义开始日期和结束日期
start_date = '2024-01-01'
end_date = '2024-12-31'

# 筛选出指定日期区间的净值数据
price_data = fund.price
filtered_data = price_data[(price_data['date'] >= start_date) & (price_data['date'] <= end_date)]
print(filtered_data)

# 检查是否有数据
if not filtered_data.empty:
    # 绘制净值走势
    plt.figure(figsize=(12, 6))
    plt.plot(filtered_data['date'], filtered_data['netvalue'], marker='o', linestyle='-', color='b', label='Net Value')

    # 在每个数据点上添加净值标签
    for i in range(len(filtered_data)):
        date = filtered_data.iloc[i]['date']
        netvalue = filtered_data.iloc[i]['netvalue']
        plt.text(date, netvalue, f'{netvalue:.2f}', fontsize=8, ha='center', va='bottom')

    plt.xlabel('Date')
    plt.ylabel('Net Value (NAV)')
    plt.title(f'Net Value Trend from {start_date} to {end_date}')
    plt.xticks(rotation=45)  # 旋转X轴日期标签，防止重叠
    plt.grid(True)  # 添加网格线
    plt.tight_layout()  # 自动调整子图参数
    plt.legend()
    plt.show()
else:
    print("指定日期区间内没有数据，请检查日期是否正确。")
