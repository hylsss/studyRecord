## package.json配置文件

#####  `package.json` 是一个用于描述和配置项目的重要文件，其中包含了许多字段和选项，可以影响项目的构建、依赖管理、脚本执行等方面。了解这些字段可以帮助开发者更好地理解和控制项目的行为。

##### `package.json`对于大部分前端开发者来说，知道`dependencies`与`devDependencies`就够了。但对于库开发者或有更高级需求的开发者来说，了解 `package.json` 的其他字段是非常有必要的。

### 一 、必须属性

1. name :定义项目的名称，不能以"."和"_"开头，不能包含大写字母
2. version：定义项目的版本号，格式为：大版本号.次版本号.修订号

###  二、描述信息
1.  description 项目描述
2.  keywords  项目关键词
3.  author 项目作者  `"author": "name (http://barnyrubble.tumblr.com/)"
    `
4.  contributors  项目贡献者
    `  "contributors": [
    "name <b@rubble.com> (http://barnyrubble.tumblr.com/)"
    ]`
5.  homepage 项目主页地址
6.  repository 项目代码仓库地址
7.  bugs  项目提交问题的地址
` //提交问题的地址和反馈的邮箱,url通常是Github中的issues页面
"bugs": { 
    "url" : "https://github.com/facebook/react/issues", 
    "email" : "xxxxx@xx.com"
}`
8.   funding  指定项目的资金支持方式和链接
`  "funding": {
    "type": "patreon",
    "url": "https://www.patreon.com/my-module"
    }
`

###  三、依赖配置
1. dependencies 生产环境的依赖包。(npm,yarna  安装的包)
如果不使用脱字符（^），安装的版本号固定；如果使用，则能安装当前大版本的最新版本，在package-lock.json中可查看当前实际安装的版本。
2. devDependencies `开发环境`的依赖包，例如webpack、vite、babel、ESLint等。

