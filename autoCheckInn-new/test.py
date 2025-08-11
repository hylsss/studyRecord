import logging

# 配置日志格式和级别
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add_numbers(a, b):
    """
    将两个数字相加，并记录结果到日志。

    :param a: 第一个数字
    :param b: 第二个数字
    :return: 两个数字的和
    """
    result = a + b
    logging.info(f"Sum of {a} and {b} is {result}")
    return result

# 调用函数并记录结果
result = add_numbers(6, 19)
logging.info(f"你好啊, 结果是: {result}")
