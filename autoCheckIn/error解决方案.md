### chromeDriver版本不匹配

这个错误提示表明你正在使用的ChromeDriver版本与你的Chrome浏览器版本不兼容。错误信息显示，ChromeDriver只支持Chrome版本126，而你当前的浏览器版本是128.0.6613.84。为了解决这个问题，你有几个选项：

1. **更新ChromeDriver**：这是最常见的解决方法。确保你的ChromeDriver与你的Chrome浏览器版本相匹配。你可以从ChromeDriver下载页面获取与你当前浏览器版本相对应的最新版本的ChromeDriver。

2. **降级Chrome浏览器**：如果你因为某些原因需要继续使用当前的ChromeDriver，你可以考虑将Chrome浏览器降级到与你的ChromeDriver兼容的版本。

3. **自动管理ChromeDriver**：使用如`webdriver-manager`这样的工具可以自动管理WebDriver的版本，使其与你的浏览器版本保持一致。这可以简化环境的维护工作。你可以通过以下命令安装这个库：

   ```
   pip install webdriver-manager
   ```

   然后在你的代码中使用它：

   ```
   from selenium import webdriver
   from webdriver_manager.chrome import ChromeDriverManager
   
   driver = webdriver.Chrome(ChromeDriverManager().install())
   ```

使用上述任何一种方法都可以解决版本不匹配的问题。通常推荐更新ChromeDriver，因为这样可以确保你使用的是最新的功能和安全性更新。



#### 使用较新版本的Selenium的问题导致chromedriver报错

这个错误是因为你使用了 `executable_path` 参数，而在较新版本的 Selenium 中，`webdriver.Chrome` 不再接受 `executable_path` 作为参数。

### 解决方法

你应该使用 `Service` 类来指定 ChromeDriver 的路径。以下是正确的代码示例：

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 如果你已经知道 chromedriver 的路径，可以直接指定
chromedriver_path = '/usr/local/bin/chromedriver'

# 创建一个 Service 对象
service = Service(chromedriver_path)

# 启动 Chrome 浏览器
driver = webdriver.Chrome(service=service)

```

#### 解释

- **Service**：用于封装 ChromeDriver 的路径信息，并且 Selenium 会通过这个对象来启动 ChromeDriver。
- **webdriver.Chrome(service=service)**：这是新的方式来初始化 ChromeDriver，替代了旧版本的 `executable_path` 参数。



#### 较旧版本的selenium版本的

```python
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
```

