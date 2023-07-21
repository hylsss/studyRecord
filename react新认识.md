import React from "react";
import logo from "./logo.svg";
import "./App.css";

第一句代码引入了 React 库，这是为了将代码中的 JSX 语句转为`React.createElement()`，所有的 React 模块都应该引入 React 模块，否则会抛错。

第二句代码引入了 `'./logo.svg'`。注意文件路径以 `./` 开头、由 `.svg` 尾——表明这是一个本地文件，并且它不是 JavaScript 文件。

第三行引入了我们的组件所需的 CSS 文件。与上面两句不同，这里没有将引入的内容赋给任何变量、也没有用到 `from` 指令。<u>请注意这种特殊的语法并非原生 JS 的语法 —— 它源自前端资源打包工具 webpack，而 create-react-app 正是基于 webpack 配置而来的。

# index.ts

```
ReactDOM.render(<App />, document.getElementById("root"));
```

传入两个参数 1.要渲染的组件 2.在 index.html 哪个地方渲染

**备注：** 在 JSX 中，React 组件和 HTML 元素必须有关闭斜杠（`/`），如 `<App />`，如果我们写 `<App>` 或者 `<img>` 将会报错。

[Service workers](https://developer.mozilla.org/zh-CN/docs/Web/API/Service_Worker_API/Using_Service_Workers)

```
import * as serviceWorker from "./serviceWorker";
```

```
serviceWorker.unregister();
```

[Service workers](https://developer.mozilla.org/zh-CN/docs/Web/API/Service_Worker_API/Using_Service_Workers) 能让我们的 App 离线运行可以删除。

props 传值

组件传值 props 是对象 object

在 React 中：

- 组件可以 import 它们需要的模块，并且在文件底部将自身 export，以让其他组件使用。
- 组件是用 `PascalCase` 也就是帕斯卡命名法命名的。
- 通过把变量放在大括号中，您可以读取 JSX 的变量，如`{so}`
- 一些 JSX 属性与 HTML 属性不相同，这样就不会与 JavaScript 的保留字相冲突，比如说，在 HTML 中的 `class` 会在 JSX 中转译为 `className`。注意这些属性都是驼峰式命名的。
- Props 属性一样写在组件里，并且传入组件。

const useAction = () => {
const { teamId } = useAuth();

const editValue = useContext(EditContext);

const quotationRef = useRef<IModalBoxRef>(null);

const [isActive, setIsActive] = useState<boolean>(false);

const [status, setStatus] = useState<IReceptionsStateEnum>();

const [requirementId, setRequirementId] = useState<string>("");

const [isCloseShow, setIsCloseShow] = useState<boolean>(true);

const [loading, setLoading] = useState<boolean>(true);

const initData = {
pageIndex: 1,
pageSize: 10,
total: 0,
totalPages: 1,
data: [],
};

const [receptionListData, setReceptionListData] =
useState<ITeamRequirementsListResponse>(initData);

const [pageDto, setPageDto] = useState<IPageInfo>({
pageIndex: 1,
pageSize: 10,
});

useEffect(() => {
setPageDto({ pageIndex: 1, pageSize: pageDto.pageSize });
}, [editValue.inputNameValue, editValue.selectStatus]);

const fetchData = async () => {
setLoading(true);
TeamRequirementsList({
pageIndex: pageDto.pageIndex,
pageSize: pageDto.pageSize,
tenantId: teamId,
isTenantPosted: false,
status:
editValue.selectStatus >= IReceptionsStateEnum.PendingQuoting
? editValue.selectStatus
: undefined,
name: editValue.inputNameValue,
})
.then((res) => {
setReceptionListData(res);
setLoading(false);
})
.catch(() => {
setLoading(false);
setReceptionListData(initData);
});
};

useEffect(() => {
if (teamId) {
fetchData();
} else {
setReceptionListData(initData);
}
}, [
editValue.flag,
editValue.selectStatus,
editValue.inputNameValue,
teamId,
pageDto,
]);

useEffect(() => {
const closedStatuses = [
IReceptionsStateEnum.Quoted,
IReceptionsStateEnum.Developing,
IReceptionsStateEnum.Archived,
IReceptionsStateEnum.Closed,
];

    status && setIsCloseShow(!closedStatuses.includes(status));

}, [status]);

const handleClickPage = (page: number, pageSize: number) => {
setPageDto({
pageIndex: page,
pageSize: pageSize,
});
};

const getOperationType = (status: IReceptionsStateEnum) => {
switch (status) {
case IReceptionsStateEnum.PendingQuoting:
return ITeamReceptionOperateEnum.Quotation;
case IReceptionsStateEnum.Quoted:
return ITeamReceptionOperateEnum.CheckQuotation;
case IReceptionsStateEnum.PendingDevelop:
return ITeamReceptionOperateEnum.AssignOrder;
default:
return ITeamReceptionOperateEnum.View;
}
};

return {
quotationRef,
isActive,
status,
receptionListData,
requirementId,
isCloseShow,
loading,
pageDto,
setStatus,
handleClickPage,
setRequirementId,
getOperationType,
};
};
