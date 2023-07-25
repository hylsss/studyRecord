

//`CurrencyType` 是一个枚举类型

export  enum CurrencyType {
  Coin,
  // 可以在这里添加其他枚举值
}



export const CurrencyTypeString: { [key: number]: string } = {
[CurrencyType.Coin]: "Coin",
  // 在这里添加其他枚举值对应的字符串
};

调用CurrencyTypeString[item.valueCurrency]