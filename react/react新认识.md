```react
import React from "react"; 
import logo from "./logo.svg"; 
import "./App.css"; 
```

第一句代码引入了 React 库，这是为了将代码中的 JSX 语句转为 `React.createElement()` ，所有的 React 模块都应该引入 React 模块，否则会抛错。

第二句代码引入了 `'./logo.svg'` 。注意文件路径以 `./` 开头、由 `.svg` 尾——表明这是一个本地文件，并且它不是 JavaScript 文件。

第三行引入了我们的组件所需的 CSS 文件。与上面两句不同，这里没有将引入的内容赋给任何变量、也没有用到 `from` 指令。<u>请注意这种特殊的语法并非原生 JS 的语法 —— 它源自前端资源打包工具 webpack，而 create-react-app 正是基于 webpack 配置而来的。

# index.ts

```react
ReactDOM.render(<App />, document.getElementById("root"));
```

传入两个参数 1. 要渲染的组件 2. 在 index.html 哪个地方渲染

**备注：** 在 JSX 中，React 组件和 HTML 元素必须有关闭斜杠（ `/` ），如 `<App />` ，如果我们写 `<App>` 或者 `<img>` 将会报错。

[Service workers](https://developer.mozilla.org/zh-CN/docs/Web/API/Service_Worker_API/Using_Service_Workers)

```javascript
import * as serviceWorker from "./serviceWorker";
```

```javascript
serviceWorker.unregister();
```

[Service workers](https://developer.mozilla.org/zh-CN/docs/Web/API/Service_Worker_API/Using_Service_Workers) 能让我们的 App 离线运行可以删除。

props 传值

组件传值 props 是对象 object

在 React 中：

* 组件可以 import 它们需要的模块，并且在文件底部将自身 export，以让其他组件使用。
* 组件是用 `PascalCase` 也就是帕斯卡命名法命名的。
* 通过把变量放在大括号中，您可以读取 JSX 的变量，如`{so}`
* 一些 JSX 属性与 HTML 属性不相同，这样就不会与 JavaScript 的保留字相冲突，比如说，在 HTML 中的 `class` 会在 JSX 中转译为 `className`。注意这些属性都是驼峰式命名的。
* Props 属性一样写在组件里，并且传入组件。
