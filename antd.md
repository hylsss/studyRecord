## select  onChange

```react
export interface IUser {
  label: string;
  value: string;
  age: number;
}

const handleChange = (value: string) => {
  // 打印出选中的 options 的 value
  console.log(value);
};

// 这个写法是为了获取选中 option 的整块信息
const handleChange = (value: string, options: IUser | IUser[]) => {
  // 要先判断 options 是不是数组
  // 单选
  if (!Array.isArray(options)) {
    console.log(options);
  }
  // 多选
  if (Array.isArray(options)) {
    console.log(options);
  }
};

```



```react
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
```



## ConfigProviderq全局配置

```react
import type { ThemeConfig } from 'antd';
import { theme } from 'antd';

const config: ThemeConfig = {
  token: {
    colorPrimary: '#1890ff',
  },
};
//全局配置
  <ConfigProvider
    theme={{
      token: {
        colorPrimary: '#00b96b',
      },
    }}
  >
    <Button />
  </ConfigProvider>
```



## antd Upload组件

不显示上传文件的文件名  showUploadList 设置 false

展示代码是只上传一张图，并且在图片上传后隐藏 add 按钮的写法。

##### 有个小坑 还得去研究一下这玩意是为啥

使用 `beforeUpload` 的时候，设置了可以上传图片的大小，不管是返回的 `boolean` 格式还是 `Promise<File>` 的格式，会有拦截提示但是会触发 `onChange` 方法，且 `onChange` 返回的file对象，里面没有 `status` 参数，正常是会有 `status` , 可以通过 `status` 去判断可不可以上传。

##### 解决方案：

可以通过 `onChange` 的size去判断是都要上传， `true` 就往下执行， `false` 就 `return` 错误

404的时候设置成 `beforeUpload={() => false}` 控制台就不会报警了, 因为 `beforeUpload` 是自动上传的，设置成false的话，就是阻止了 `文件自动上传` ，如果你不想使用false的话，有两个解决方案

方案一：使用 `customRequest` 覆盖自动上传的逻辑，

```ruby
  <Upload
    listType="text"
    fileList={fileList}
    showUploadList={false}
    maxCount={1}
    beforeUpload={beforeUpload}
    customRequest={handleUploadImg}
    className="w-24"
    accept="image/*"
  >
    <Button
      type="primary"
      className="w-24"
      loading={loading}
      disabled={loading}
    >
          上传
    </Button>
  </Upload>
  
// beforeUpload的拦截逻辑
  const beforeUpload = (file: RcFile): Promise<RcFile> => {
    return new Promise((resolve, reject) => {
      const maxSize = file.size / 1024 / 1024 > 20;
      if (maxSize) {
        message.error("请上传20M以内的图片！");
        reject(file);
      } else {
        setUploadVal({
          ...uplaodVal,
          inputVal: file.name,
        });
        console.log(file);

        resolve(file);
      }
    });
  };
   
// customRequest 覆盖自动上传的逻辑，如果不能通过beforeUpload的校验就不会进入到这一步
 const handleUploadImg = (info: { file: string | Blob | RcFile }) => {
    const formData = new FormData();
    formData.append("file", info.file);
    const newfile: UploadFile[] = [];

    setLoading(true);
    PostUrlImg(formData)
      .then((res) => {
        if (res) {
          setLoading(false);
          message.success(`上传成功`);
          newfile.push({ url: res.fileUrl, uid: "", name: uplaodVal.inputVal });
          setFileList(newfile);
          setUploadVal({
            ...uplaodVal,
            uploadId: res.id,
          });
        }
      })
      .catch((error) => {
        setLoading(false);
      });
  };
```

 #####  方案二 ：设置action，把你上传图片的接口丢进去，然后配置headers，data（你传的参数），就可以解决的了，但是不建议这个方案，容易忘了修改action的接口，还得传headers配置（推荐方案一）

###  只上传一张图片，上传图片后隐藏add的操作，

```react
//upload组件只上传一张图片
  <Upload
    listType="picture-card"
    fileList={fileList}
    maxCount={1}
    onChange={handleChange}
    beforeUpload={() => false}
    className="mt-4"
    accept="image/*"
    onRemove={handleRemove}
  >
    {fileList.length ? null : (
      <div>
        {!loading && !fileList.length ? (
          <div>
            <PlusOutlined />
            <div style={{ marginTop: 8 }}>Uplaod</div>
          </div>
        ) : (
          <div>
            <Spin size="large" spinning={loading} className="self-center" />
          </div>
        )}
      </div>
    )}
  </Upload>;
              

```


## Form组件的坑

###  小坑

1. `<Form.Item>`中只能包含一个`value`，否则会读取不到多个`value`
2. Select组件，要把`value`设置成`null`或者`undefined`，不然设置成`""`空字符会不显示placeholder的提示
3. DatePicker的默认值，使用**时间戳形式**,默认值直接传**空字符**会报错的。

###  奇奇怪怪的总结

1. `Form` 表单使用`name`属性绑定表单的值，表单控件会自动添加`value`值，数据同步要干的事就会被 `form` 接管，所以我们使用`setState`去设置值，跟表单的值是没有关系的。
2.  `Form` 表单值更新的时候使用 `form.setFieldsValue` 来动态改变表单的值
3. 获取  `Form` 表单的值使用 `form.getFieldValue`来获取对应的值 ，`form.getFieldsValue`获取表单全部的值.
4. 当然也可以继续使用 `onChange`  方法，但是显示的时候要跟对应的组件value绑定，例如 `Select`  组件 要跟对应的`value` 值绑定，不然回显不出来，或者使用 Form 组件自己的监听方法 `onValuesChange`  继续监听值的变化

### modal清空表单的数据

##### 方案一：

```react
// 关闭弹窗后在父组件直接调用子组件的reset方法
const [form] =Form.useForm();
form.resetFields();
```

##### 方案二: 该方案还没有尝试过

```react
// destroyOnClose 关闭时销毁 Modal 里的子元素 默认为false
<Modal destroyOnClose={true}>
  // preserve 当字段被删除时保留字段值 默认为true
  <Form preserve={false}></Form>
</Modal>;

```

####  方案二的话可以省去封装了组件，把resetFields()方法传过去父组件的步骤。
