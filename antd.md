### select  onChange

```javascript
#index.ts

interface IUser {
  label： string
  value： string
  age: number
}

const handleChange = (value： string) => {
  //打印出选中的options的value
  console.log(value)

}

//这个写法是为了获取选中option的整块信息
const handleChange = (value: string, options: IUser | IUser[]) => {
  //要先判断出options是不是数组
  //单选
  !Array.isArray(options) && console.log(options)
  //多选
  Array.isArray(options) && console.log(options)
}
```

```html
<Select
    showSearch
    value={userData.userName}
    style={{ width: `100%` }}
    defaultActiveFirstOption={false}
    showArrow={false}
    filterOption={false}
    notFoundContent={null}
    onSearch={handleStaffSearch}
    onChange={handleStaffChange}
    options={staffInfoData.map((data) => ({
      value: data.id,
      label: data.userName,
      nameCn: data.nameCn,
      nameEn: data.nameEn,
    }))}
/>
```

### ConfigProvider全局化配置

###
